#!/usr/bin/python

import pymysql
import re
import requests

# 这个文件是获取所有教材


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


def getHtml(chid, xd):
    url = 'https://www.21cnjy.com/soft.php?mod=list&chid=%s&xd=%d' % (chid, xd)
    html = requests.get(url).text
    return html



def getTM():
    # 获取教材信息
    db, cursor = getDBcon()
    cursor.execute('select * from msg where id>31')
    data=cursor.fetchall()
    for line in data:
        sid=line[0]
        xd=line[1]
        chid=line[3]
        html=getHtml(chid,xd)
        html = html.replace('\n', '').replace(' ', '')
        p=r'data-vid=\"(.*?)\">(.*?)</a>'
        res=re.findall(p,html)
        for x in res:
            catId=int(x[0])
            tmName=x[1]
            cursor.execute('insert into teachingmaterial values (%s,%s,%s,%s,%s)',(sid,tmName,catId,xd,chid))
            db.commit()
            print(catId,tmName)


def getSpTM():
    pass
if __name__ == '__main__':
    getSpTM()
    
