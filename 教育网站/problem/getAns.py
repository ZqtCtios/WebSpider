import json
import os
import re
import time
import threading
import urllib
import requests
import demjson
from bs4 import BeautifulSoup
import pymysql
#12.38
db = pymysql.connect(
    "localhost", "root", "edu123456", "test", use_unicode=True, charset="utf8")
cursor = db.cursor()
headers = {
    'Accept':
    'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding':
    'gzip, deflate',
    'Accept-Language':
    'zh-CN,zh;q=0.8',
    'Connection':
    'keep-alive',
    'Cookie':
    'JSESSIONID=lM1KOmVYVMZg7O4KBTLSHwze; screen_width_id=w1200; localAreaCode=58.; regFlg=0; username=360101100141720014; usertype=2; schoolStage="0001,0002,0003"; gradeCode=""; schoolId=36010110014172; defaultStage=0001; classId=""; studentId=""; schoolAreaCode=36.01.01; areacode=36.01.01; telNumber=13911635829; verifyCodePhone=13911635829; sso_login_flag=1; ut=50a3fac5af3753869a094b3607985741195c0ba386a397260821f33077357e8f82f2dd428d7ece59; isPortal=1; phoneBuyAble=false; lastVisitTime=20171204143148; student_number=""; student_name=""',
    'Host':
    'plshdkt.jxrrt.cn',
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36',
    'X-Requested-With':
    'XMLHttpRequest'
}
proxyHost = "http-dyn.abuyun.com"
proxyPort = "9020"

#代理隧道验证信息
proxyUser = "HP07809N4O4MEA8D"
proxyPass = "49A1ECE7666C0CF0"

proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
    "host": proxyHost,
    "port": proxyPort,
    "user": proxyUser,
    "pass": proxyPass,
}

proxies = {
    "http": proxyMeta,
    "https": proxyMeta,
}


def getQuestionAns(pid):
    url = 'http://tqmshdkt.jxrrt.cn/tqms/newhomework/topicstest/viewQuestion.action'
    data = {'questions.id': pid, '_dc': int(time.time())}
    text = requests.get(
        url, headers=headers, params=data).text
    return text


def getdata():
    sql = 'SELECT pid FROM ans_ok where ok=0'
    cursor.execute(sql)
    data = cursor.fetchall()
    return data


def getans(data):
    db_temp = pymysql.connect(
        "localhost",
        "root",
        "edu123456",
        "test",
        use_unicode=True,
        charset="utf8")
    cursor_temp = db_temp.cursor()
    for line in data:
        pid = line[0]
        adata = getQuestionAns(pid)
        try:
            js = json.loads(adata)
        except:
            continue
        ans = js['answer']
        analysis = js['answer_analysis']
        sql = 'insert into ans values(%s,%s,%s)'
        cursor_temp.execute(sql, (pid, ans, analysis))
        db_temp.commit()
        sql = 'update ans_ok set ok=1 where pid=%s'
        cursor_temp.execute(sql, (pid))
        db_temp.commit()


def work():
    data = getdata()
    dataLen = len(data)
    print(dataLen)
    tnum = 20
    x = dataLen // tnum
    Thead = []
    for r in range(0, tnum):
        t = threading.Thread(target=getans, args=(data[r * x:r * x + x], ))
        Thead.append(t)
    t = threading.Thread(target=getans, args=(data[x * tnum:dataLen], ))

    Thead.append(t)
    for t in Thead:
        t.start()

    for t in Thead:
        t.join()


if __name__ == '__main__':
    work()
