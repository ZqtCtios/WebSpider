import json
import requests
import re
import os
from bs4 import BeautifulSoup
import codecs


def creatDir(num):
    print('创建目录....')
    path = '【%s】内容' % (num)
    if os.path.isdir(path):
        pass
    else:
        os.mkdir(path)
    path = '【%s】图片' % (num)
    if os.path.isdir(path):
        pass
    else:
        os.mkdir(path)
    print('创建目录成功')


def getSum(headers, num):
    url = 'https://www.zhihu.com/question/' + str(num)
    print('获取知乎页面:  ', url)
    html = requests.get(url, headers=headers).text
    name = BeautifulSoup(html, 'html.parser').title.text
    sum = re.findall(r'<span>(\d*) 个回答', html)[0]
    print('----%s----共个%s回答' % (name, sum))
    return int(sum)


def getImgs(headers, num):
    sum = getSum(headers, num)
    imgs = []
    for i in range(0, sum, 20):
        url = 'https://www.zhihu.com/api/v4/questions/46508954/answers?include=data%5B*%5D.is_normal%2Ccontent&offset={0}&limit=20&sort_by=default'.format(
            i)
        s = requests.get(url, headers=headers).text
        data = json.loads(s)
        print(len(data['data']))
        for x in data['data']:
            soup = BeautifulSoup(x['content'], 'html.parser')
            author = x['author']['name']
            dir = '【%s】内容' % (num)
            path = '{0}/{1}.{2}'.format(dir, author, 'html')
            print('获取： ', path)
            f = open(path, 'wb')
            s = x['content'].encode('utf-8')
            f.write(s)
            f.close()
            for x in soup.find_all('img'):
                img = x['src']
                if img == '//zhstatic.zhihu.com/assets/zhihu/ztext/whitedot.jpg':
                    img = x['data-actualsrc']
                imgs.append(img)
                print(img)

    return imgs


def downloadImg(headers,imgs, num):
    dir = '【%s】图片' % (num)
    i = 0
    for url in imgs:
        try:
            content = requests.get(url,timeout=3,headers=headers).content
            if url[-3:] == 'jpg':
                path = '{0}/{1}.{2}'.format(dir, i, 'jpg')
            else:
                path = '{0}/{1}.{2}'.format(dir, i, 'gif')
            print('获取： ', path)
            f = open(path, 'wb')
            f.write(content)
            f.close()
            i = i + 1
            
        except :
            continue
        


if __name__ == '__main__':
    num = 46508954
    creatDir(num)
    headers = {
        'Cookie': 'r_cap_id="NmQzM2M1NGMwYmY1NGM2ZDhlZWNjMWI2NWI0YzNiMzk=|1499061687|aaaf3ce50e5f867335423af711c1b16bea2175fb"; cap_id="YjYxN2Y2Yzg1OGZiNGRjODliMWIxMDRmNWY1OGI5NTc=|1499061687|ba33019288ac56f66dcd0ec6b36d3af171f5966a"; d_c0="AJCCgTHWAQyPTlkw64i2kvOSK2qYhKanJ5g=|1499061688"; _zap=f24b1930-7078-478a-bf5e-bb87dbad23e7; z_c0=Mi4wQUJDTVFzcWhMZ2tBa0lLQk1kWUJEQmNBQUFCaEFsVk55V3FCV1FDdnlDbjRPbGo2RnZZSmdIbkFyWHg5akRzY2hB|1499061705|74fe0c8235c5e30a23274c004b677a6281544492; q_c1=fbabdc892c3e499ca51a2d466ded906d|1500173415000|1497202664000; q_c1=fbabdc892c3e499ca51a2d466ded906d|1500173415000|1497202664000; aliyungf_tc=AQAAABX+pi4BHw8AiSFN3gIsWeCk/62Y; s-q=%E8%A1%A8%E6%83%85%E5%8C%85; s-i=3; sid=21dvsakg; __utma=51854390.483180661.1499061688.1501137673.1501226884.7; __utmb=51854390.0.10.1501226884; __utmc=51854390; __utmz=51854390.1501226884.7.7.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/question/54883718/answer/202284505; __utmv=51854390.100-1|2=registration_date=20151219=1^3=entry_date=20151219=1; _xsrf=635766be-98ff-4013-8673-1788bca19de6',
        'Host': 'www.zhihu.com',
        'Referer': 'https://www.zhihu.com/question/'+str(num),
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    imgs = getImgs(headers, num)
    downloadImg(headers,imgs, num)
