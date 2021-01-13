import os
import threading
import urllib
import mkdp
import time
import datetime
import pymysql
import requests
from bs4 import BeautifulSoup

# 12.38
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
    'application/xml, text/xml, */*; q=0.01',
    'Accept-Encoding':
    'gzip, deflate',
    'Accept-Language':
    'zh-CN,zh;q=0.8',
    'Connection':
    'keep-alive',
    'Cookie':
    'verifyCodePhone=13911635829; sso_login_flag=1; ut=2026c482a64c9c3965964f42eb46675ef9ec358a635d9503d93c2da132f42a7fd4f2a5040675cbac; isPortal=1; phoneBuyAble=false; lastVisitTime=20171204143148; student_number=""; student_name=""; regFlg=0; username=360101100141720014; usertype=2; schoolStage="0001,0002,0003"; gradeCode=""; schoolId=36010110014172; defaultStage=0001; classId=""; studentId=""; schoolAreaCode=36.01.01; areacode=36.01.01; telNumber=13911635829; screen_width_id=w1200; localAreaCode=58.; JSESSIONID=nuXwLjMNJBtEQHeyvbN5Mi7k; __session:0.6501248349868358:=http:',
    'Host':
    'plshdkt.jxrrt.cn',
    'User-Agent':
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
    'X-Requested-With':
    'XMLHttpRequest'
}
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


def downData(data):
    db_temp = pymysql.connect(
        "localhost",
        "root",
        "edu123456",
        "hdkt_dev",
        use_unicode=True,
        charset="utf8")
    cursor_temp = db_temp.cursor()
    sql = 'UPDATE down2 SET ok=1 WHERE id=%s'
    for x in data:
        # if timeover():
        #     return
        cid = x[0]
        fp = x[1]
        rcode = x[2]
        try:
            if download(fp, rcode):
                cursor_temp.execute(sql, (cid))
                db_temp.commit()    
        except:
            pass
        
    cursor.close()
    db_temp.close()


def download(path, rcode):
    home = '/home/data/'
    url = 'http://plshdkt.jxrrt.cn/youjiao2/doMutiplePlay.do'
    data = {
        'rcode': rcode,
        'userName': '360101100141720014',
        'filterType': '1',
        'ct': '0'
    }
    text = requests.get(
        url, headers=headers, params=data, proxies=proxies).text
    soup = BeautifulSoup(text, 'html.parser')
    x = soup.find('file')
    downUrl = x['path']
    filepath = home + path
    filepath = filepath.replace(' ', '')
    print(downUrl, filepath)
    # urllib.request.urlretrieve(downUrl, filepath)
    r = requests.get(downUrl, proxies=proxies).content
    with open(filepath, 'wb') as f:
        f.write(r)
    size = os.path.getsize(filepath)
    print(path, size)
    if size < 1024:
        return False
    if os.path.exists(filepath):
        print('下载成功:', path)
        return True
    else:
        return False


def getdata():
    sql = 'SELECT id,url,rcode FROM document WHERE ok=0 '
    cursor.execute(sql)
    data = cursor.fetchall()
    return data


def work():
    data = getdata()
    dataLen = len(data)
    tnum = 5
    x = dataLen // tnum
    Thead = []
    for r in range(0, tnum):
        t = threading.Thread(target=downData, args=(data[r * x:r * x + x], ))
        Thead.append(t)
    t = threading.Thread(target=downData, args=(data[x * tnum:dataLen], ))

    Thead.append(t)
    for t in Thead:
        t.start()

    for t in Thead:
        t.join()


# def oktime():
#     a = time.localtime()
#     h = int(time.strftime("%H", a))
#     w = int(time.strftime("%w", a))
#     if w==0 or w==6:
#         return True
#     if h >= 18:
#         return True
#     return False

# def passtime():
#     url = 'http://plshdkt.jxrrt.cn/youjiao/baceContent.do?section=0001&grade=0005&volume=0002&subject=0007&versions=0001&listType=1'
#     x = requests.get(url, headers=headers, proxies=proxies)
#     time.sleep(20)
#     print('passtime')

# def timeover():
#     a = time.localtime()
#     w = int(time.strftime("%w", a))
#     h = int(time.strftime("%H", a))
#     if w in range(1, 6):
#         if h >= 8 and h < 18:
#             return True
#     return False

if __name__ == '__main__':
    # while True:
    #     if oktime():
    #         work()
    #     else:
    #         passtime()
    work()