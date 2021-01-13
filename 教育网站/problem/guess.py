import filetype
import os
import threading
import pymysql
#12.38
db = pymysql.connect(
    "localhost",
    "root",
    "edu123456",
    "hdkt_dev",
    use_unicode=True,
    charset="utf8")
cursor = db.cursor()


def getFileType(path):
    kind = filetype.guess(path)
    return kind.extension


def renameFlie(path, type):
    home = '/home/data/'
    os.rename(home + path, home + path + type)


def getdata():
    sql = 'select id,url,documentName from document2 where documentName like \'%.\''
    cursor.execute(sql)
    data = cursor.fetchall()
    return data


def getall(data):
    home = '/home/data/'
    db_temp = pymysql.connect(
        "localhost",
        "root",
        "edu123456",
        "hdkt_dev",
        use_unicode=True,
        charset="utf8")
    cursor_temp = db_temp.cursor()
    for line in data:
        xid = line[0]
        path = line[1]
        filename = line[2]
        print(filename)
        ftype = getFileType(home + path)
        renameFlie(path, ftype)
        filename = filename + ftype
        path = path + ftype
        print(filename)
        sql2 = 'update document2 set documentName=%s,url=%s where id=%s'
        cursor_temp.execute(sql2, (filename,path,xid))
        db_temp.commit()


def work():
    data = getdata()
    dataLen = len(data)
    print(dataLen)
    tnum = 2
    x = dataLen // tnum
    Thead = []
    for r in range(0, tnum):
        t = threading.Thread(target=getall, args=(data[r * x:r * x + x], ))
        Thead.append(t)
    t = threading.Thread(target=getall, args=(data[x * tnum:dataLen], ))

    Thead.append(t)
    for t in Thead:
        t.start()

    for t in Thead:
        t.join()


if __name__ == '__main__':
    work()
