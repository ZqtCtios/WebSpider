import json
import time
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
    'JSESSIONID=65US1r3mnXaQtCm32xe3jYr2; screen_width_id=w1200; localAreaCode=58.; regFlg=0; username=360101100141720014; usertype=2; schoolStage="0001,0002,0003"; gradeCode=""; schoolId=36010110014172; defaultStage=0001; classId=""; studentId=""; schoolAreaCode=36.01.01; areacode=36.01.01; telNumber=13911635829; verifyCodePhone=13911635829; sso_login_flag=1; ut=8fa1b53ed9ead94b20354fb858edcfd8c693af3cda303643dfcf6374a02ef4b0aaae6ddd135bc7a2; isPortal=1; phoneBuyAble=false; lastVisitTime=20171204143148; student_number=""; student_name=""',
    'Host':
    'plshdkt.jxrrt.cn',
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36',
    'X-Requested-With':
    'XMLHttpRequest'
}
proxyHost = "http-pro.abuyun.com"
proxyPort = "9010"

#代理隧道验证信息
proxyUser = "HI3591I4LLO1GQ3P"
proxyPass = "F4E33B74B40A5995"

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


def getHomeWork(classId):
    url = 'http://tqmshdkt.jxrrt.cn/tqms/interface/homework/queryHomeworkByPaperType.action'
    data = {
        'username': '360101100141720014',
        'classId': classId,
        'studentClass': '',
        'paperType': '1',
        'start': '0',
        'limit': '1000',
        '_dc': int(time.time())
    }
    text = requests.get(
        url, headers=headers, params=data).text
    return text


def getdata():
    sql = 'SELECT id,classId FROM ctemp where ok=0'
    cursor.execute(sql)
    data = cursor.fetchall()
    return data


def getPaper(data):
    db_temp = pymysql.connect(
        "localhost",
        "root",
        "edu123456",
        "work",
        use_unicode=True,
        charset="utf8")
    cursor_temp = db_temp.cursor()
    for line in data:
        chapterId = line[0]
        classId = line[1]
        pdata = getHomeWork(classId)
        try:
            js = json.loads(pdata)
            js = js['items']
        except:
            continue
        for paper in js:
            rcode = paper['rcode']
            rtitle = paper['rtitle']
            hotDegree = paper['hotDegree']
            paperType = 2
            sql = 'insert into completePapper(chapterId,paperName,hotDegree,paperType,rcode) values(%s,%s,%s,%s,%s)'
            cursor_temp.execute(sql, (chapterId, rtitle, hotDegree,
                                      paperType, rcode))
            db_temp.commit()
        sql2 = 'update ctemp set ok=1 where id=%s' %(chapterId) 
        cursor_temp.execute(sql2)
        db_temp.commit()
        print(chapterId)
        time.sleep(1)


def work():
    data = getdata()
    getPaper(data)

if __name__ == '__main__':
    work()
