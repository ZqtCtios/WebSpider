import urllib
import urllib.request
import requests
import re
import os
headers = { 'Host':'www.pixiv.net',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0',
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
            'Accept-Encoding':'gzip, deflate',
            'Referer':'http://www.pixiv.net/ranking.php?mode=daily&content=ugoira',
            'Cookie':'PHPSESSID=8d2d82602d88f95db7cd24e37bb0e729; p_ab_id=8; p_ab_id_2=4; a_type=0; module_orders_mypage=%5B%7B%22name%22%3A%22recommended_illusts%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22everyone_new_illusts%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22following_new_illusts%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22mypixiv_new_illusts%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22fanbox%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22featured_tags%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22contests%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22sensei_courses%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22spotlight%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22booth_follow_items%22%2C%22visible%22%3Atrue%7D%5D; is_sensei_service_user=1; login_ever=yes',
            'Connection':'keep-alive',
            'Upgrade-Insecure-Requests':'1',
            'Cache-Control':'max-age=0'}
def getURl(url):
    s = requests.get(url, headers=headers)
    return s.text
def go(i):
    print("开始爬取第"+str(i)+"页")
    url = 'http://www.pixiv.net/ranking.php?mode=daily&content=illust&p='+str(i)
    text = getURl(url)
    pattern = re.compile(r'data-id="(.*?)"')
    item = re.findall(pattern,text)
    if len(item)==0:
        return
    item=set(item)
    for id in item:
        try:
            num=int(id)
            url='http://www.pixiv.net/member_illust.php?mode=medium&illust_id='+id
            text = getURl(url)
            pattern = re.compile(r'img-master/img/(.*?)_p0_master1200\.jpg')
            item2 = re.findall(pattern, text)
            if len(item2)==0:
                continue
            url2='https://i.pximg.net/img-master/img/'+item2[0]+'_p0_master1200.jpg'
            headers = ('Referer', url)  # 防盗链，修改访问来源
            opener = urllib.request.build_opener()
            opener.addheaders = [headers]
            data = opener.open(url2).read()
            with open('pixiv/'+id+'.jpg', "wb") as code:
                code.write(data)
            print("图片"+id+".jpg 保存成功")
        except:
            continue

if __name__ == '__main__':
	for i in range(20):
		go(i)


