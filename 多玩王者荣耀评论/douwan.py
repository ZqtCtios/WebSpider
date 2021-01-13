import os
import re
import pymysql
import requests
import threading
from bs4 import BeautifulSoup

headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

def getText(url):
    content=''
    try:
        html=requests.get(url,headers=headers).text
        soup=BeautifulSoup(html,'html.parser')
        num=int(soup.find_all('span',attrs={'class':'xi1'})[1].text)
        num=num//15+1
        for i in range(2,num):
            url=url[:-8]+str(i)+url[-7:]
            html=html+requests.get(url,headers=headers).text
        soup=BeautifulSoup(html,'html.parser')
        
        for x in soup.find_all('td',attrs={'class':'t_f'}):
            line=re.sub('[’!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~0-9a-zA-Z【】“”！，。？：、]+','',x.text)
            line=line.replace("space","").replace("\n", "")
            content+=line
    except:
        pass
    return content.replace("\r","").replace("\n", "")
    
def getHmtl(x):
    db = pymysql.connect(
        "localhost",
        "root",
        "Zqt_1997",
        "python",
        use_unicode=True,
        charset="utf8")
    cursor = db.cursor()
    sql = 'INSERT INTO duowan(title,page) VALUES (%s, %s)'
    for page in range(x,x+10):
        print('正在爬取第%s页'%(page))
        url='http://bbs.duowan.com/forum-2637-%s.html'%(page)
        html=requests.get(url,headers=headers).text
        soup=BeautifulSoup(html,'html.parser')

        for a in soup.find_all('a',attrs={'onclick':'atarget(this)'}):
            title=a.text
            tempUrl='http://bbs.duowan.com/'+a['href']
            page=getText(tempUrl)
            cursor.execute(sql,(title,page))
            db.commit()

if __name__ == '__main__':
    Thead=[]
    for x in range(1,110,10):
        t=threading.Thread(target=getHmtl,args=(x,))
        Thead.append(t)
    
    for t in Thead:
        t.start()
    
    for t in Thead:
        t.join()
  
        
    


    