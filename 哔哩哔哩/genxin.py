import requests
import json
import re
print('哔哩哔哩更新：\n')

urls = []


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


def work(num, conut):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
        'Cookie': 'finger=edc6ecda; sid=5v3lyil6; DedeUserID=33285185; DedeUserID__ckMd5=8fe4562504109256; SESSDATA=4c1c83ef%2C1512802205%2C5dec60b4; bili_jct=3cd98c8e269232aef8426fececa0b112; LIVE_BUVID=AUTO4315102102115053; buvid3=D968CD3D-4EE9-495D-AE34-FF2B5544B4FC47166infoc; UM_distinctid=15fa0dd9a3139-07896c0a885d84-c303767-1fa400-15fa0dd9a333b; fts=1510232400; pgv_pvi=7338741760; rpdid=olilkiswwkdosowikipww; _cnt_pm=0; _cnt_notify=0; _dfcaptcha=ef80adc0d9ab210b2345430f9f33cc27; pgv_si=s2756832256; _cnt_dyn=0; _cnt_dyn__ckMd5=42c5c8dec5428373'}
    url = 'https://api.bilibili.com/x/web-feed/feed?callback=jQuery17208093876707749166_1510128744195&jsonp=jsonp&ps=10&pn={}&type=0&_=1510128749821'.format(
        num)
    html = requests.get(url, headers=headers).text + 'end'
    p = r'jQuery[0-9]*_[0-9]*\((.*?)\)end'
    js = re.findall(p, html)[0]
    data = json.loads(js)
    for x in data['data']:
        try:
            title = x['archive']['title']
            id = x['archive']['aid']
            owner = x['archive']['owner']['name']
            url = 'https://www.bilibili.com/video/av' + str(id)
            urls.append(url)
            print(
                alignment(str(conut), 10, align='left'),
                alignment(title, 100, align='left'),
                alignment(owner, 40, align='left'),
                url + '\n')
            conut += 1
        except BaseException:
            pass
    return conut


if __name__ == '__main__':
    conut = 1
    for i in range(1, 6):
        conut = work(i, conut)
    x=int(input("打开："))
    cmd='start '+urls[x-1]
    import os
    os.system(cmd)
