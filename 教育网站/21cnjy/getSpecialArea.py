#!/usr/bin/python
from bs4 import BeautifulSoup
import pymysql
with open('21cnjy.html', 'r') as f:
    html = f.read() 
db = pymysql.connect(
    "localhost",
    "root",
    "zqt1997",
    "21cnjy",
    use_unicode=True,
    charset="utf8")
cursor = db.cursor()

soup = BeautifulSoup(html, 'lxml')
items = soup.find_all('div', attrs={'class': 'cate-item'})
for div in items:
    fats = div.find_all('div', attrs={'class': 'fat'})
    for fat in fats:
        title = fat.h3.text
        thins = fat.find_all('div', attrs={'class': 'thin'})
        for thin in thins:
            itemName = thin.span.text.replace('：', '')
            for a in thin.find_all('a'):
                href = a['href'][23:-1]
                href = href[href.find('/')+1:]
                if len(href) == 0:
                    href = 0
                href = int(href)
                print(title, itemName, a.text, href)
                cursor.execute('insert into msg values(%s,%s,%s,%s)',(title, itemName, a.text, href))
                db.commit()
