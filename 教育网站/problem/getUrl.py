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





def getdata():
    sql = 'select id,path from cp'
    cursor.execute(sql)
    data = cursor.fetchall()
    return data


def getall(data):
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
        sql2='select documentName from document where id=%s'
        cursor_temp.execute(sql2,(xid))
        name=cursor_temp.fetchall()[0][0]
        path=path+'/'+name
        sql2 = 'update document set url=%s where id=%s'
        cursor_temp.execute(sql2, (path,xid))
        db_temp.commit()
        print(xid)


def work():
    data = getdata()
    dataLen = len(data)
    print(dataLen)
    tnum = 20
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
