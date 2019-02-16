import urllib.request
from bs4 import BeautifulSoup
import pymysql
import re


# 豆瓣电影top250


def __getHtml():
    data = []
    pageNum = 1
    pageSize = 0
    try:
        while (pageSize <= 225):
            # headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
            # 'Referer':None #注意如果依然不能抓取的话，这里可以设置抓取网站的host
            # }
            # opener = urllib.request.build_opener()
            # opener.addheaders = [headers]
            url = "https://movie.douban.com/top250?start=" + str(pageSize) + "&filter="
            # data['html%s' % i ]=urllib.request.urlopen(url).read().decode("utf-8")
            data.append(urllib.request.urlopen(url).read().decode("utf-8"))
            pageSize += 25
            pageNum += 1
            print(pageSize, pageNum)
    except Exception as e:
        raise e
    return data


def __getData(html):
    title = []
    rating_num = []
    range_num = []
    pic=[]
    msg=[]
    data = {}
    page=[]
    # bs4解析html
    soup = BeautifulSoup(html, "html.parser")
    for li in soup.find("ol", attrs={'class': 'grid_view'}).find_all("li"):
        title.append(li.find("span", class_="title").text)
        rating_num.append(li.find("div", class_='star').find("span", class_='rating_num').text)
        range_num.append(li.find("div", class_='pic').find("em").text)
        msg.append(li.find('div',class_='info').find('div',class_='bd').find('p',class_='').text)
        pic.append(li.find('div',class_='pic').a.find('img',class_='').attrs['src'])
        page.append(li.find('div',class_='pic').a.attrs['href'])
    print(len(pic))
    data['title'] = title
    data['rating_num'] = rating_num
    data['range_num'] = range_num
    data['pic']=pic
    data['msg']=msg
    data['page']=page
    return data





if __name__ == '__main__':
    datas = []
    htmls = __getHtml()
    for x in htmls:
        data = __getData(x)
        datas.append(data)
        # print(htmls)
    db = pymysql.connect("localhost", "root", "zqt1997", "javaee",use_unicode=True, charset="utf8")


    cursor = db.cursor()

    sql = 'UPDATE movie set page=%s where mid=%s'
    for j in range(10):
       data=datas[j]
       for i in range(25):
           cursor.execute(sql, (data['page'][i],int(data['range_num'][i])))
           db.commit()



#__getMovies(datas)