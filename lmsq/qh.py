import requests
import pymysql
from bs4 import BeautifulSoup
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
}
text=''
# db = pymysql.connect(
#         "localhost",
#         "root",
#         "Zqt_1997",
#         "lmqs",
#         use_unicode=True,
#         charset="utf8")
# c=db.cursor()
# sql='insert into qh(content) values (%s)'
for i in range(30):
    url='http://www.juzimi.com/tags/%E6%83%85%E8%AF%9D?page={}'.format(i)
    html=requests.get(url,headers=headers).text
    soup = BeautifulSoup(html, 'lxml')
    print(html)
    for x in soup.find_all('div',attrs={'class':'views-field-phpcode-1'}):
        temp=x.a.text
        print(temp)
        #c.execute(sql,(temp))
        #db.commit()
