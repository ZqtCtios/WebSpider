import json
import os
import re
import time
import urllib
import requests
from bs4 import BeautifulSoup
import pymysql
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
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Connection': 'keep-alive',
    'Cookie': 'verifyCodePhone=13911635829; sso_login_flag=1; ut=5888a34dd2c756f86a79a20cf68fca3466d40a8a3a05d4ee185842d5c4f577e88a6a72b1c55c27fe; isPortal=1; phoneBuyAble=false; lastVisitTime=20171204143148; student_number=""; student_name=""; regFlg=0; username=360101100141720014; usertype=2; schoolStage="0001,0002,0003"; gradeCode=""; schoolId=36010110014172; defaultStage=0001; classId=""; studentId=""; schoolAreaCode=36.01.01; areacode=36.01.01; telNumber=13911635829; screen_width_id=w1200; localAreaCode=58.; JSESSIONID=pCoLLVJaUGMFWumzI4t2kmTb',
    'Host': 'plshdkt.jxrrt.cn',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
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


def work():
    dic = {'名师教案': '20170208134331825859395528865',
           '优教教案': '20170208134341549661661664663',
           '名师课件': '20170208134519779207253281283',
           '优教课件': '20170221145318849992935237657'}
    sql = 'select * from chapter where id >16357'
    cursor.execute(sql)
    ans = cursor.fetchall()
    sql2 = 'insert into source values(%s,%s,%s)'
    for line in ans:
        cid = line[0]
        code = line[4]
        for key in dic.keys():
            time.sleep(1)
            x = getKTJX(code, dic[key])
            cursor.execute(sql2, (x, cid, key))
            print(code, key)
            db.commit()
        time.sleep(1)
        x = sucai(code)
        cursor.execute(sql2, (x, cid, '素材'))
        db.commit()
        print(code, '素材')


if __name__ == '__main__':
    work()
