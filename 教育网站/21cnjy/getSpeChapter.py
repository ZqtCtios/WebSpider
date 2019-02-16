#!/usr/bin/python3

import pymysql
import re
import requests
import json
# 这个文件是获取所有教材的所有年级的所有章节
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
    url = 'https://www.21cnjy.com/soft.php?mod=zyindex_ajax&categories=1&xd=%s&chid=%s&upid=%s' % (
        xd, chid, upid)
    text = requests.get(url).text
    return text


def getChapter(pids, xd, chid, cid):
    db, cursor = getDBcon()
    for i in range(len(pids)):
        pid = pids[i]
        cdata = getJson(xd, chid, pid)
        try:
            js = json.loads(cdata)
        except:
            print(pid)
        chid_pid = []
        sort = 0
        for chapter in js:
            sort += 1
            rcode = chapter['id']
            cname = chapter['name']
            child = int(chapter['child'])
            level = int(chapter['depth']) - 2
            chid_pid.append(rcode)
            if child == 0:
                is_last = 1
            else:
                is_last = 0
            sql = 'insert into chapter2(subject_id,teachIngMaterial_id,grade_id,chapter_name,parent_id,level,is_last,sort,chapter_id) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            cursor.execute(sql, (0, 0, cid, cname, pid,
                                 level, is_last, sort, rcode))
            db.commit()
            print(cname)
        if len(chid_pid) > 0:
            getChapter(chid_pid,xd, chid, cid)
    db.close()


def workForGrade(data):
    db, cursor = getDBcon()
    for line in data:
        pids = [line[1]]
        cid = line[0]
        chid = line[2]
        xd = line[3]
        getChapter(pids, xd, chid, cid)
        sql = 'update msg set ok=1 where id=%s'
        cursor.execute(sql, cid)
        db.commit()
    db.close()


def work():
    db, cursor = getDBcon()
    sql = 'select id,spId,chid,xd from msg where ok=0 and (type=2 or type=3) '
    cursor.execute(sql)
    data = cursor.fetchall()
    dataLen = len(data)
    tnum = 5
    x = dataLen // tnum
    Thead = []
    for r in range(0, tnum):
        t = threading.Thread(target=workForGrade,
                             args=(data[r * x:r * x + x], ))
        Thead.append(t)
    t = threading.Thread(target=workForGrade, args=(data[x * tnum:dataLen], ))

    Thead.append(t)
    for t in Thead:
        t.start()

    for t in Thead:
        t.join()
    db.close()


if __name__ == '__main__':
    work()
