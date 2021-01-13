import pymysql
import threading
# 12.38
db = pymysql.connect(
    "localhost",
    "root",
    "edu123456",
    "hdkt_dev",
    use_unicode=True,
    charset="utf8")
cursor = db.cursor()
def sp(data):
    db_temp = pymysql.connect(
        "localhost",
        "root",
        "edu123456",
        "hdkt_dev",
        use_unicode=True,
        charset="utf8")
    cursor_temp = db_temp.cursor()
    sql = 'UPDATE down2 SET fp=%s WHERE id=%s'
    for x in data:
        cid = x[0]
        filepath = x[1]
        filepath=filepath+'/'+x[2]
        filepath = filepath.replace(' ', '')      
        print(filepath)
        cursor_temp.execute(sql, (filepath, cid))
        db_temp.commit()
    cursor.close()
    db_temp.close()

def getdata():
    sql = 'SELECT id,path,filename FROM down2 WHERE ok=0 '
    cursor.execute(sql)
    data = cursor.fetchall()
    return data


def work():
    data = getdata()
    dataLen = len(data)
    x = dataLen // 15
    Thead = []
    for r in range(0, 15):
        t = threading.Thread(target=sp, args=(data[r * x:r * x + x], ))
        Thead.append(t)
    t = threading.Thread(target=sp, args=(data[x * 15:dataLen], ))

    Thead.append(t)
    for t in Thead:
        t.start()

    for t in Thead:
        t.join()
if __name__ == '__main__':
    work()
    