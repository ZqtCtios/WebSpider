import requests
import re
import json
from bs4 import BeautifulSoup
import os
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
    'Cookie': 'd_c0="AJCCgTHWAQyPTlkw64i2kvOSK2qYhKanJ5g=|1499061688"; _zap=f24b1930-7078-478a-bf5e-bb87dbad23e7; q_c1=fbabdc892c3e499ca51a2d466ded906d|1500173415000|1497202664000; capsion_ticket="2|1:0|10:1502450299|14:capsion_ticket|44:MjMzMjQ4NTA0ZjczNDE0Mjg4NjNmYTUzMDIzMmNhYjc=|30585314f893993f53d29072aaf7c9f8a1103de87245c2fc1043e86a10bc15d3"; r_cap_id="YTYwZTY0YTAyM2EwNDI0MmEzMzY5MTdiMzk0YTg2MmE=|1502453206|057d668174c3071ce4ed86d066c7c3f967c57d5d"; cap_id="MzUzZDg0NTZjYzk0NDQwODk0NThiYzM4NTJhYjhjMDE=|1502453206|4bd86c27633443da8718364fc6733f708e27f33f"; z_c0=Mi4xeFB4a0FnQUFBQUFBa0lLQk1kWUJEQmNBQUFCaEFsVk5BQ3kxV1FBaDNRajAtUkVMR0xIWFBCTFBFTjNiY3FJYTlR|1502453504|8e2831fbc9873188632548c6ed44ffe41d350ef0; q_c1=fbabdc892c3e499ca51a2d466ded906d|1502905523000|1497202664000; aliyungf_tc=AQAAAFHQeiSYkwoAys54at7QqHxbCc+R; s-q=noah633; s-i=1; sid=lvp4peeo; __utma=51854390.483180661.1499061688.1502905540.1503127395.19; __utmb=51854390.0.10.1503127395; __utmc=51854390; __utmz=51854390.1503127395.19.17.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmv=51854390.100-1|2=registration_date=20151219=1^3=entry_date=20151219=1; _xsrf=0d159a7c-3a81-410f-9141-711bf063a8c6'
}
def start():
    path='NOAH633'
    if os.path.isdir(path):
        pass
    else:
        os.mkdir(path)
    getUrl()
    
def down(imgs):
    num=1
    for url in imgs:
        content=requests.get(url,headers=headers).content
        f=open('NOAH633/%d.jpg'%(num),'wb')
        f.write(content)
        f.close
        num+=1

def getUrl():

    url = 'https://www.zhihu.com/api/v4/members/dan-wen-hui-10/answers?include=data%5B*%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Cmark_infos%2Ccreated_time%2Cupdated_time%2Creview_info%2Cquestion%2Cexcerpt%2Crelationship.is_authorized%2Cvoting%2Cis_author%2Cis_thanked%2Cis_nothelp%2Cupvoted_followees%3Bdata%5B*%5D.author.badge%5B%3F(type%3Dbest_answerer)%5D.topics&offset=0&limit=20&sort_by=created'
    html = requests.get(url, headers=headers).text
    js = json.loads(html)
    imgs=[]
    for x in js['data']:
        a_id = x['id']
        q_id = x['question']['id']
        url = 'https://www.zhihu.com/question/{}/answer/{}'.format(q_id, a_id)
        img=getImg(url)
        imgs.extend(img)
    down(imgs)
        


def getImg(url):
    html = requests.get(url, headers=headers).text
    soup = BeautifulSoup(html, 'lxml')
    imgs = []
    for x in soup.find(
            'span', attrs={
            'class': 'RichText CopyrightRichText-richText'}).find_all('img'):
        imgs.append(x['src'])
    return imgs[::2]



if __name__ == '__main__':
    start()
