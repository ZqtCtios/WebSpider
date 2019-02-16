#!/usr/bin/python
from bs4 import BeautifulSoup
import pymysql
import requests
import json
import threading


def getDBcon():
    db = pymysql.connect(
        "60.205.224.56",
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
        'select id,grade_id,chapter_id,xd,chid,subject_id from chapter2 where ok=0')
    data = cursor.fetchall()
    db.close()
    return data


def getJson(xd, chid, catid, page, diquid, bookversion):
    url = 'https://www.21cnjy.com/soft.php'
    data = {
        'mod': 'list',
        'xd': xd,
        'chid': chid,
        'catid': catid,
        'page': page,
        'typeid': '',
        'isjin': 0,
        'diquid': diquid,
        'stars': 0,
        'bookversion': bookversion,
        'async_update': '1'
    }
    html = requests.get(url, params=data,timeout=10).text
    return html


def getDocument(data):
    db, cursor = getDBcon()
    area_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17,
                 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 35, 36]
    for dataLine in data:
        try:
            cid = dataLine[0]
            subjectId = dataLine[5]
            tmId = 0
            gradeId = dataLine[1]
            chapterId = dataLine[2]
            xd = dataLine[3]
            chid = dataLine[4]
            itemData = []
            cursor.execute(
                'select id,bookversion from SpeTm where subjectId=%s', (subjectId))
            bookversions = cursor.fetchall()
            for x in bookversions[0:]:
                tmId = x[0]
                bookversion = x[1]
                if int(bookversion)==0:
                    continue
                for area_sp_id in area_data:
                    page = 0
                    while True:
                        #print(cid,bookversion,area_sp_id,page)
                        if page==100:
                            print('Too big',cid)
                            
                        page += 1
                        html = getJson(xd, chid, chapterId, page,
                                    area_sp_id, bookversion)
                        js = json.loads(html)['list']
                        if len(js) == 0:
                            break
                        i = 0
                        for line in js:
                            itemId = line['itemid']
                            if itemId not in itemData:
                                itemData.append(itemId)
                            else:
                                continue
                            i += 1
                            documentName = line['nice_subject']
                            documentExpain = line['softintro']
                            downUrl = line['downurl']
                            dateTime = line['nice_datetime']
                            typeName = line['nice_typeicon']
                            downNum = line['downnum']
                            uid = line['uid']
                            userName = line['username']
                            typeidroot = line['typeidroot']
                            flag = int(line['flag'])
                            stars = int(line['stars'])
                            if flag == 7:
                                flag = 1
                            elif flag == 8:
                                flag = 2
                            else:
                                flag = 3
                            if stars <= 2:
                                stars = 12
                            elif stars <= 4:
                                stars = 34
                            else:
                                stars = 5
                            sql = 'INSERT INTO document2(document_classify,subject_id,teachingmaterial_id,grade_id,chapter_id,document_name,document_explain,url,file_type,used_count,prepare_lesson_type,prepare_lesson_importance,prepare_lesson_area,prepare_lesson_level,teacher_id,document_source,show_sort,show_time,document_id,userName)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                            cursor.execute(sql, (1, subjectId, tmId, gradeId, cid, documentName, documentExpain, downUrl,
                                                typeName, downNum, typeidroot, flag, area_sp_id, stars, uid, 2, i, dateTime, itemId, userName))
                            
            sql = 'update chapter2 set ok=1 where id=%s'
            print(cid)
            cursor.execute(sql, (cid))
            db.commit()
        except:
            continue


def work():
    data = getData()
    dataLen = len(data)
    tnum = 30
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
