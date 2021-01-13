# -*- coding: utf-8 -*-
# @Time    : 2019-08-31 16:30
# @Author  : ctios
# @Software: PyCharm
import json
import os
import threading
import time

import pymysql
import requests
import re
from bs4 import BeautifulSoup

headers = {
    'Host':
    'www.zujuan.com',
        'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36',
        'X-Requested-With':
    'XMLHttpRequest'
}
db = pymysql.connect(
    "localhost",
    "root",
    "zqt1997",
    "hdkt_dev",
    use_unicode=True,
    charset="utf8")
cursor = db.cursor()

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
    url = 'https://zujuan.21cnjy.com/api/paper/paper-category-list?xd={}&chid={}&categories={}&page={}'.format(
        xd, chid, categories, page)
    jsonText = requests.get(url, headers=headers).text
    return jsonText


def findPage(grade):
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
    xd = grade['xd']
    chid = grade['21_id']
    spiderId = grade['21_grade']
    jsonData = getJson(xd, chid, spiderId, '')
    jsonData = json.loads(jsonData)['data']
    sum = jsonData['total']
    subjectId = grade['subjectId']
    gradeId = grade['grade']
    teachingMaterialId = 123489
    page = 1
    while sum > 0:
        jsonData = getJson(xd, chid, spiderId, page)
        jsonData = json.loads(jsonData)['data']
        for paper in jsonData['list']:
            paperName = paper['title']
            pid = paper['pid']
            paperExplain = paper['description']
            paperType = paper['papertype']
            print('gradeId:', gradeId, 'paper:', pid)
            sql = 'insert into paper(id,paperName,paperExplain,gradeId,subjectId,teachingMaterialId,paperType) values (%s,%s,%s,%s,%s,%s,%s)'
            cursor.execute(
                sql,
                (pid,
                 paperName,
                 paperExplain,
                 gradeId,
                 subjectId,
                 teachingMaterialId,
                 paperType))
            url = 'https://zujuan.21cnjy.com/paper/view/{}'.format(pid)
            html = requests.get(url, headers=headers).text
            p = html.find('paper_detail')
            p = html.find('{', p)
            q = html.find('query: query', p)
            jsonText = html[p:q].replace(' ', '')
            jsonText = jsonText[:-2]
            jsonData = json.loads(jsonText)['content'][0]
            sort = 0
            for problem in jsonData['questions']:
                scrapId = problem['question_id']
                sort += 1
                if int(scrapId) in problemIds:
                    sql = 'insert into paper_problem(paperId,problemId,sort) values (%s,%s,%s)'
                    cursor.execute(sql, (pid, scrapId, sort))
                    continue
                problemType = problem['question_channel_type']
                problemDiffculty = problem['difficult_index']
                problemKind = problem['exam_type']
                problemContent = problem['title']
                problemContentStr = problem['question_text']

                problemAnswer = str(problem['options'])
                problemAnswer = db.escape_string(problemAnswer)
                answer = problem['answer']
                try:
                    sql = 'insert into problem(id,scrapId,problemType,problemDiffculty,problemKind,problemContent,problemContentStr,problemAnswer,answer) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                    cursor.execute(
                        sql,
                        (scrapId,
                         scrapId,
                         problemType,
                         problemDiffculty,
                         problemKind,
                         problemContent,
                         problemContentStr,
                         problemAnswer,
                         answer))
                    sql = 'insert into paper_problem(paperId,problemId,sort) values (%s,%s,%s)'
                    cursor.execute(sql, (pid, scrapId, sort))
                except BaseException:
                    continue
                # analyses = getAnalyses()
                childList = problem['list']
                if childList is None:
                    childList = []
                for child in childList:
                    parentId = scrapId
                    scrapId = child['question_id']
                    problemType = child['question_channel_type']
                    problemDiffculty = child['difficult_index']
                    problemKind = child['exam_type']
                    problemContent = child['title']
                    problemContentStr = child['question_text']
                    problemAnswer = str(child['options'])
                    problemAnswer = db.escape_string(problemAnswer)
                    answer = child['answer']
                    # analyses = getAnalyses()
                    try:
                        sql = 'insert into problem(id,scrapId,problemType,problemDiffculty,problemKind,problemContent,problemContentStr,problemAnswer,answer,parentId) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                        cursor.execute(
                            sql,
                            (scrapId,
                             scrapId,
                             problemType,
                             problemDiffculty,
                             problemKind,
                             problemContent,
                             problemContentStr,
                             problemAnswer,
                             answer,
                             parentId))
                        sql = 'insert into paper_problem(paperId,problemId,sort) values (%s,%s,%s)'
                        cursor.execute(sql, (pid, scrapId, sort))
                    except BaseException:
                        continue
            db.commit()
        page += 1
        sum -= 10
    db.commit()


def MultiThread():
    Thead = []
    for grade in data:
        t = threading.Thread(
            target=findPage,
            args=(
                grade,
            ))
        Thead.append(t)

    for t in Thead:
        t.start()

    for t in Thead:
        t.join()


if __name__ == '__main__':
    MultiThread()
