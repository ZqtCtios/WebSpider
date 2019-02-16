
# -*- coding: UTF-8 -*-
import urllib
import urllib2
import re

i=1
pic_all=[]
print "开始爬取知乎页面"
for i in range(1,100):
    print "正在爬取页面", i
    geturl = 'https://www.zhihu.com/question/22212644?page='+str(i)
    request = urllib2.Request(geturl)
    response = urllib2.urlopen(request)
    content = response.read()
    pattern = re.compile(r'https://pic3\.zhimg\.com/(.*?)\.jpg')
    item = re.findall(pattern,content)
    if len(item) == 0:
        break
    pic_all.extend(item)
    i=i+1
print "爬取完毕"
i=1
for x in pic_all:
    url='https://pic3.zhimg.com/'+x+'.jpg'
    path = str("fun/")+str(i)+str(".jpg")
    i += 1
    try:
        urllib.urlretrieve(x, path)
        print "图片",path,"爬取成功"
    except:
        print "图片",path,"爬取失败"
