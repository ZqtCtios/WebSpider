#!/usr/bin/python

import pymysql
import re

# 这个文件是获取同步资源，专区的选项信息，比如地区，星级


def getDBcon():
    # 连接数据库
    db = pymysql.connect(
        "localhost",
        "root",
        "zqt1997",
        "21cnjy",
        use_unicode=True,
        charset="utf8")
    cursor = db.cursor()
    return db, cursor


def getArea(html):
    p = r'data-param=\"diquid=([0-9]*?)\">(.*?)</a>'
    res = re.findall(p, html)
    return res


def getImportance(html):
    p = r'data-param=\"isjin=([0-9]*?)\">(.*?)</a>'
    res = re.findall(p, html)
    return res


def getLevel(html):
    p = r'data-param=\"stars=([0-9]*?)\">(.*?)</a>'
    res = re.findall(p, html)
    return res


def getType(html):
    p = r'data-param=\"typeid=([0-9]*?)\">(.*?)</a>'
    res = re.findall(p, html)
    return res


def WorkForSynchronizeResources():
    # 处理同步资源信息
    # 来自于SynchronizeResources.html
    db, cursor = getDBcon()
    with open('SynchronizeResources.html', 'r') as f:
        html = f.read()
    html = html.replace('\n', '').replace(' ', '')

    res = getType(html)  # 获取类型信息
    for i in range(len(res)):
        typeid = res[i][0]
        typName = res[i][1]
        sql = 'insert into dict_prepare_lesson_type(name,sort,type_id) values(%s,%s,%s)'
        cursor.execute(sql, (typName, i+1, typeid))
    db.commit()

    res = getArea(html)  # 获取地区信息
    for i in range(len(res)):
        diquid = res[i][0]
        areaName = res[i][1]
        sql = 'insert into dict_prepare_lesson_area(name,sort,area_id) values(%s,%s,%s)'
        cursor.execute(sql, (areaName, i+1, diquid))
    db.commit()

    res = getImportance(html)  # 获取精品普通信息
    for i in range(len(res)):
        isjin = res[i][0]
        importanceName = res[i][1]
        sql = 'insert into dict_prepare_lesson_importance(name,sort,importance_id) values(%s,%s,%s)'
        cursor.execute(sql, (importanceName, i+1, isjin))
    db.commit()

    res = getLevel(html)  # 获取星级信息
    for i in range(len(res)):
        stars = res[i][0]
        levelName = res[i][1]
        sql = 'insert into dict_prepare_lesson_level(name,sort,level_id) values(%s,%s,%s)'
        cursor.execute(sql, (levelName, i+1, stars))
    db.commit()

    cursor.close()
    db.close()


def getGradeMsg():
    db, cursor = getDBcon()
    # 获取 科目 年级 请求参数信息
    with open('SynchronizeResources.html', 'r') as f:
        html = f.read()
    html = html.replace('\n', '').replace(' ', '')
    p = r'data-xd=\"([0-9]*?)\"class=\"tabitem-h.*?\">(.*?)</a>'
    xueduan = []  # 学段
    xueduanName = []  # 学段名字
    res = re.findall(p, html)
    for x in res:
        xueduan.append(int(x[0]))
        xueduanName.append(x[1])
    print(xueduan)
    print(xueduanName)
    p = r'data-chid=\"([0-9]*?)\"class=".*?">(.*?)</a>'
    xueduan = []
    i = 0
    chid = []  # 学科
    chidname = []  # 学科名
    res = re.findall(p, html)
    for x in res:
        if int(x[0]) == 2:
            i += 1
        xueduan.append(i)
        chid.append(int(x[0]))
        chidname.append(x[1])
    for i in range(len(xueduan)):
        xd = xueduan[i]
        xdName = xueduanName[xd-1]
        ch = chid[i]
        sname = chidname[i]
        sql='insert into msg values(%s,%s,%s,%s)'
        cursor.execute(sql,(xd,xdName,ch,sname))
        db.commit()
    db.close()


if __name__ == '__main__':
    getGradeMsg()
