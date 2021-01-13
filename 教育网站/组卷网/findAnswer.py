from selenium import webdriver
import time

import pymysql
import requests
import json
import threading
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': 'HqNL_ef65_saltkey=Yu9ZSF15; HqNL_ef65_lastvisit=1567155840; Hm_lvt_0280ecaa2722243b1de4829d59602c72=1567159442; HqNL_ef65_sid=Y4Y144; HqNL_ef65_lastact=1567522207%09index.php%09index; chid=d79688f1e7866722fd16866f40a252116287a86b4e6e2213e3150af3ba96e038a%3A2%3A%7Bi%3A0%3Bs%3A4%3A%22chid%22%3Bi%3A1%3Bs%3A1%3A%222%22%3B%7D; xd=494a1f745cfdce14dad87288ba1fd45465b7d32eec1df130011fd3cd0b6415c2a%3A2%3A%7Bi%3A0%3Bs%3A2%3A%22xd%22%3Bi%3A1%3Bs%3A1%3A%221%22%3B%7D; _sync_login_identity=f68bec521fe2fd6386153cde1f881b38bc4a02bc4874ed3397b9efb756c28656a%3A2%3A%7Bi%3A0%3Bs%3A20%3A%22_sync_login_identity%22%3Bi%3A1%3Bs%3A63%3A%22%5B9444196%2C%22SPuZ5l7tQ-xss27JPGxuyUj5QSdbByZI%22%2C70512%2C1567553088%2C0%5D%22%3B%7D; PHPSESSID=rdmjjs16mb76b4vv665mjtnne2; _identity=5ea8a0101ef7423477bb6096bab86509586429e2ed6f2282e9619cae42f2664da%3A2%3A%7Bi%3A0%3Bs%3A9%3A%22_identity%22%3Bi%3A1%3Bs%3A50%3A%22%5B9444196%2C%224ec2f6dd6d06c1ef8ffdf4250b496af0%22%2C86400%5D%22%3B%7D; _csrf=2521ac5da2d35bb4487bff9964423ba61d3faced417c5063c5c4957967396daca%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22gls5fndnTpqsf1JnsVQ_6BtUF22q69Bs%22%3B%7D; Hm_lpvt_0280ecaa2722243b1de4829d59602c72=1567553090; Hm_lvt_5d70f3704df08b4bfedf4a7c4fb415ef=1567220217,1567292334,1567413356,1567553091; Hm_lpvt_5d70f3704df08b4bfedf4a7c4fb415ef=1567553091',
    'Host': 'zujuan.21cnjy.com',
    'If-None-Match': 'W/"1235f-Z3U1a0vd1HuexULF53ZsTdJLTEw"',
    'Referer': 'https://zujuan.21cnjy.com/question?tree_type=category&xd=2&chid=3',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
}


def getProblemIdList():
    db = pymysql.connect(
        "localhost",
        "root",
        "zqt1997",
        "hdkt_dev",
        use_unicode=True,
        charset="utf8")
    cursor = db.cursor()
    #sql = 'select scrapId,parentId from problem where ok=0 and parentId=0'
    sql='select id from problem where ok=0 and parentId=0'
    cursor.execute(sql)
    data = cursor.fetchall()
    problemIdList = []
    for line in data:
        problemIdList.append(int(line[0]))
    db.close()
    return problemIdList


def getJsonData(pid):
    url = 'https://zujuan.21cnjy.com/question/detail/{}'.format(pid)
    html = requests.get(url, headers=headers).text
    p = html.find('question: ')
    p = html.find('{', p)
    q = html.find('});', p)
    try:
        data=json.loads(html[p:q - 1])
    except:
        data={}
    return data


def download(url, filename):
    res = requests.get(url).content
    with open(filename, 'wb+') as f:
        f.write(res)


