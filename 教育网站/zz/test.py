# -*- coding':'utf-8 -*-
# @Time    ':'2019-09-10 23:58
# @Author  ':'ctios
# @Software':'PyCharm
import requests
import json
import time
from bs4 import BeautifulSoup
headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Connection': 'keep-alive',
    'Cookie': 'screen_width_id=w1200; localAreaCode=1.; gjpt=zz; sso_login_flag=1; vut=ce88385a007dd9d7b3b26e35ef0cbdb5ffbd495885c4bfbbeae8d99e9f55b27316fff9933948c515; isPortal=1; returnSso=ssozz.zzedu.net.cn; ut=ce88385a007dd9d7b3b26e35ef0cbdb5ffbd495885c4bfbbeae8d99e9f55b273a300068bfe7757ff; phoneBuyAble=false; lastVisitTime=20190910171251; student_number=""; regFlg=0; username=4101016001170066; usertype=2; schoolStage=0001%2C0002%2C0003; schoolId=410101600117; defaultStage=0001; areacode=1.1.1; schoolAreaCode=1.1.1; JSESSIONID=NvMN7T1I8opa+JCt2sAPNPUj; __session:0.34460476379889093:=https:',
    'Host': 'plszz.zzedu.net.cn',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
}


def getFileList(classHourId, userName):
    t = int(time.time())
    url = 'https://plszz.zzedu.net.cn/prepare/queryClassHourPackByUserName.do?classHourId={}&userName={}&t={}&classHourIcon=1'.format(
        classHourId, userName, t)
    jsonText = requests.get(url, headers=headers).text
    # with open('x.json', 'w+') as f:
    #     f.write(jsonText)
    data = json.loads(jsonText)
    return data['linkedResList']


def downloadImg(rcode, userName):
    url = 'https://plszz.zzedu.net.cn/youjiao/doMutiplePlay.do?rcode={}&userName={}&filterType=0&allowPcMain=1'.format(
        rcode, userName)
    xmlData = requests.get(url, headers=headers).text
    soup = BeautifulSoup(xmlData, 'lxml')
    for fileTag in soup.find_all('file'):
        imgUrl = fileTag['path']
        fileName = fileTag['filepath'].replace('/', '')
        print(fileName)
        # content = requests.get(imgUrl, headers=headers).content
        # with open(fileName, 'wb+') as f:
        #     f.write(content)


def downloadFile(rcode, userName):
    t = int(time.time())
    url = 'https://plszz.zzedu.net.cn/youjiaoplay/getInfoJson.do?rcode={}&rsType=1&t={}'.format(
        rcode, t)
    jsonText = requests.get(url, headers=headers).text
    with open('x.json', 'w+') as f:
        f.write(jsonText)
    data = json.loads(jsonText)
    pid = data['pdfSID']
    RTitle = data['info']['RTitle']
    fileName = '{}.{}'.format(RTitle, 'pdf')
    print(fileName)
    fileUrl = 'https://plszz.zzedu.net.cn/servlet/DownloadFileServlet?pdfsid={}'.format(
        pid)
    content = requests.get(fileUrl, headers=headers).content
    with open(fileName, 'wb+') as f:
        f.write(content)


if __name__ == '__main__':
    classHourId = 20180716210528323609549241554
    userName = 4101016001170066
    data = getFileList(classHourId, userName)
    for line in data:
        title = line['destTitle']
        destCode = line['destCode']
        appTypeShowType = line['appTypeShowType']
        print(title, destCode, appTypeShowType)
        if appTypeShowType == 1:
            downloadImg(destCode, userName)
        else:
            downloadFile(destCode, userName)
