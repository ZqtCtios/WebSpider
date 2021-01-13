from bs4 import BeautifulSoup
import requests
import json

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Host': 'zujuan.21cnjy.com',
    'Pragma': 'no-cache',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}


def getQuestionData(xd, chid, categories, page):
    url = 'https://zujuan.21cnjy.com/api/question/list?xd={}&chid={}&categories={}&page={}'.format(
        xd, chid, categories, page)
    jsonText = requests.get(url, headers=headers).json()
    return jsonText


def getAnserData(pid):
    url = 'https://zujuan.21cnjy.com/question/detail/{}'.format(pid)
    html = requests.get(url, headers=headers).text
    p = html.find('question: ')
    p = html.find('{', p)
    q = html.find('});', p)
    try:
        data = json.loads(html[p:q - 1])
    except:
        data = {}
    return data


if __name__ == '__main__':
    print(getAnserData(42582657))
