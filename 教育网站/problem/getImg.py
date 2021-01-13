import json
import os
import re
import threading
import time

import pymysql
import requests

#12.38
db = pymysql.connect(
    "localhost",
    "root",
    "edu123456",
    "hdkt_dev",
    use_unicode=True,
    charset="utf8")
cursor = db.cursor()


def getdata():
    sql = 'SELECT id,problemContent FROM problem4 where id in (select id from pp where ok=0)'
    cursor.execute(sql)
    data = cursor.fetchall()
    return data


def getImg(data):
    db_temp = pymysql.connect(
        "localhost",
        "root",
        "edu123456",
        "hdkt_dev",
        use_unicode=True,
        charset="utf8")
    cursor_temp = db_temp.cursor()
    for line in data:
        sid = line[0]
        qcontent = line[1]
        p = r'src="(/tqms/.*?)\.img"'
        for img in re.findall(p, qcontent):
            img = img + '.img'
            path = '/home/newdata' + img
            url = 'http://tqmshdkt.jxrrt.cn' + img
            content = requests.get(url).content
            f = open(path, 'wb+')
            f.write(content)
            f.close()
        sql = 'update pp set ok=1 where id=%s'
        cursor_temp.execute(sql, (sid))
        db_temp.commit()


def work():
    data = getdata()
    dataLen = len(data)
    print(dataLen)
    tnum = 10
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
