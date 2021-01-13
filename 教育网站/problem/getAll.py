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
    "localhost",
    "root",
    "edu123456",
    "test",
    use_unicode=True,
    charset="utf8")
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
    'JSESSIONID=gRu87ghR3PIkGymRB1S4xkNg; screen_width_id=w1200; localAreaCode=58.; verifyCodePhone=13911635829; sso_login_flag=1; ut=8e38ac621ed53a53f49228f398bcda36e83f9f364c8ab574d7e9284b7e33ffc3ecd74e13ecd4fc0e; isPortal=1; phoneBuyAble=false; lastVisitTime=20171204143148; student_number=""; student_name=""; regFlg=0; username=360101100141720014; usertype=2; schoolStage="0001,0002,0003"; gradeCode=""; schoolId=36010110014172; defaultStage=0001; classId=""; studentId=""; schoolAreaCode=36.01.01; areacode=36.01.01; telNumber=13911635829',
    'Host':
    'plshdkt.jxrrt.cn',
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36',
    'X-Requested-With':
    'XMLHttpRequest'
}
proxyHost = "http-dyn.abuyun.com"
proxyPort = "9020"

# 代理隧道验证信息
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


def getKnowledge(cid, sid):
    url = 'http://tqmshdkt.jxrrt.cn/tqms/newhomework/topicstest/knowledge.action'
    data = {
        'questions.class_id': cid,
        'questions.qtype_id': '',
        'questions.difficulty': '',
        'questions.material_id': sid,
        'questions.Knowledge_id': '',
        'questions.from_platform': '2',
        '_dc': int(time.time())
    }
    text = requests.get(
        url, headers=headers, params=data).text
    return text


def getQuestion(cid, sid):
    url = 'http://tqmshdkt.jxrrt.cn/tqms/newhomework/topicstest/allQuestions.action'
    data = {
        'questions.class_id': cid,
        'questions.qtype_id': '',
        'questions.difficulty': '',
        'questions.material_id': sid,
        'questions.Knowledge_id': '',
        'questions.from_platform': '2',
        'start': '0',
        'limit': '1000',
        '_dc': int(time.time())
    }
    text = requests.get(
        url, headers=headers, params=data).text
    return text


def getdata():
    sql = 'select * from ctemp where ok=0'
    cursor.execute(sql)
    data = cursor.fetchall()
    return data



def getall(data):
    db_temp = pymysql.connect(
        "localhost",
        "root",
        "edu123456",
        "test",
        use_unicode=True,
        charset="utf8")
    cursor_temp = db_temp.cursor()
    for line in data:
        xid = line[0]
        pid = line[1]
        cid = line[2]
        qdata = getQuestion(cid, pid)
        if len(qdata) == 0:
            continue
        try:
            js = json.loads(qdata)
            js = js['items']
        except:
            print(qdata)
            continue
        for x in js:
            difficultyname = x['difficultyname']
            qid = x['id']
            print(qid)
            qcontent = x['qcontent']
            qtype_name = x['qtype_name']
            source = x['source']
            sql2 = 'insert into problemData2(chapterId,difficultyname,qid,qcontent,qtype_name,source) values(%s,%s,%s,%s,%s,%s)'
            cursor_temp.execute(sql2, (xid, difficultyname, qid,
                                       qcontent, qtype_name, source))

            db_temp.commit()
        sql2 = 'update ctemp set ok=1 where id=%s'
        cursor_temp.execute(sql2, (xid))
        db_temp.commit()

def work():
    data = getdata()
    dataLen = len(data)
    print(dataLen)
    tnum = 10
    x = dataLen // tnum
    Thead = []
    for r in range(0, tnum):
        t = threading.Thread(target=getall, args=(data[r * x:r * x + x], ))
        Thead.append(t)
    t = threading.Thread(target=getall, args=(data[x * tnum:dataLen], ))

    Thead.append(t)
    for t in Thead:
        t.start()

    for t in Thead:
        t.join()

    
if __name__ == '__main__':
    work()
    