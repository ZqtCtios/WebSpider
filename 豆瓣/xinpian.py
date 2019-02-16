import requests
import json
from bs4 import BeautifulSoup
import operator 

def alignment(str1, space, align='left'):
    length = len(str1.encode('gbk'))
    space = space - length if space >= length else 0
    if align == 'left':
        str1 = str1 + ' ' * space
    elif align == 'right':
        str1 = ' ' * space + str1
    elif align == 'center':
        str1 = ' ' * (space // 2) + str1 + ' ' * (space - space // 2)
    return str1
dic={'name':'','pf':'','region':'','director':'','actors':''}
dics=[]
print('豆瓣新片：')
print()
url = 'https://movie.douban.com/cinema/nowplaying/beijing'
html = requests.get(url).text
soup = BeautifulSoup(html, "html.parser")
for li in soup.find(
    "ul", attrs={
        'class': 'lists'}).find_all(
            "li", attrs={
                'class': 'list-item'}):
    dic['name'] = li.attrs['data-title']
    dic['pf'] = li.attrs['data-score']
    dic['region'] = li.attrs['data-region'].split()[0]
    dic['director'] = li.attrs['data-director'].split()[0]
    dic['actors'] = li.attrs['data-actors']
    dics.append(dic.copy())

dics=sorted(dics, key=operator.itemgetter('pf'),reverse=True)

for x in dics:
    print(
        '名称：{} 评分：{}  {} 导演：{} 演员：{}'.format(
            alignment(x['name'], 40), 
            alignment(x['pf'], 6), 
            alignment(x['region'], 10), 
            alignment(x['director'], 20), 
            x['actors']
            )
        )
    print()

