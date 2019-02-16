#!/usr/bin/python
from bs4 import BeautifulSoup
import pymysql
import requests
import json
import threading


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

def work():
    db, cursor=getDBcon()
    cursor.execute('select id,areaId from msg2')
    data=cursor.fetchall()
    last=1
    i=1882
    for line in data:
        mid=line[0]
        aid=int(line[1])
        sql='update msg2 set sort=%s where id=%s'
        cursor.execute(sql,(i,mid))
        print(mid,aid,i)
        i+=1
    db.commit()
    db.close()
def test():
    # for i in range(0,19):
    #     sql='update document2 set prepare_lesson_level=1 where prepare_lesson_level=5 and id>={} and id<{};'.format(i*100000,(i+1)*100000);
    #     sql2='update document2 set prepare_lesson_level=2 where prepare_lesson_level=12 and id>={} and id<{};'.format(i*100000,(i+1)*100000);
    #     sql3='update document2 set prepare_lesson_level=3 where prepare_lesson_level=34 and id>={} and id<{};'.format(i*100000,(i+1)*100000);
    #     print(sql)
    #     print(sql2)
    #     print(sql3)
    # for i in range(0,6):
    #     # sql='update document2 as d inner join dict_prepare_lesson_type as t on d.id>={} and d.id<{} and t.type_id=d.prepare_lesson_type set d.prepare_lesson_type=t.id;'.format(i*100000,(i+1)*100000);
    #     # sql='update document2 set prepare_lesson_area=prepare_lesson_area+1 where id>={} and id<{} and prepare_lesson_area<32;'.format(i*100000,(i+1)*100000);
    #     # sql2='update document2 set prepare_lesson_area=prepare_lesson_area-2 where id>={} and id<{} and prepare_lesson_area>33;'.format(i*100000,(i+1)*100000);
    #     # sql3='update document2 set document_classify=2 where id>={} and id<{};'.format(i*100000,(i+1)*100000);
    #     # sql4='insert into prepare_lesson_document(id,document_classify,special_area_teachingmaterial_id,document_name,document_explain,url,file_type,used_count,prepare_lesson_type,prepare_lesson_importance,prepare_lesson_area,prepare_lesson_level,teacher_id,document_source,show_sort,show_time,document_id,username) select  id,document_classify,teachingmaterial_id,document_name,document_explain,url,file_type,used_count,prepare_lesson_type,prepare_lesson_importance,prepare_lesson_area,prepare_lesson_level,teacher_id,document_source,show_sort,show_time,document_id,username from document2 where id>={} and id<{};'.format(i*100000,(i+1)*100000);
    #     sql='insert into prepare_lesson_document(id,document_classify,subject_id,document_name,document_explain,url,file_type,used_count,prepare_lesson_type,teacher_id,document_source,show_sort,show_time,document_id,username) select id+2999999,document_classify+1,subject_id,document_name,document_explain,url,file_type,used_count,prepare_lesson_type,teacher_id,document_source,show_sort,show_time,document_id,username from document3 where id>={} and id<{};'.format(i*100000,(i+1)*100000);
    #     print(sql)
    #     #print(sql2)
#1708387
    with open('test.sql','r') as f:
        data=f.readlines()
    for x in data:
        x=x.replace('\n','')
        sh='mysqldump -u root -pzqt1997 21cnjy {}>{}.sql'.format(x,x)
        print(sh)
if __name__ == '__main__':
    test()
    
