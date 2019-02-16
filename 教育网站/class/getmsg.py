import requests
import re
from bs4 import BeautifulSoup
from lxml import etree
def getMsg(cid):
    text=requests.get('http://www.class.cn/course/course_detail/?course_id=%s'%(cid)).text 
    html = etree.HTML(text)
    x=html.xpath('//*[@id="course_right"]/div[1]/div/p[2]')[0]
    aims=etree.tostring(x).decode("utf-8")
    time=html.xpath('//*[@id="course_right"]/div[1]/div/h2/span/text()')
    instructions=html.xpath('//*[@id="course_left"]/div[1]/div/section/p')[0]
    instructions=etree.tostring(instructions).decode("utf-8")
    print(time,aims,instructions))

getMsg(8837)