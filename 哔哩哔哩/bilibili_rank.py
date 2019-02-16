import requests
import json
import pymysql
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
#浏览器信息
db = pymysql.connect(
        "localhost",
        "root",
        "Zqt_1997",
        "bilibili",
        use_unicode=True,
        charset="utf8")
cursor = db.cursor()
sql = 'INSERT INTO fanju(title,play,Ctime,videos,pic,coin,av) VALUES (%s, %s, %s, %s, %s, %s, %s)'
for pn in range(1,642):    
    try:
        url='https://api.bilibili.com/archive_rank/getarchiverankbypartion?type=jsonp&tid=32&pn=%s'%(pn)
        content=requests.get(url,headers=headers).text
        js=json.loads(content)
        for i in range(20):
            x=js['data']['archives']['%s'%(i)]
            title=x['title']
            play=x['play']
            if play=='--':
                play=0
            time=x['create']
            videos=x['videos']
            pic=x['pic']
            coin=x['stat']['coin']
            av=x['aid']
            # print('标题:',title)
            # print('播放量:',play)
            # print('时间:',time)
            # print('集数:',videos)
            # print('硬币数:',coin)
            # print('av号:',av)
            cursor.execute(sql,(title,play,time,videos,pic,coin,av))
            db.commit()
        print('第%s页成功'%(pn))
    except:
        print('第%s页错误'%(pn))


