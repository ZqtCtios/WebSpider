# -*- coding: utf-8 -*-
# @Time    : 2019-09-12 15:20
# @Author  : ctios
# @Software: PyCharm
import requests
import pymysql
import json
import time
from bs4 import BeautifulSoup
import os
headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Connection': 'keep-alive',
    'Cookie': 'gjpt=zz; screen_width_id=w1200; localAreaCode=1.; sso_login_flag=1; vut=c3d478520a7a4649df374ac1c7aa5cd9a132a2c97029bc8507431a0cf112ea9b7d4c2d1e70453ad7; isPortal=1; returnSso=ssozz.zzedu.net.cn; ut=c3d478520a7a4649df374ac1c7aa5cd9a132a2c97029bc8507431a0cf112ea9ba18ac1dca490bb20; phoneBuyAble=false; lastVisitTime=20190916145910; student_number=""; regFlg=0; username=4101016001170066; usertype=2; schoolStage=0001%2C0002%2C0003; schoolId=410101600117; defaultStage=0001; areacode=1.1.1; schoolAreaCode=1.1.1; JSESSIONID=1vItmFuTqHWJyhrgA0bzXw1E',
    'Host': 'plszz.zzedu.net.cn',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
}


def getDB():
    db = pymysql.connect(
        "localhost",
        "root",
        "zqt1997",
        "data",
        use_unicode=True,
        charset="utf8")
    cursor = db.cursor()
    return db, cursor


def getChapterDocs(versionID):
    db, cursor = getDB()
    sql = 'select id,vc_chapterId,subjectId from chapter where parentId<>0 and versionid=%s and ok=0'
    cursor.execute(sql, (versionID))
    data = cursor.fetchall()
    path = 'files'
    for line in data:
        try:
            lid = line[0]
            cid = line[1]
            print(cid)
            subjectId = line[2]
            url = 'https://plszz.zzedu.net.cn/prepare/queryClassHourPackByUserName.do?classHourId={}&userName=4101016001170066&classHourIcon=1'.format(
                cid)
            jsonText = requests.get(url, headers=headers).text
            jsonData = json.loads(jsonText)['linkedResList']
            for doc in jsonData:
                did = doc['id']
                ok = 1
                sourceCode = doc['sourceCode']
                destCode = doc['destCode']
                destTitle = doc['destTitle']
                iconTitle = doc['iconTitle']
                if iconTitle.find('电子教材') < 0:
                    continue
                sort = doc['sort']
                try:
                    trueName = doc['trueName']
                except:
                    trueName = ""
                downloadNum = doc['downloadNum']
                docType = doc['appTypeShowType']
                print(destCode, destTitle, iconTitle)
                url = 'https://plszz.zzedu.net.cn/youjiaoplay/getInfoJson.do?rcode={}&rsType=1&t={}'.format(
                    destCode, int(time.time()))
                res = requests.get(url, headers=headers).text
                res = json.loads(res)
                RDesc = res['info']['RDesc']
                did = res['info']['id']
                RCode = res['info']['RCode']
                feiType = res['info']['feiType']
                url = 'https://plszz.zzedu.net.cn/youjiao/doMutiplePlay.do?rcode={}&userName=4101016001170066&filterType={}&allowPcMain=1'.format(
                    RCode, feiType)
                xmlData = requests.get(url, headers=headers).text
                soup = BeautifulSoup(xmlData, 'lxml')

                for fileTag in soup.find_all('file'):
                    imgUrl = fileTag['path']
                    fileName = fileTag['filepath'].replace('/', '')
                    if fileName.find('mp4') >= 0:
                        ok = 0
                        break
                    print(fileName)
                    if fileName == 'data.xml':
                        continue
                    try:
                        os.mkdir('{}/{}'.format(path, RCode))
                    except:
                        pass
                    content = requests.get(imgUrl, headers=headers).content
                    with open('{}/{}/{}'.format(path, RCode, fileName), 'wb+') as f:
                        f.write(content)
                    sql = 'insert into electronic_material_photo(document_id,photo_url,chapter_id,oss_url) values(%s,%s,%s,%s)'
                    cursor.execute(
                        sql, (did, '{}/{}/{}'.format(path, RCode, fileName), lid, imgUrl))
                sql = 'insert into document(id,subjectId,documentName,documentExplain,url,localPath,fileType,chapterId,vcomChapter,showSort,rcode) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                if ok:
                    cursor.execute(sql, (did, subjectId, destTitle,
                                        RDesc, "", "", docType, lid, 0, sort, RCode))
                db.commit()
            sql = 'update chapter set ok=1 where id=%s'
            cursor.execute(sql, (lid))
            db.commit()
        except:
            pass
    db.close()


def work():
    db, cursor = getDB()
    for type in range(1, 4):
        sql = 'select versionsId,name from data where ok=%s'
        cursor.execute(sql, (type))
        data = cursor.fetchall()
        for line in data:
            versionsId = line[0]
            name = line[1]
            print(name, versionsId)
            getChapterDocs(versionsId)


if __name__ == "__main__":
    work()
