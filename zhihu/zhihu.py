# -*- coding: utf-8 -*-
import urllib2
import re
def findMoive(values):
    url = 'https://www.douban.com/search?cat=1002&q='
    geturl = url+values
    request = urllib2.Request(geturl)
    response = urllib2.urlopen(request)
    content = response.read()
    pattern = re.compile(r' <span class="rating_nums">(.*?)</span>')
    item = re.findall(pattern,content)
    if len(item) == 0 :
        return 0
    else:
        return float(item[0])



i=1
moives_all=[]
print "开始爬取知乎页面"
while i>0:
    print "正在爬取页面", i
    geturl = 'https://www.zhihu.com/question/25699277?page='+str(i)
    request = urllib2.Request(geturl)
    response = urllib2.urlopen(request)
    content = response.read()
    pattern = re.compile(r'《(.*?)》')
    item = re.findall(pattern,content)
    if len(item) == 0:
        break
    moives_all.extend(item)
    i=i+1
print "爬取完毕"
print  "开始获取豆瓣评分...."
moives=list(set(moives_all))
ranting=[]
for x in moives:
    x=str(x)
    try:
        n=findMoive(x)
    except:
        n=0
    ranting.append(n)
    print x,n
print "豆瓣评分获取完毕"
dict={}
for i in range(len(moives)):
    dict[moives[i]]=ranting[i]
dict=sorted(dict.items(),key=lambda item:item[1],reverse=True)
print "最终结果为："
for x in dict:
    print x[0],x[1]