def work(problemIdList):
    db = pymysql.connect(
        "localhost",
        "root",
        "zqt1997",
        "hdkt_dev",
        use_unicode=True,
        charset="utf8")
    cursor = db.cursor()
    for pid in problemIdList:
        print('pid:', pid)
        sql='select chapterId from problem_chapter where  problemId=%s'
        cursor.execute(sql,(pid))
        chapterId=cursor.fetchall()[0]
        jsonData = getJsonData(pid)
        if len(jsonData.keys())==0:
            continue
        qid = jsonData['question_id']
        answerImgUrl = jsonData['answer']
        answerPath = 'answer/{}.png'.format(qid)
        if answerImgUrl is None:
            answerImgUrl = ''
        elif len(answerImgUrl) > 0 and answerImgUrl.find('http') == 0:
            download(answerImgUrl, answerPath)
        else:
            answerPath = answerImgUrl
        explanationImgUrl = jsonData['explanation']
        explanationPath = 'explanation/{}.png'.format(qid)
        if explanationImgUrl is None:
            explanationImgUrl = ''
        elif len(explanationImgUrl) > 0 and explanationImgUrl.find('http') == 0:
            download(explanationImgUrl, explanationPath)
        else:
            explanationPath = explanationImgUrl
        childList = jsonData['list']
        if childList is None:
            childList = []
        for child in childList:
            qid = child['question_id']
            sql='select id from problem where id=%s'
            cursor.execute(sql,(qid))
            res=cursor.fetchall()
            if len(res)==0:
                parentId = pid
                scrapId = child['question_id']
                problemType = child['question_channel_type']
                problemDiffculty = child['difficult_index']

                problemKind = child['exam_type']
                problemContent = child['title']
                problemContentStr = child['question_text']
                problemAnswer = str(child['options'])
                problemAnswer = db.escape_string(problemAnswer)
                answer = child['answer']
                # analyses = getAnalyses()
                # print(scrapId, scrapId, problemType, problemDiffculty,problemKind, problemContent, problemContentStr, problemAnswer, answer)
                sql = 'insert into problem(id,scrapId,problemType,problemDiffculty,problemKind,problemContent,problemContentStr,problemAnswer,answer,parentId) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                cursor.execute(
                    sql,
                    (scrapId,
                     scrapId,
                     problemType,
                     problemDiffculty,
                     problemKind,
                     problemContent,
                     problemContentStr,
                     problemAnswer,
                     answer,
                     parentId))
                sql = 'insert into problem_chapter(chapterId,problemId) values (%s,%s)'
                cursor.execute(sql, (chapterId, scrapId))

            childAnswerImgUrl = child['answer']
            childAnswerPath = 'answer/{}.png'.format(qid)
            if childAnswerImgUrl is None:
                childAnswerImgUrl = ''
            elif len(childAnswerImgUrl) > 0 and childAnswerImgUrl.find('http') == 0:
                download(childAnswerImgUrl, childAnswerPath)
            else:
                childAnswerPath = childAnswerImgUrl
            childExplanationImgUrl = child['explanation']
            childExplanationPath = 'explanation/{}.png'.format(qid)
            if childExplanationImgUrl is None:
                childExplanationImgUrl = ''
            elif len(childExplanationImgUrl) > 0 and childExplanationImgUrl.find('http') == 0:
                download(childExplanationImgUrl, childExplanationPath)
            else:
                childExplanationPath = childExplanationImgUrl
            sql = 'update problem set answer=%s,analyses=%s,parentId=%s,ok=1 where id=%s'
            cursor.execute(sql, (childAnswerPath, childExplanationPath, pid,qid))
        print(answerPath, explanationPath, pid)
        sql = 'update problem set answer=%s,analyses=%s,ok=1 where id=%s'
        cursor.execute(sql, (answerPath, explanationPath, pid))
        db.commit()

    db.close()


def MultiThreadDownload(problemIdList, tnum=16):
    startTime = time.time()
    dataLen = len(problemIdList)
    x = dataLen // tnum
    print('启动{}线程下载'.format(tnum))
    Thead = []
    for r in range(0, tnum):
        t = threading.Thread(
            target=work,
            args=(
                problemIdList[r * x:r * x + x],
            ))
        Thead.append(t)
    t = threading.Thread(
        target=work,
        args=(
            problemIdList[x * tnum:dataLen],
        ))

    Thead.append(t)
    for t in Thead:
        t.start()

    for t in Thead:
        t.join()
    endTime = time.time()
    print('下载结束')
    print('共用时：', endTime - startTime)
    return True


if __name__ == '__main__':
    while True:
        problemIdList = getProblemIdList()
        if len(problemIdList) == 0:
            break
        MultiThreadDownload(problemIdList)
