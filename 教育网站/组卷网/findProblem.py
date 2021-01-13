import json
import threading
import pymysql
import requests
import logging

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(filename='spider.log', level=logging.info, format=LOG_FORMAT)

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Host': 'zujuan.21cnjy.com',
    'Pragma': 'no-cache',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}


def getQuestionData(xd, chid, categories, page):
    # 请求问题api
    url = 'https://zujuan.21cnjy.com/api/question/list?xd={}&chid={}&categories={}&page={}'.format(
        xd, chid, categories, page)
    jsonText = requests.get(url, headers=headers).json()
    return jsonText


def getGradeMsg():
    # 查到没有爬完的年级
    db = pymysql.connect(
        "localhost",
        "root",
        "zqt1997",
        "zujuan",
        use_unicode=True,
        charset="utf8")
    cursor = db.cursor()
    sql = "select * from spider where has_down = 0 limit 20"
    cursor.execute(sql)
    data = []
    for line in cursor.fetchall():
        temp = {}
        temp["id"] = line[0]
        temp["gid"] = line[1]
        temp["g_21_id"] = line[2]
        temp["gradeName"] = line[3]
        temp["tid"] = line[4]
        temp["t_21_id"] = line[5]
        temp["materialName"] = line[6]
        temp["subjectName"] = line[7]
        temp["xd"] = line[8]
        temp["chid"] = line[9]
        temp["has_down"] = line[10]
        data.append(temp)
    cursor.close()
    db.close()
    return data


def findChapterToProblem(grade):
    db = pymysql.connect(
        "localhost",
        "root",
        "zqt1997",
        "zujuan",
        use_unicode=True,
        charset="utf8")
    cursor = db.cursor()
    sql = "select id from problem"
    cursor.execute(sql)
    resData = cursor.fetchall()
    problemIds = []
    for line in resData:
        problemIds.append(line[0])
    sql = 'select id,spiderId,chapterName from chapter where gradeId={} and is_deleted = 0'.format(
        grade['gid'])
    cursor.execute(sql)
    chapter_data = cursor.fetchall()
    xd = grade['xd']
    chid = grade['chid']
    logging.info(f'正在爬取: {grade["subjectName"]}-{grade["materialName"]}-{grade["gradeName"]}')
    for line in chapter_data:
        chapterId = line[0]
        chapterName = line[2]
        logging.info(f'正在爬取章节: {chapterId}-{chapterName}')
        spiderId = line[1]
        try:
            jsonData = getQuestionData(xd, chid, spiderId, '')['data']
        except:
            logging.error("爬取失败")
            continue
        sum = jsonData['total']
        logging.info(f'total:{sum}')
        page = 1
        while sum > 0:
            try:
                jsonData = getQuestionData(xd, chid, spiderId, page)['data']
            except:
                continue
            for problem in jsonData['questions']:
                scrapId = problem['question_id']
                if int(scrapId) in problemIds:
                    sql = 'insert into problem_chapter(chapterId,problemId) values (%s,%s)'
                    cursor.execute(sql, (chapterId, scrapId))
                    continue
                problemType = problem['question_channel_type']
                problemDiffculty = problem['difficult_index']
                problemKind = problem['exam_type']
                if problemKind == '0':
                    problemKind = 3
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
                    sql = 'insert into problem_chapter(chapterId,problemId) values (%s,%s)'
                    cursor.execute(sql, (chapterId, scrapId))
                except BaseException:
                    continue
                childList = problem['list']
                if childList is None:
                    childList = []
                for child in childList:
                    parentId = scrapId
                    scrapId = child['question_id']
                    try:
                        problemType = child['question_channel_type']
                    except:
                        problemType = problem['question_channel_type']
                    try:
                        problemDiffculty = child['difficult_index']
                    except:
                        problemDiffculty = problem['difficult_index']
                    try:
                        problemKind = child['exam_type']
                    except:
                        problemKind = problem['exam_type']
                    if problemKind == '0':
                        problemKind = 3
                    try:
                        problemContent = child['title']
                    except:
                        problemContent = ""
                    problemContentStr = child['question_text']
                    problemAnswer = str(child['options'])
                    problemAnswer = db.escape_string(problemAnswer)
                    answer = child['answer']
                    sql = 'insert into problem(id,scrapId,problemType,problemDiffculty,problemKind,problemContent,problemContentStr,problemAnswer,answer,parentId) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                    try:
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
                        sql = 'insert into problem_chapter(chapterId,problemId) values (%s,%s)'
                        cursor.execute(sql, (chapterId, scrapId))
                    except BaseException:
                        continue
            db.commit()
            page += 1
            sum -= 10
        sql = 'update chapter set is_deleted = 1 where id={}'.format(chapterId)
        cursor.execute(sql)
        db.commit()
        logging.info("爬取成功")
    sql = 'update spider set has_down = 1 where id={}'.format(grade['id'])
    cursor.execute(sql)
    db.commit()
    db.close()


def MultiThreadWork(data):
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
    while True:
        data = getGradeMsg()
        if len(data) == 0:
            break
        MultiThreadWork(data)
