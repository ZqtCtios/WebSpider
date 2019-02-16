import json
import os
import re
import time
import urllib
import requests
from bs4 import BeautifulSoup
import pymysql
import threading
# 12.38
db = pymysql.connect(
    "localhost",
    "root",
    "Zqt_1997",
    "hdkt_dev",
    use_unicode=True,
    charset="utf8")
cursor = db.cursor()
headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Cookie': 'verifyCodePhone=13911635829; sso_login_flag=1; ut=69942e6d5236ff623401ca068f8b129c553eb65917337bea3f699e8d716fdb4d897b23f8d115f635; isPortal=1; phoneBuyAble=false; lastVisitTime=20171204143148; student_number=""; student_name=""; regFlg=0; username=360101100141720014; usertype=2; schoolStage="0001,0002,0003"; gradeCode=""; schoolId=36010110014172; defaultStage=0001; classId=""; studentId=""; schoolAreaCode=36.01.01; areacode=36.01.01; telNumber=13911635829; screen_width_id=w1200; localAreaCode=58.; JSESSIONID=p3pCICxOA8aW7nlIX3YhGcqG',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}
# 代理服务器
proxyHost = "http-dyn.abuyun.com"
proxyPort = "9020"

# 代理隧道验证信息
proxyUser = "HO2R82620331664D"
proxyPass = "3EE5F896C43DFAF0"

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


def getKTJX(code, commonTypeId):
    url = 'http://plshdkt.jxrrt.cn/prepare/queryPreResInfo.do'
    data = {
        'menuCode': code,
        'page': '1',
        'pageNum': '10',
        'listType': '2',
        'userName': '360101100141720014',
        'commonTypeId': commonTypeId,
        'commonType': '1',
        'yun': '1',
        'resComeType': '1',
        't': int(time.time()),
        'orderby': '6'}

    text = requests.get(
        url,
        headers=headers,
        params=data,
        proxies=proxies).text
    return text


def getJASJ(code, commonTypeId):
    url = 'http://plshdkt.jxrrt.cn/prepare/queryPreResInfo.do'
    data = {
        'menuCode': code,
        'page': '1',
        'pageNum': '10',
        'listType': '2',
        'userName': '360101100141720014',
        'commonTypeId': commonTypeId,
        'commonType': '2',
        'resComeType': '2',
        'yun': '1',
        't': int(time.time()),
        'orderby': '6'}
    text = requests.get(
        url,
        headers=headers,
        params=data,
        proxies=proxies).text
    return text


def sucai(code):
    url = 'http://plshdkt.jxrrt.cn/prepare/queryPreResInfo.do'
    data = {
        'menuCode': code,
        'page': '1',
        'pageNum': '10',
        'listType': '2',
        'userName': '360101100141720014',
        'typeCode': 'RT002,RT004',
        'yun': '1',
        'resComeType': '3',
        't': int(time.time()),
        'orderby': '6'}
    text = requests.get(
        url,
        headers=headers,
        params=data,
        proxies=proxies).text
    return text


def work2():
    dic = {'名师教案': '20170208134331825859395528865',
           '优教教案': '20170208134341549661661664663',
           '名师课件': '20170208134519779207253281283',
           '优教课件': '20170221145318849992935237657'}
    # sql = 'select * from chapter where id >4196'
    # cursor.execute(sql)
    # ans = cursor.fetchall()
    # sql2 = 'insert into source values(%s,%s,%s)'
    # for line in ans:
    #     cid = line[0]
    #     code = line[4]
    #     for key in dic.keys():
    #         time.sleep(2)
    #         x = getKTJX(code, dic[key])
    #         cursor.execute(sql2, (x, cid, key))
    #         print(code, key)
    #         db.commit()
    #     time.sleep(2)
    #     x = sucai(code)
    #     cursor.execute(sql2, (x, cid, '素材'))
    #     db.commit()
    #     print(code, '素材')
    sql = 'select * from source where cid>9'
    cursor.execute(sql)
    ans = cursor.fetchall()
    for line in ans:
        cid = line[1]
        ctype = line[2]
        code = line[3]
        sql = 'update source set content=%s where cid=%s and type=%s'
        if str(ctype) == '名师教案':
            typeid = dic['名师教案']
            x = getJASJ(code, typeid)
            print(x, cid, ctype)
            cursor.execute(sql, (x, cid, ctype))
            db.commit()
        if str(ctype) == '优教教案':
            typeid = dic['优教教案']
            x = getJASJ(code, typeid)
            cursor.execute(sql, (x, cid, ctype))
            print(x, cid, ctype)
            db.commit()


def msja(data):
    dic = ['名师教案', '优教教案', '名师课件', '优教课件', '素材']
    db_temp = pymysql.connect(
        "localhost",
        "root",
        "Zqt_1997",
        "hdkt_dev",
        use_unicode=True,
        charset="utf8")
    cursor_temp = db_temp.cursor()
    for x in data:
        cid = x[0]
        code = x[1]
        for typeid in dic:
            sql = 'select * from source where code like %s and type like %s'
            cursor_temp.execute(sql, (code, typeid))
            ans = cursor_temp.fetchall()
            if len(ans) > 0:
                print(cid, code, 'ok')
            else:
                print(cid, code, 'insert')
                sql = 'insert into source values(%s,%s,%s,%s)'
                cursor_temp.execute(sql, ("", cid, typeid, code))
                db_temp.commit()


def work():

    sql = 'select * from source where length(content)<10'
    cursor.execute(sql)
    data = cursor.fetchall()
    dataLen = len(data)
    x = dataLen // 10
    Thead = []
    for r in range(0, 10):
        t = threading.Thread(target=getsource, args=(data[r * x:r * x + x],))
        Thead.append(t)
    t = threading.Thread(target=getsource, args=(data[x * 10:dataLen],))

    Thead.append(t)
    for t in Thead:
        t.start()

    for t in Thead:
        t.join()


def getsource(data):
    db_temp = pymysql.connect(
        "localhost",
        "root",
        "Zqt_1997",
        "hdkt_dev",
        use_unicode=True,
        charset="utf8")
    cursor_temp = db_temp.cursor()
    dic = {'名师教案': '20170208134331825859395528865',
           '优教教案': '20170208134341549661661664663',
           '名师课件': '20170208134519779207253281283',
           '优教课件': '20170221145318849992935237657'}

    sql2='update source set content=%s where id=%s'
    for line in data:
        cid = line[0]
        typeid = line[3]
        code = line[4]
        print(line)
        if typeid=='素材':
            x = sucai(code)
        elif typeid == '名师教案':
            x = getJASJ(code, dic[typeid])
        elif typeid == '优教教案':
            x = getJASJ(code, dic[typeid])   
        else:
            x = getKTJX(code, dic[typeid])
        cursor_temp.execute(sql2,(x,cid))
        db_temp.commit()
        


if __name__ == '__main__':
    work()
