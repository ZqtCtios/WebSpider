import json
import os
import re
import time
import urllib
import requests
from bs4 import BeautifulSoup
import pymysql
#12.38
db = pymysql.connect(
    "localhost",
    "root",
    "Zqt_1997",
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
    'verifyCodePhone=13911635829; sso_login_flag=1; ut=40b04e0431f386c5a2047842a1f7e20cd915556dca5543bc956ea5b4ce25b69fd3171f95ab22fdfe; isPortal=1; phoneBuyAble=false; lastVisitTime=20171204143148; student_number=""; student_name=""; regFlg=0; username=360101100141720014; usertype=2; schoolStage="0001,0002,0003"; gradeCode=""; schoolId=36010110014172; defaultStage=0001; classId=""; studentId=""; schoolAreaCode=36.01.01; areacode=36.01.01; telNumber=13911635829; screen_width_id=w1200; localAreaCode=58.; JSESSIONID=NhkUDat-cnp2QeUwpyIbvcZE',
    'Host':
    'plshdkt.jxrrt.cn',
    'User-Agent':
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
    'X-Requested-With':
    'XMLHttpRequest'
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

# def getListData(section,grade,volume,subject,versions):


def getListData(section, grade, volume, subject, versions):
    url = 'http://plshdkt.jxrrt.cn/youjiao/baceContent.do'
    data = {
        'section': section,
        'grade': grade,
        'volume': volume,
        'subject': subject,
        'versions': versions,
        'listType': '1'
    }

    text = requests.get(
        url, headers=headers, params=data, proxies=proxies).text
    time.sleep(5)
    return text


def getFormatStr(s):
    s = str(s)
    for i in range(4 - len(s)):
        s = '0' + s
    return s


def kemu():
    sql = 'INSERT INTO test VALUES(%s,%s,%s,%s,%s,%s)'
    i = 0
    versions = [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 51, 52, 53, 54, 55, 56, 57, 58, 59, 51, 102,
        103, 104, 105, 106, 107, 108, 109
    ]
    for grade in range(1, 10):
        for subject in range(1, 17):
            for section in range(1, 3):
                for volume in range(1, 3):
                    for version in versions:
                        i += 1
                        section = getFormatStr(section)
                        grade = getFormatStr(grade)
                        volume = getFormatStr(volume)
                        subject = getFormatStr(subject)
                        version = getFormatStr(version)
                        print(section, grade, volume, subject, version)
                        x = getListData(section, grade, volume, subject,
                                        version)
                        cursor.execute(sql, (x, section, grade, volume,
                                             subject, version))
                        db.commit()
    print(i)


def mkDir(listData):
    now = '.'
    for x in listData:
        code = x['code']
        name = x['name']
        if int(x['endflag']) == 0:
            continue

        if int(x['isUnit']) == 1:
            now = './' + name
            os.mkdir(now)
            print('创建目录：', now)
        else:
            temp = now + '/' + name
            os.mkdir(temp)
            print('创建目录：', temp)


def findResource(listData):
    now = '.'
    for x in listData:
        code = x['code']
        name = x['name']
        if int(x['endflag']) == 0:
            continue

        if int(x['isUnit']) == 1:
            now = './' + name
            path = now
        else:
            temp = now + '/' + name
            path = temp
        getJASJ(path, code)
        getKTJX(path, code)


def getJASJ(path, code):
    try:
        path = path + '/教案设计'
        os.mkdir(path)
        url = 'http://plshdkt.jxrrt.cn/prepare/queryPreResInfo.do'
        data = {
            'menuCode': code,
            'page': '1',
            'pageNum': '10',
            'listType': '2',
            'userName': '360101100141720014',
            'commonTypeId': '20170208134331825859395528865',
            'commonType': '2',
            'resComeType': '2',
            'yun': '1',
            't': int(time.time()),
            'orderby': '6'
        }
        text = requests.get(url, headers=headers, params=data).text
        js = json.loads(text)
        title = js['ResInfo'][0]['RTitle']
        rcode = js['ResInfo'][0]['RCode']
        print(title, rcode)
        download(path, rcode)
    except BaseException:
        pass


def getKTJX(path, code):
    try:
        path = path + '/课堂教学'
        os.mkdir(path)
        url = 'http://plshdkt.jxrrt.cn/prepare/queryPreResInfo.do'
        data = {
            'menuCode': '00010b02020404',
            'page': '1',
            'pageNum': '10',
            'listType': '2',
            'userName': '360101100141720014',
            'commonTypeId': '20170208134519779207253281283',
            'commonType': '1',
            'yun': '1',
            'resComeType': '1',
            't': '1514008909938',
            'orderby': '6'
        }

        text = requests.get(url, headers=headers, params=data).text
        js = json.loads(text)
        title = js['ResInfo'][0]['RTitle']
        rcode = js['ResInfo'][0]['RCode']
        download(path, rcode)
    except BaseException:
        pass


def download(path, rcode):
    url = 'http://plshdkt.jxrrt.cn/youjiao2/doMutiplePlay.do'
    data = {
        'rcode': rcode,
        'userName': '360101100141720014',
        'filterType': '1',
        'ct': '0'
    }
    text = requests.get(url, headers=headers, params=data).text
    soup = BeautifulSoup(text, 'lxml')
    ans = soup.find_all('file')
    for x in ans:
        downUrl = x['path']
        filepath = path + x['filepath']
        print('正在下载', filepath)
        urllib.request.urlretrieve(downUrl, filepath)
        print('down')


def jiaocai():
    sql = 'SELECT * FROM jiaocai WHERE id<264'
    sql2 = 'update jiaocai set content=%s where id=%s'
    cursor.execute(sql)
    ans = cursor.fetchall()
    for line in ans:
        section = line[2]
        grade = line[3]
        volume = line[4]
        subject = line[5]
        version = line[6]
        print(section, grade, volume, subject, version)
        x = getListData(section, grade, volume, subject, version)
        cursor.execute(sql2, (x, line[0]))
        db.commit()


def getGaozhong():
    sql = 'insert into test2 values(%s,%s,%s,%s,%s)'
    section = '0003'
    i = 0
    for subject in range(14, 17):
        for versions in range(30):
            for rxiu in range(30):
                subject = getFormatStr(subject)
                versions = getFormatStr(versions)
                rxiu = 'x' + getFormatStr(rxiu)
                i += 1
                print(section, subject, versions, rxiu)
                x = getGjson(section, subject, versions, rxiu)
                cursor.execute(sql, (x, section, subject, versions, rxiu))
                db.commit()
    print(i)


def getGjson(section, subject, versions, rxiu):
    url = 'http://plshdkt.jxrrt.cn/youjiao/baceContent.do'
    data = {
        'section': section,
        'subject': subject,
        'versions': versions,
        'rxiu': rxiu,
        'listType': '1'
    }
    text = requests.get(
        url, headers=headers, params=data, proxies=proxies).text
    time.sleep(5)
    return text


if __name__ == '__main__':
    #listData = getListData()
    # print(listData)
    #kemu()
    #jiaocai()
    getGaozhong()
    # mkDir(listData)
    # findResource(listData)
