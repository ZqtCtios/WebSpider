import requests
import argparse
import pymysql
from bs4 import BeautifulSoup


def findMoive(values):

    url = 'https://www.douban.com/search?cat=1002&q='
    geturl = url + values
    text = requests.get(geturl).text

    soup = BeautifulSoup(text, "html.parser")
    i = 0
    title = []
    page = []
    img = []
    pf = []
    msg = []
    for div in soup.find_all("div", attrs={'class': 'result'}):
        try:
            title.append(
                div.find(
                    'div', attrs={
                        'class': 'content'}).find(
                    'div', attrs={
                        'class': 'title'}).a.text)
            page.append(
                div.find(
                    'div', attrs={
                        'class': 'pic'}).a.attrs['href'])
            img.append(
                div.find(
                    'div', attrs={
                        'class': 'pic'}).img.attrs['src'])
            pf.append(div.find('div',
                               attrs={'class': 'rating-info'}).find('span',
                                                                    attrs={'class': 'rating_nums'}).text)
            msg.append(div.p.text)
            i += 1
            if i >= 4:
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

    sql = 'INSERT INTO search(mid, name, pf, msg, pic, page) VALUES (%s, %s, %s, %s, %s, %s)'
    cursor.execute('TRUNCATE TABLE search')
    db.commit()
    for i in range(len(title)):
        cursor.execute(sql, (i, title[i], pf[i], msg[i], img[i], page[i]))
        db.commit()


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("name")
    args = parser.parse_args()
    name = args.name
    print(name)

    findMoive(name)
