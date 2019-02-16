import json
import time
import threading
import requests
from bs4 import BeautifulSoup
import pymysql

db = pymysql.connect(
    "localhost",
    "root",
    "zqt1997",
    "work2",
    use_unicode=True,
    charset="utf8")
cursor = db.cursor()
headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36',
}

gradeData = [
    '46371', '46372', '46373', '46374', '46375', '46376', '46377', '46378',
    '46379', '46380', '88262', '88263'
]

#gradeData=['119480','128314','132948','139442']


def getChapterJson(pid):
    url = 'https://www.21cnjy.com/soft.php'
    data = {
        'mod': 'zyindex_ajax',
        'categories': '1',
        'xd': '2',
        'chid': '3',
        'upid': pid
    }
    text = requests.get(url, headers=headers, params=data).text
    return text


def getChapter(pids, gradeId=0, start=0):
    for i in range(len(pids)):
        pid = pids[i]
        gradeId = 134980
        cdata = getChapterJson(pid)
        try:
            js = json.loads(cdata)
        except:
            print(pid)
        chid_pid = []
        sort = 0
        for chapter in js:
            sort += 1
            rcode = chapter['id']
            cname = chapter['name']
            child = int(chapter['child'])
            level = int(chapter['depth']) - 2
            for j in range(level):
                print('  ', end='')
            print(cname)
            chid_pid.append(rcode)
            if child == 0:
                is_last = 1
            else:
                is_last = 0
            sql = 'insert into temp(spiderId,subjectId,teachIngMaterialId,gradeId,chapterName,parentId,level,is_last,sort) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            cursor.execute(sql, (rcode, 's101', '10000', gradeId, cname, pid,
                                 level, is_last, sort))
            db.commit()

        if len(chid_pid) > 0:
            getChapter(chid_pid, gradeId=gradeId, start=1)


if __name__ == '__main__':
    getChapter([17418])
