#!/usr/bin/python
from bs4 import BeautifulSoup
import pymysql
import requests
import json
import threading
import re


def getDBcon():
    db = pymysql.connect(
        "localhost",
        "root",
        "zqt1997",
        "21cnjy",
        use_unicode=True,
        charset="utf8")
    cursor = db.cursor()
    return db, cursor


def work():
    db, cursor = getDBcon()
    cursor.execute('select id,spId,xd,xueduan from msg2')
    data = cursor.fetchall()
    ok=[]
    for line in data:
        gradeId = line[0]
        spId = line[1]
        xd = line[2]
        xueduan = line[3]
        if xueduan in ok:
            continue
        #url = 'https://www.21cnjy.com/{}/{}/'.format(xd, spId)
        url='https://www.21cnjy.com/2/49247/'
        text = requests.get(url).text
        text = text.replace('\n', '').replace(' ', '')
        p = r'data-param="bookversion=(.*?)">(.*?)</a>'
        res = re.findall(p, text)
        if len(res)==0:
            continue
        ok.append(xueduan)
        print(xueduan)
        for x in res:
            cursor.execute('insert into SpeTm(gradeId,bookversion,name,xueduan) values (%s,%s,%s,%s)',(gradeId,x[0],x[1],xueduan))
            print(x)
        db.commit()
        input()
    db.close()
    print(len(ok))

if __name__ == '__main__':
    work()
    