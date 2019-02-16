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
    "hdkt_dev",
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
    'JSESSIONID=HWE7f-wyev4vkdVOsSby4gqx; screen_width_id=w1200; localAreaCode=58.; regFlg=0; username=360101100141720014; usertype=2; schoolStage="0001,0002,0003"; gradeCode=""; schoolId=36010110014172; defaultStage=0001; classId=""; studentId=""; schoolAreaCode=36.01.01; areacode=36.01.01; telNumber=13911635829; verifyCodePhone=13911635829; sso_login_flag=1; ut=3269c89e72fc8efd09930f8d3eceb52c76a33bc692e9de63d0e95cfbd7af904de567a391d2d2d25a; isPortal=1; phoneBuyAble=false; lastVisitTime=20171204143148; student_number=""; student_name=""',
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
        url, headers=headers, params=data, proxies=proxies).text
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
        url, headers=headers, params=data, proxies=proxies).text
    return text


def getps(data):
    db_temp = pymysql.connect(
        "localhost",
        "root",
        "edu123456",
        "hdkt_dev",
        use_unicode=True,
        charset="utf8")
    cursor_temp = db_temp.cursor()
    sql = 'update temp3 set qdata=%s,ok=1 where id=%s'
    for line in data:
        xid = line[0]
        pid = line[1]
        cid = line[2]
        # try:
        #     kdata = getKnowledge(cid, pid)
        #     qdata = getQuestion(cid, pid)
        #     print(xid, pid, cid)
        #     print(kdata)
        #     print(qdata)
        #     cursor_temp.execute(sql, (kdata, qdata, xid))
        #     db_temp.commit()
        # except:
        #     sql2 = 'update temp set ok=0 where id=%s'
        #     cursor_temp.execute(sql2, (xid))
        #     db_temp.commit()
        qdata = getQuestion(cid, pid)
        print(xid, pid, cid)
        cursor_temp.execute(sql, (qdata, xid))
        db_temp.commit()


def getdata():
    sql = 'SELECT id,pid,cid FROM temp2 where ok=0'
    cursor.execute(sql)
    data = cursor.fetchall()
    return data


def work():
    data = getdata()
    dataLen = len(data)
    print(dataLen)
    tnum = 3
    x = dataLen // tnum
    Thead = []
    for r in range(0, tnum):
        t = threading.Thread(target=work3, args=(data[r * x:r * x + x], ))
        Thead.append(t)
    t = threading.Thread(target=work3, args=(data[x * tnum:dataLen], ))

    Thead.append(t)
    for t in Thead:
        t.start()

    for t in Thead:
        t.join()
 


def getall(start):
    print("start:",start)
    db_temp = pymysql.connect(
        "localhost",
        "root",
        "edu123456",
        "hdkt_dev",
        use_unicode=True,
        charset="utf8")
    cursor_temp = db_temp.cursor()
    sql = 'select id,kdata from temp where id>=%s and id<%s'
    cursor_temp.execute(sql,(start,start+2000))
    data=cursor_temp.fetchall()
    for line in data:
        xid = line[0]
        kdata = line[1]
        print(xid)
        try:
            js=json.loads(kdata)
        except:
            continue
        for x in js:
            kid=x['id']
            name=x['name']
            sql2='insert into knowledge values(%s,%s,%s)'
            cursor_temp.execute(sql2,(xid,kid,name))
            db_temp.commit()
            sql2 = 'update tempk set ok=3 where id=%s'
            cursor_temp.execute(sql2, (xid))
            db_temp.commit()

def getall2(start):
    print("start:", start)
    db_temp = pymysql.connect(
        "localhost",
        "root",
        "edu123456",
        "hdkt_dev",
        use_unicode=True,
        charset="utf8")
    cursor_temp = db_temp.cursor()
    sql = 'select id,qdata from temp3 where ok=1 and id>=%s and id<%s'
    cursor_temp.execute(sql, (start,start+2000))
    data = cursor_temp.fetchall()
    for line in data:
        xid = line[0]
        qdata = line[1]

        if len(qdata)==0:
            continue
        print(xid)

        try:
            js = json.loads(qdata)
            js = js['items']
        except:
            print(qdata)
            continue
        # js = json.loads(qdata)
        # js = js['items']
        for x in js:
            difficulty = x['difficulty']
            difficultyname = x['difficultyname']
            grade_name = x['grade_name']
            sid = x['id']
            knowledge_content = x['knowledge_content']
            qcontent = x['qcontent']
            qcontent_main = x['qcontent_main']
            qtype_name = x['qtype_name']
            questionsList = x['questionsList']
            quote_num = x['quote_num']
            sbj_name = x['sbj_name']
            scores = x['scores']
            source = 0
            video_analysis = x['video_analysis']
            sql2 = 'insert into problemData values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            cursor_temp.execute(
                sql2, (xid, difficulty, difficultyname, grade_name, sid,
                       knowledge_content, qcontent, qcontent_main, qtype_name,
                       questionsList, quote_num, sbj_name, scores, source,
                       video_analysis))
            
            db_temp.commit()
        sql2 = 'update temp3 set ok=3 where id=%s'
        cursor_temp.execute(sql2, (xid))
        db_temp.commit()  

def work3(data):
    db_temp = pymysql.connect(
        "localhost",
        "root",
        "edu123456",
        "hdkt_dev",
        use_unicode=True,
        charset="utf8")
    cursor_temp = db_temp.cursor()
    for line in data:
        xid = line[0]
        pid = line[1]
        cid = line[2]
        qdata = getQuestion(cid, pid)
        if len(qdata)==0:
            continue
        print(xid)
        try:
            js = json.loads(qdata)
            js = js['items']
        except:
            print(qdata)
            continue
        for x in js:
            difficulty = x['difficulty']
            difficultyname = x['difficultyname']
            grade_name = x['grade_name']
            sid = x['id']
            knowledge_content = x['knowledge_content']
            qcontent = x['qcontent']
            qcontent_main = x['qcontent_main']
            qtype_name = x['qtype_name']
            questionsList = x['questionsList']
            quote_num = x['quote_num']
            sbj_name = x['sbj_name']
            scores = x['scores']
            source = 0
            video_analysis = x['video_analysis']
            sql2 = 'insert into problemData values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            cursor_temp.execute(
                sql2, (xid, difficulty, difficultyname, grade_name, sid,
                       knowledge_content, qcontent, qcontent_main, qtype_name,
                       questionsList, quote_num, sbj_name, scores, source,
                       video_analysis))
            
            db_temp.commit()
        sql2 = 'update temp2 set ok=3 where id=%s'
        cursor_temp.execute(sql2, (xid))
        db_temp.commit()  

def work2():
    start = 19723
    tnum = 10
    x = 2000
    Thead = []
    for r in range(0, tnum):
        t = threading.Thread(target=getall, args=(x * r + start, ))
        Thead.append(t)

    for t in Thead:
        t.start()

    for t in Thead:
        t.join()


if __name__ == '__main__':
    # start = 19723
    # for i in range(0,20):
    #     getall2(start+i*1000)
    work()