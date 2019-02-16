import os
import threading
import urllib
import mkdp
import pymysql
import requests
from bs4 import BeautifulSoup

# 12.38
db = pymysql.connect(
    "localhost",
    "root",
    "zqt1997",
    "hdkt_dev",
    use_unicode=True,
    charset="utf8")
cursor = db.cursor()


def getdata():
    sql = 'SELECT id,fp FROM down'
    cursor.execute(sql)
    data = cursor.fetchall()
    return data


def find(data):
    print('working......')
    db_temp = pymysql.connect(
        "localhost",
        "root",
        "zqt1997",
        "hdkt_dev",
        use_unicode=True,
        charset="utf8")
    cursor_temp = db_temp.cursor()
    home = '/home/data2/'
    sql = 'update document set url=%s where id=%s;'
    i=0
    for x in data:
        cid = x[0]
        fp = x[1]
        cursor_temp.execute(sql, (fp,cid))
        db_temp.commit()
    cursor.close()
    db_temp.close()
def work():
    data = getdata()
    dataLen = len(data)
    x = dataLen // 25
    Thead = []
    for r in range(0, 25):
        t = threading.Thread(target=find, args=(data[r * x:r * x + x], ))
        Thead.append(t)
    t = threading.Thread(target=find, args=(data[x * 25:dataLen], ))

    Thead.append(t)
    for t in Thead:
        t.start()

    for t in Thead:
        t.join()

if __name__ == '__main__':
    work()