import json
import os
import threading
import time

import pymysql
import requests
from bs4 import BeautifulSoup

db = pymysql.connect(
    "localhost",
    "root",
    "edu123456",
    "hdkt_dev",
    use_unicode=True,
    charset="utf8")
cursor = db.cursor()
headers = {
    'Host':
    'www.zujuan.com',
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36',
    'X-Requested-With':
    'XMLHttpRequest'
}
request_data = [[2, 3, 4, 5, 9], [2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 11],
                [2, 3, 4, 6, 7, 8, 9, 10, 11]]
session = requests.Session()
url = 'http://www.zujuan.com/paper/new-index'
session.get(url, headers=headers)


def findjiaocai(str):
    x = int(str[1:])
    xd = x // 100 - 1
    ss = x % 100 - 1
    chid = request_data[xd][ss]
    return xd + 1, chid


def getPaper(res, gradeId):

    for line in res:
        nid = line[0]
        print(gradeId, nid)
        sql = 'update chapter2 set ok=1 where id=%s'
        cursor.execute(sql, (nid))
        db.commit()
        url = 'http://www.zujuan.com/paper/list/?tree_type=category&categories={}&_={}'.format(
            nid, int(time.time()))
        text = session.get(url).text
        if len(text) < 30:
            continue
        try:
            js = json.loads(text)['list']
            for line in js:
                title = line['title']
                viewUrl = line['viewUrl']
                viewUrl = 'http://www.zujuan.com' + viewUrl
                pid = line['pid']
                print(nid, pid, viewUrl, title)
                sql = 'insert into relation values(%s,%s,%s,%s)'
                cursor.execute(sql, (nid, pid, viewUrl, title))
                db.commit()
        except BaseException:
            continue


def getRelation(s):
    sql = 'select t.gradeId,t.teachIngMaterialId from (SELECT teachIngMaterialId,gradeId FROM chapter2 WHERE subjectId LIKE %s) as t group by t.gradeId '
    cursor.execute(sql, (s))
    data = cursor.fetchall()
    for line in data:
        gradeId = line[0]
        version = line[1]
        print(s, version, gradeId)
        url = 'http://www.zujuan.com/paper/new-index?bookversion={}&nianji={}'.format(
            version, gradeId)
        session.get(url)
        sql2 = 'select id from chapter2 where gradeId=%s'
        cursor.execute(sql2, (gradeId))
        res = cursor.fetchall()
        getPaper(res, gradeId)


def work():
    sql = 'SELECT subjectId FROM `chapter2` group by subjectId'
    cursor.execute(sql)
    data = cursor.fetchall()
    for line in data:
        s = line[0]
        xd, chid = findjiaocai(s)
        url = 'http://www.zujuan.com/paper/new-index?chid={}&xd={}&tree_type=category'.format(
            chid, xd)
        session.get(url)
        getRelation(s)


if __name__ == '__main__':
    work()
