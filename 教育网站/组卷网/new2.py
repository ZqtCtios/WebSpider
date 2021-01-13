import json
import os
import threading
import time

import pymysql
import requests
from bs4 import BeautifulSoup
headers = {
    'Host':
    'www.zujuan.com',
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36',
    'X-Requested-With':
    'XMLHttpRequest'
}


data = [{'subjectId': 's101', '21_id': 2, 'name': '小学语文', 'xd': 1, '21_grade': '160080', 'grade': 158737},
        {'subjectId': 's101', '21_id': 2, 'name': '小学语文',
            'xd': 1, '21_grade': '160568', 'grade': 158738},
        {'subjectId': 's101', '21_id': 2, 'name': '小学语文',
            'xd': 1, '21_grade': '160570', 'grade': 158739},
        {'subjectId': 's101', '21_id': 2, 'name': '小学语文',
         'xd': 1, '21_grade': '160572', 'grade': 158740},
        {'subjectId': 's101', '21_id': 2, 'name': '小学语文',
         'xd': 1, '21_grade': '160574', 'grade': 158741},
        {'subjectId': 's101', '21_id': 2, 'name': '小学语文',
         'xd': 1, '21_grade': '160576', 'grade': 158742},
        {'subjectId': 's201', '21_id': 2, 'name': '初中语文',
         'xd': 2, '21_grade': '534', 'grade': 534},
        {'subjectId': 's201', '21_id': 2, 'name': '初中语文',
         'xd': 2, '21_grade': '127893', 'grade': 127893},
        {'subjectId': 's201', '21_id': 2, 'name': '初中语文',
         'xd': 2, '21_grade': '133168', 'grade': 133168},
        {'subjectId': 's201', '21_id': 2, 'name': '初中语文',
         'xd': 2, '21_grade': '139276', 'grade': 134888},
        {'subjectId': 's201', '21_id': 2, 'name': '初中语文',
         'xd': 2, '21_grade': '146576', 'grade': 146576},
        {'subjectId': 's201', '21_id': 2, 'name': '初中语文', 'xd': 2, '21_grade': '154302', 'grade': 158821}]


def getJson(xd, chid, categories, page):
    url = 'https://zujuan.21cnjy.com/api/question/list?xd={}&chid={}&categories={}&page={}'.format(
        xd, chid, categories, page)
    jsonText = requests.get(url, headers=headers).text
    return jsonText


def getAnalyses():
    pass


def findChapterToProblem(grade):
    db = pymysql.connect(
        "localhost",
        "root",
        "zqt1997",
        "hdkt_dev",
        use_unicode=True,
        charset="utf8")
    cursor = db.cursor()
    sql = 'select id from problem'
    cursor.execute(sql)
    data2 = cursor.fetchall()
    problemIds = []
    for line in data2:
        problemIds.append(line[0])
    sql = 'select id,spiderId from chapter where gradeId={} and parentId<>0'.format(
        grade['grade'])
    cursor.execute(sql)
    data = cursor.fetchall()
    xd = grade['xd']
    chid = grade['21_id']
    print('grade:', grade['grade'])
    for line in data:
        chapterId = line[0]
        print('chapterId:', chapterId)
        spiderId = line[1]
        jsonData = getJson(xd, chid, spiderId, '')
        jsonData = json.loads(jsonData)['data']
        sum = jsonData['total']
        print('total:', sum)
        page = 1
        while sum > 0:
            jsonData = getJson(xd, chid, spiderId, page)
            jsonData = json.loads(jsonData)['data']
            for problem in jsonData['questions']:
                scrapId = problem['question_id']
                sql = 'insert into problem_chapter(chapterId,problemId) values (%s,%s)'
                cursor.execute(sql, (chapterId, scrapId))
            page += 1
            sum -= 10
            db.commit()
    db.close()


def MultiThread():
    Thead = []
    for grade in data:
        t = threading.Thread(
            target=findChapterToProblem,
            args=(
                grade,
            ))
        Thead.append(t)

    for t in Thead:
        t.start()

    for t in Thead:
        t.join()


if __name__ == "__main__":
    MultiThread()
