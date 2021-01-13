import pymysql
import json
db = pymysql.connect(
    "localhost",
    "root",
    "Zqt_1997",
    "hdkt_dev",
    use_unicode=True,
    charset="utf8")
cursor = db.cursor()
def getall():
    sql='select * from gaozhongjiaocai'
    cursor.execute(sql)
    ans=cursor.fetchall()
    for line in ans:
        cid=line[0]
        content=line[1]
        section = line[2]
        subject = line[3]
        versions = line[4]
        rxiu = line[5]
        js=json.loads(content)['classes']
        name=js[0]['allname']
        sql='update gaozhongjiaocai set content=%s where id=%s'
        cursor.execute(sql,(name,cid))
        db.commit()
        # for i in range(1,len(js)):
        #     x=js[i]
        #     name=x['name']
        #     code=x['code']
        #     data=str(x)
        #     sql='insert into chapter(classname,jiaocaiid,data,code) values(%s,%s,%s,%s)'
        #     cursor.execute(sql,(name,cid,data,code))
        #     db.commit()


if __name__ == '__main__':
    getall()