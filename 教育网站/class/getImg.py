# -*- coding: utf-8 -*-
import json
import time
import threading
import requests
from lxml import etree
import pymysql

db = pymysql.connect(
    "localhost", "root", "edu123456", "work2", use_unicode=True, charset="utf8")
cursor = db.cursor()

def getdata():
    sql = 'SELECT id,courseId FROM course_data2 where ok=0'
    cursor.execute(sql)
    data = cursor.fetchall()
    return data
def getMsg(cid):
    print('http://www.class.cn/course/course_detail/?course_id=%s'%(cid))
    session = requests.Session()
    req=session.get('http://www.class.cn/course/course_detail/?course_id=%s'%(cid))
    req.encoding = 'utf8'
    html = etree.HTML(req.text)
    try:
        x=html.xpath('//*[@id="course_right"]/div[1]/div/p[2]')[0]
        aims=etree.tostring(x,encoding='utf-8',pretty_print=True,method='html')
    except:
        aims=""
    try:
        time=html.xpath('//*[@id="course_right"]/div[1]/div/h2/span/text()')
    except:
        time=""
    try:
        instructions=html.xpath('//*[@id="course_left"]/div[1]/div/section/p')[0]
        instructions=etree.tostring(instructions,encoding='utf-8',pretty_print=True,method='html')
    except:
        instructions=''
    return time,aims,instructions

def getImg(data):
    db_temp = pymysql.connect(
        "localhost",
        "root",
        "edu123456",
        "work2",
        use_unicode=True,
        charset="utf8")
    cursor_temp = db_temp.cursor()
    for line in data:
        id=line[0]
        cid=line[1]
        time,aims,instructions=getMsg(cid)
        sql='update course_data2 set time=%s,aims=%s,instructions=%s,ok=1 where id=%s'
        cursor_temp.execute(sql,(time,aims,instructions,id))
        db_temp.commit()


def work():
    data=getdata()
    dataLen=len(data)
    tnum = 25
    x = dataLen // tnum
    Thead = []
    for r in range(0, tnum):
        t = threading.Thread(target=getImg, args=(data[r * x:r * x + x], ))
        Thead.append(t)
    t = threading.Thread(target=getImg, args=(data[x * tnum:dataLen], ))

    Thead.append(t)
    for t in Thead:
        t.start()

    for t in Thead:
        t.join()


if __name__ == '__main__':
    work()
