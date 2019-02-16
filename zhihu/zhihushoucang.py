import requests
import re
import os
import chardet
def getUrlText(url):
    headers = { 'Host':'www.zhihu.com',
                'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0',
                'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
                'Accept-Encoding':'gzip, deflate, br',
                'Referer':'https://www.zhihu.com/',
                'Cookie':'aliyungf_tc=AQAAAAIpqTGNbg4A61pI31R8V1O59hMQ; l_n_c=1; q_c1=a52f9bbe383a4a8a80e2129e8e5a02d5|1490937725000|1490937725000; _xsrf=ef2a49dfe93e207c7a7441806d57d9d8; r_cap_id="OGRjMTdhYjM4Yzk5NGZjNDg5OTczM2E2OGE5M2UyNjQ=|1490937725|85fe741b8fcde996e93febe4f3a610ca90c6d75a"; cap_id="M2FjYTcyNmFkOWYzNGNiMzk0NjllYmZmOTY1MTc3NWQ=|1490937725|0490e4c8048ab8e2983ec39991e0c1190c0e3b4e"; d_c0="AFCCMb3HiAuPTqFavv3ss7EkESr9L5GlavI=|1490937726"; _zap=816ba85d-1bda-49ea-a22c-d02f0025901b; __utma=51854390.613922337.1490937730.1490937730.1490937730.1; __utmc=51854390; __utmz=51854390.1490937730.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmv=51854390.100-1|2=registration_date=20151219=1^3=entry_date=20151219=1; z_c0=Mi4wQUJDTVFzcWhMZ2tBVUlJeHZjZUlDeGNBQUFCaEFsVk5CblVGV1FERjY3N0FfOV9kM2dvVlc4MDNGbDBaYWhGdWhn|1490937900|e9bff6fc02e44bfd29dc29d4dd7062d5d258af2c',
                'Connection':'keep-alive',
                'Upgrade-Insecure-Requests':'1',
                'Cache-Control':'max-age=0'}
    s=requests.get(url,headers=headers)
    return s.text
def saveWeb(url,path):

    text=getUrlText(url)
    pattern = re.compile(r'<title data-react-helmet="true" data-reactid="4">(.*?)</title>')
    item = re.findall(pattern,text)
    path=path+'/'+item[0]+'.html'
    text.encode('utf-8')
    f=open(path,"w",encoding='utf-8')
    f.write(text)

def main():
    os.chdir('zhihu')
    print('获取收藏夹...')
    text=getUrlText('https://www.zhihu.com/people/ceng-qing-tao-58/collections');
    pattern = re.compile(r'&quot;http://www.zhihu.com/api/v4/collections/(.*?)&quot;')
    item = re.findall(pattern,text)
    pattern = re.compile(r'&quot;title&quot;:&quot;(.*?)&quot;')
    item2 = re.findall(pattern,text)
    if len(item)==0:
        print('获取失败')
        exit()
    print('获取成功，共有',len(item),'个收藏夹')
    for i in range(len(item)):
        item[i]='https://www.zhihu.com/collection/'+item[i]
        print(item2[i],item[i])
    print('开始爬取收藏夹.......')
    for i in range(len(item)):
        print("正在保存收藏夹",item2[i])
        os.mkdir(item2[i])
        url=item[i]
        text=getUrlText(url)
        pattern = re.compile(r'<link itemprop="url" href="(.*?)">')
        list_ans = re.findall(pattern, text)
        for j in range(len(list_ans)):
            list_ans[j]='https://www.zhihu.com'+list_ans[j]
        pattern = re.compile(r'href="(.*?)" data-za-element-name="Title">')
        list_zl = re.findall(pattern, text)
        list_ans.extend(list_zl)
        for x in list_ans:
            try:
                saveWeb(x,item2[i])
            except:
                print('失败')



main()