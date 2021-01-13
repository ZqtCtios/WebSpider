import json
import os
import re
import threading
import time

import pymysql
import requests

db = pymysql.connect(
    "localhost",
    "root",
    "edu123456",
    "hdkt_dev",
    use_unicode=True,
    charset="utf8")
cursor = db.cursor()


def showSubject():
    sql = 'select id,subjectName from dict_subject'
    cursor.execute(sql)
    data = cursor.fetchall()
    for i in range(len(data)):
        sid = data[i][0]
        name = data[i][1]
        print("%-3d %s" % (i + 1, name))
    s = input('输入要查看的科目序号')
    showTeach(data[int(s) - 1][0])


def showTeach(sid):
    print()
    print()
    sql = 'select id,materialName from dict_teachingmaterial where subjectId like %s'
    cursor.execute(sql, (sid))
    data = cursor.fetchall()
    for i in range(len(data)):
        name = data[i][1]
        print("%-3d %s" % (i + 1, name))
    s = input('输入要查看的教材序号')
    showGrade(sid, data[int(s) - 1][0])


def showGrade(sid, tid):
    print()
    print()
    sql = 'select id,gradeName from dict_grade where subjectId like %s and teachingMaterialId =%s'
    cursor.execute(sql, (sid, tid))
    data = cursor.fetchall()
    for i in range(len(data)):
        name = data[i][1]
        print("%-3d %s" % (i + 1, name))
    s = input('输入要查看的年纪序号')
    showChapter(sid, tid, data[int(s) - 1][0])


def showChapter(sid, tid, gid):
    print()
    print()
    sql = 'select id,chapterName,level from chapter where subjectId like %s and teachingMaterialId =%s and gradeId=%s'
    cursor.execute(sql, (sid, tid, gid))
    data = cursor.fetchall()
    for i in range(len(data)):
        name = data[i][1]
        level = int(data[i][2])
        if level == 1:
            print("%-3d %s" % (i + 1, name))
        else:
            print("%-3d       %s" % (i + 1, name))
    s = input('输入要查看的章节序号')
    chioce(data[int(s) - 1][0])

def chioce(cid):
    print()
    print()
    print('1  按章节查找')
    print('2  按知识点查找')
    s=input('选择查找方式')
    if int(s)==1:
        showProblem(cid)
    else:
        showProblem2(cid)
def showProblem(cid):
    sql = 'select problemId from chap_to_problem where chapterId = %s'
    cursor.execute(sql, (cid))
    data = cursor.fetchall()
    ids = str(data[0][0])
    for i in range(1, len(data)):
        s = str(data[i][0])
        ids = ids + ',' + s    
    sql='select problemContent from problem4 where id in (%s)'%(ids)
    cursor.execute(sql)
    data=cursor.fetchall()
    f=open('/var/www/html/index.html','w+')
    s=''
    for line in data:
        s=s+line[0]+'\n';
    f.write(s)
    f.close() 
        
def showProblem2(cid):
    print()
    print()
    sql = 'select knowledgeId,name from chap_to_knowledge2 where chapterId = %s'
    cursor.execute(sql, (cid))
    data = cursor.fetchall()
    ids = str(data[0][0])
    for i in range(1, len(data)):
        s = str(data[i][0])
        ids = ids + ',' + s
        name = data[i][1]
        print("%-3d %s" % (i + 1, name))
    sql ='select problemId from problem_knowledge3 where knowledgeId in (%s)'%(ids)
    cursor.execute(sql)
    data = cursor.fetchall()
    ids = str(data[0][0])
    for i in range(1, len(data)):
        s = str(data[i][0])
        ids = ids + ',' + s  
    sql='select problemContent from problem4 where id in (%s)'%(ids)
    cursor.execute(sql)
    data=cursor.fetchall()
    f=open('/var/www/html/index.html','w+')
    s=''
    for line in data:
        s=s+line[0]+'\n';
    f.write(s)
    f.close() 
        

if __name__ == '__main__':
    showSubject()
