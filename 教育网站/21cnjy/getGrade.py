#!/usr/bin/python

import pymysql
import re
import requests
import json
# 这个文件是获取所有教材的所有年级
import threading

def getDBcon():
    # 连接数据库
    db = pymysql.connect(
        "localhost",
        "root",
        "zqt1997",
        "21cnjy",
        use_unicode=True,
        charset="utf8")
    cursor = db.cursor()
    return db, cursor


def getJson(xd, chid, upid):
    url = 'https://www.21cnjy.com/soft.php?mod=zyindex_ajax&categories=1&xd=%d&chid=%d&upid=%d' % (
        xd, chid, upid)
    text = requests.get(url).text
    js = json.loads(text)
    return js


def getGrade(data):
    db, cursor = getDBcon()
    for line in data:
        sid = line[0]
        print(sid)
        tmId = line[1]
        xd = line[2]
        chid = line[3]
        js = getJson(xd, chid, tmId)
        for grade in js:
            gradeName=grade['name']
            gradeId=grade['id']
            child=grade['child']
            sql='insert into grade values (%s,%s,%s,%s)'
            cursor.execute(sql,(gradeName,gradeId,sid,child))
            db.commit()
    db.close()



def work():
    db, cursor = getDBcon()
    cursor.execute('select id,tmId,xd,chid from teachingmaterial')
    data = cursor.fetchall()
    dataLen=len(data)
    tnum = 20
    x = dataLen // tnum
    Thead = []
    for r in range(0, tnum):
        t = threading.Thread(target=getGrade, args=(data[r * x:r * x + x], ))
        Thead.append(t)
    t = threading.Thread(target=getGrade, args=(data[x * tnum:dataLen], ))

    Thead.append(t)
    for t in Thead:
        t.start()

    for t in Thead:
        t.join()
    db.close()

if __name__ == '__main__':
    work()
    