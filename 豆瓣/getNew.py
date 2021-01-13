import argparse
import requests
import pymysql
from bs4 import BeautifulSoup


def findMoive():

    geturl = 'https://movie.douban.com/chart'
    text = requests.get(geturl).text

    soup = BeautifulSoup(text, "html.parser")
    i = 0
    title = []
    page = []
    img = []
    pf = []
    msg = []
    for table in soup.find_all("tr", attrs={'class': 'item'}):
        try:
            title.append(table.find('td').a.attrs['title'])
            page.append(table.find('td').a.attrs['href'])
            img.append(table.find('td').a.img.attrs['src'])
            pf.append(
                table.find_all(
                    'td',
                    attrs={
                        'valign': 'top'})[1].find(
                    'div',
                    attrs={
                        'class': 'star clearfix'}).find(
                    'span',
                    attrs={
                        'class': 'rating_nums'}).text)
            msg.append(
                table.find_all(
                    'td', attrs={
                        'valign': 'top'})[1].find('div').p.text)

            i += 1
            if i >= 10:
                break
        except BaseException:
            1
    db = pymysql.connect(
        "localhost",
        "root",
        "zqt1997",
        "javaee",
        use_unicode=True,
        charset="utf8")

    cursor = db.cursor()

    sql = 'INSERT INTO new(mid, name, pf, msg, pic, page) VALUES (%s, %s, %s, %s, %s, %s)'
    cursor.execute('TRUNCATE TABLE new')
    db.commit()
    for i in range(len(title)):
        cursor.execute(sql, (i, title[i], pf[i], msg[i], img[i], page[i]))
        db.commit()


if __name__ == '__main__':

    findMoive()
