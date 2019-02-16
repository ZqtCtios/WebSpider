#!/usr/bin/python
from bs4 import BeautifulSoup
import pymysql
import requests
import json
import threading


def getDBcon():
    db = pymysql.connect(
        "localhost",
        "root",
        "Zqt_1997",
        "21cnjy",
        use_unicode=True,
        charset="utf8")
    cursor = db.cursor()
    return db, cursor


def getData():
    db, cursor = getDBcon()
    cursor.execute(
        'select * from knowledge where ok=0')
    data = cursor.fetchall()
    db.close()
    return data


def getJson(xd, chid, kid, page):
    url = 'https://www.21cnjy.com/knowledge.php'
    data = {
        'kid': kid,
        'xd': xd,
        'chid': chid,
        'page': page,
        'async_update': '1'
    }
    html = requests.get(url, params=data).text
    return html


def findType(x):
    a = [0, 3, 8, 7, 4, 6, 12]
    for i in range(len(a)):
        if a[i] == x:
            return i+1
    return 1


def getDocument(data):

    db, cursor = getDBcon()
    for dataLine in data:
        kid = dataLine[0]
        subjectId = dataLine[1]
        knowledgeId = dataLine[2]
        chid = dataLine[3]
        xd = dataLine[4]
        page = 0
        while True:
            page += 1
            html = getJson(xd, chid, knowledgeId, page)
            js = json.loads(html)['list']
            if len(js) == 0:
                break
            if page == 100:
                print("Data too Big kid={}".format(kid))
            i = 0
            for line in js:
                itemId = line['itemid']
                i += 1
                documentName = line['nice_subject']
                documentExpain = line['softintro']
                downUrl = line['downurl']
                dateTime = line['nice_datetime']
                typeName = line['nice_typeicon']
                downNum = line['downnum']
                uid = line['uid']
                userName = line['username']
                typeidroot = int(line['typeidroot'])
                typeidroot = findType(typeidroot)
                stars = 0
                flag = 0

                sql = 'INSERT INTO document3(document_classify,subject_id,teachingmaterial_id,grade_id,chapter_id,document_name,document_explain,url,file_type,used_count,prepare_lesson_type,prepare_lesson_importance,prepare_lesson_area,prepare_lesson_level,teacher_id,document_source,show_sort,show_time,document_id,userName)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                cursor.execute(sql, (1, subjectId, 0, 0, kid, documentName, documentExpain, downUrl,
                                     typeName, downNum, typeidroot, flag, 0, stars, uid, 2, i, dateTime, itemId, userName))
                # print(1, subjectId, 0, 0, 0, documentName, documentExpain, downUrl,
                #                     typeName, downNum, typeidroot, flag, 0, stars, uid, 2, i, dateTime, itemId, userName)
                db.commit()
        sql = 'update knowledge set ok=1 where id=%s'
        print(kid)
        cursor.execute(sql, (kid))
        db.commit()


def work():
    data = getData()
    dataLen = len(data)
    tnum = 40
    print(dataLen)
    x = dataLen // tnum
    Thead = []
    for r in range(0, tnum):
        t = threading.Thread(target=getDocument,
                             args=(data[r * x:r * x + x], ))
        Thead.append(t)
    t = threading.Thread(target=getDocument, args=(data[x * tnum:dataLen], ))

    Thead.append(t)
    for t in Thead:
        t.start()

    for t in Thead:
        t.join()


if __name__ == '__main__':
    work()
