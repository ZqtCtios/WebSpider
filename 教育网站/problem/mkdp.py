import pymysql
import os
db = pymysql.connect(
    "localhost",
    "root",
    "edu123456",
    "hdkt_dev",
    use_unicode=True,
    charset="utf8")
cursor = db.cursor()
home = '/home/data/document'
if os.path.isdir(home) == False:
    os.mkdir(home)


def mkdir():
    sql = 'select mainContent from content group by mainContent'
    cursor.execute(sql)
    data = cursor.fetchall()
    for x in data:
        path = home + '/' + x[0].replace(' ','')

        if os.path.isdir(path) == False:
            print('Mkdir:', path)
            os.mkdir(path)
    sql = 'select mainContent,subContent from content'
    cursor.execute(sql)
    data = cursor.fetchall()
    for x in data:
        path = home + '/' + x[0].replace(' ','') + '/' + x[1].replace(' ','')
        if os.path.isdir(path) == False:
            print('Mkdir:', path)
            os.mkdir(path)

if __name__ == '__main__':
    mkdir()
