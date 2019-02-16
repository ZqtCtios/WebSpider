#!/usr/bin/python
from bs4 import BeautifulSoup
import pymysql
import requests
import json
import threading
import re


def getDBcon():
    db = pymysql.connect(
        "localhost",
        "root",
        "zqt1997",
        "21cnjy",
        use_unicode=True,
        charset="utf8")
    cursor = db.cursor()
    return db, cursor


def getData():
    db, cursor = getDBcon()
    cursor.execute(
        'select * from knowledge_msg')
    data = cursor.fetchall()
    db.close()
    return data


def getJson(xd, chid, upid):
    url = 'https://www.21cnjy.com/soft.php?mod=zyindex_ajax&knowledges=1&xd=%s&chid=%s&upid=%s' % (
        xd, chid, upid)
    text = requests.get(url).text
    return text


def getKnowledge(pids, xd, chid, subjectId, depth=1):
    db, cursor = getDBcon()
    for i in range(len(pids)):
        pid = pids[i]
        print(pid)
        cdata = getJson(xd, chid, pid)
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
            level = depth+1
            chid_pid.append(rcode)
            if child == 0:
                is_last = 1
            else:
                is_last = 0
            sql = 'insert into dict_prepare_lesson_knowledge(knowleage_name,subject_id,parent_id,level,is_last,sort,knowledge_id) values (%s,%s,%s,%s,%s,%s,%s)'
            cursor.execute(sql, (cname, subjectId, pid,
                                 level, is_last, sort, rcode))
        
            print(subjectId, cname, pid, level, is_last, sort, rcode)
        db.commit()
        if len(chid_pid) > 0:
            getKnowledge(chid_pid, xd, chid, subjectId, depth=depth+1)
    db.close()


def work1():
    db, cursor = getDBcon()
    data = getData()
    for line in data:
        chid = line[0]
        subjectName = line[1]
        kid = line[2]
        subjectId = line[3]
        xd = line[4]
        url = 'https://www.21cnjy.com/knowledge.php?chid={}&kid={}'.format(
            chid, kid)
        text = requests.get(url).text
        # with open('x.html','w+') as f:
        #     f.write(text)
        p = r'knowledges = (\[.*?\])'
        res = re.findall(p, text)[0]
        js = json.loads(res, encoding='utf8')
        for x in js:
            kid = x['id']
            kname = x['name']
            child = x['child']
            if int(child) > 0:
                is_last = 1
            else:
                is_last = 0
            sql = 'insert into dict_prepare_lesson_knowledge(knowleage_name,subject_id,parent_id,level,is_last,sort,knowledge_id) values (%s,%s,%s,%s,%s,%s,%s)'
            cursor.execute(sql, (kname, subjectId, 0, 1, is_last, 1, kid))
            print(kname, subjectId, 0, 1, is_last, 1, kid)
    db.commit()
    db.close()


def work2():
    db, cursor = getDBcon()
    sql = 'select k.id,k.knowledge_id,s.id,s.chid,s.xd from dict_prepare_lesson_knowledge as k inner join subject as s on s.id=k.subject_id and k.id>3'
    cursor.execute(sql)
    data = cursor.fetchall()
    for line in data:
        kid = line[0]
        spId = line[1]
        subjectId = line[2]
        chid = line[3]
        xd = line[4]
        print([spId], xd, chid, subjectId)
        getKnowledge([spId], xd, chid, subjectId)
    db.close()


if __name__ == '__main__':
    work2()
