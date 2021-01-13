# -*- coding: utf-8 -*-
# @Time    : 2019-09-12 15:20
# @Author  : ctios
# @Software: PyCharm
# 高中
import requests
import pymysql
import json

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Connection': 'keep-alive',
    # 'Cookie': 'screen_width_id=w1200; localAreaCode=1.; gjpt=zz; sso_login_flag=1; vut=ce88385a007dd9d7b3b26e35ef0cbdb5ffbd495885c4bfbbeae8d99e9f55b27316fff9933948c515; isPortal=1; returnSso=ssozz.zzedu.net.cn; ut=ce88385a007dd9d7b3b26e35ef0cbdb5ffbd495885c4bfbbeae8d99e9f55b273a300068bfe7757ff; phoneBuyAble=false; lastVisitTime=20190910171251; student_number=""; regFlg=0; username=4101016001170066; usertype=2; schoolStage=0001%2C0002%2C0003; schoolId=410101600117; defaultStage=0001; areacode=1.1.1; schoolAreaCode=1.1.1; JSESSIONID=NvMN7T1I8opa+JCt2sAPNPUj; __session:0.34460476379889093:=https:',
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


def getVersionData():
    db, cursor = getDB()
    sql = 'select * from data where ok=0'
    cursor.execute(sql)
    data = cursor.fetchall()
    return data


def work():
    db, cursor = getDB()
    jcData = getVersionData()
    for line in jcData:
        name = line[1]
        section = line[2]
        gradeId = line[4]
        rxiu = line[5]
        subject = line[7]
        subjectId = line[8]
        versions = line[9]
        versionsId = line[10]
        url = 'https://plszz.zzedu.net.cn/youjiao/baceContent.do?section={}&subject={}&versions={}&rxiu={}&listType=1&classHour=1'.format(
            section, subject, versions, rxiu)
        jsonText = requests.get(url, headers=headers).text
        jsonData = json.loads(jsonText)['classes']
        for chapter in jsonData[1:]:
            order = chapter['order']
            pid = chapter['pid']
            code = chapter['code']
            name = chapter['name']
            print(name)
            sql = 'insert into chapter(termid,gradeid,sectioncode,subjectid,versionid,vc_chapterId,vc_chapterName,vc_material_id,seq_no,parentId) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            cursor.execute(sql, (0, gradeId, section,
                                 subjectId, versionsId, code, name, pid, order, 0))
            try:
                classHours = chapter['classHours']
            except:
                continue
            for childChapter in classHours:
                ccId = childChapter['id']
                name = childChapter['name']
                sortNum = childChapter['sortNum']
                sql = 'insert into chapter(termid,gradeid,sectioncode,subjectid,versionid,vc_chapterId,vc_chapterName,vc_material_id,seq_no,parentId) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                cursor.execute(sql, (0, gradeId, section, subjectId,
                                     versionsId, ccId, name, pid, sortNum, code))
                print('     ', name)
        db.commit()


if __name__ == '__main__':
    work()
