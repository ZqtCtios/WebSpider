# -*- coding: utf-8 -*-
# @Time    : 2019-09-02 10:31
# @Author  : ctios
# @Software: PyCharm
import time
import pymysql
import requests
import json
import threading
from bs4 import BeautifulSoup


def getAllData():
    db = pymysql.connect(
        "localhost",
        "root",
        "zqt1997",
        "hdkt_dev",
        use_unicode=True,
        charset="utf8")
    cursor = db.cursor()
    sql = 'select id,problemContentStr,problemAnswer from problem where ok=0'
    cursor.execute(sql)
    data = cursor.fetchall()
    db.close()
    return data


def download(url, filename):
    res = requests.get(url).content
    with open(filename, 'wb+') as f:
        f.write(res)


def work(data):
    db = pymysql.connect(
        "localhost",
        "root",
        "zqt1997",
        "hdkt_dev",
        use_unicode=True,
        charset="utf8")
    cursor = db.cursor()
    for line in data:
        pid = line[0]
        content = line[1]
        problemAnswer = line[2]
        if content.find('img') < 0 and problemAnswer.find('img') < 0:
            continue
        soup = BeautifulSoup(content, 'lxml')
        imgs = soup.find_all('img')
        sort = 0
        for img in imgs:
            try:
                sort += 1
                src = img['src']
                imgPath = 'problemContent/{}-{}.png'.format(pid, sort)
                download(src, imgPath)
                img['src'] = imgPath
            except BaseException:
                pass
        contentHtml = str(soup).replace(
            '<html><body><p>', '').replace(
            '</p></body></html>', '')
        soup = BeautifulSoup(problemAnswer, 'lxml')
        imgs = soup.find_all('img')
        sort = 0
        for img in imgs:
            try:
                sort += 1
                src = img['src']
                imgPath = 'problemContent/{}-option-{}.png'.format(pid, sort)
                download(src, imgPath)
                img['src'] = imgPath
            except BaseException:
                pass

        anserHtml = str(soup).replace(
            '<html><body><p>', '').replace(
            '</p></body></html>', '')
        sql = 'update problem set problemContentStr=%s,problemAnswer=%s,ok=1 where id=%s'
        print(pid)
        cursor.execute(sql, (contentHtml, anserHtml, pid))
        db.commit()
    db.close()


if __name__ == '__main__':
    while True:
        data = getAllData()
        work(data)
        if len(data) == 0:
            break
