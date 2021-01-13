import json
import time
import re
import threading
import requests
from bs4 import BeautifulSoup
import pymysql

db = pymysql.connect(
    "localhost", "root", "edu123456", "work", use_unicode=True, charset="utf8")
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
    'JSESSIONID=PhA2JYWs2Tz5nYjug9WOYZGy; screen_width_id=w1200; localAreaCode=58.; verifyCodePhone=13911635829; sso_login_flag=1; ut=2f5f4e9476b566f8bbff125e47c8b67817f3184b01312c711dfb0884fec184e423498ae702acc073; isPortal=1; phoneBuyAble=false; lastVisitTime=20171204143148; student_number=""; student_name=""; regFlg=0; username=360101100141720014; usertype=2; schoolStage="0001,0002,0003"; gradeCode=""; schoolId=36010110014172; defaultStage=0001; classId=""; studentId=""; schoolAreaCode=36.01.01; areacode=36.01.01; telNumber=13911635829',
    'Host':
    'plshdkt.jxrrt.cn',
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36',
    'X-Requested-With':
    'XMLHttpRequest'
}


def getPaperProblem(rcode):
    url = 'http://tqmshdkt.jxrrt.cn/tqms/interface/queryPaper.action?paper_id=%s' % (
        rcode)
    text = requests.get(url, headers=headers).text
    p = r'data-id="(.*?)"'
    res = re.findall(p, text)
    pids = []
    for x in res:
        pids.append(str(x))
    pids = set(pids)
    return pids


def getdata():
    sql = 'select id,rcode from paperOk where ok=0'
    cursor.execute(sql)
    data = cursor.fetchall()
    return data


def getPaperMsg(data):
    for line in data:
        paperId = line[0]
        rcode = line[1]
        pids = getPaperProblem(rcode)
        if len(pids) == 0:
            continue
        sql = 'select id from kp where pid like %s'
        for pid in pids:
            cursor.execute(sql, (pid))
            red = cursor.fetchall()
            if len(red) == 0:
                continue
            problemId = red[0][0]
            sql2 = 'insert into completePapper_problem(completePapperId,problemId) values(%s,%s)'
            cursor.execute(sql2, (paperId, problemId))
            db.commit()
        sql3 = 'update paperOk set ok=1 where id=%s' % (paperId)
        cursor.execute(sql3)
        db.commit()
        print(paperId)


def work():
    data = getdata()
    getPaperMsg(data)


if __name__ == '__main__':
    work()
