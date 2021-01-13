def getSum(headers,num):
    url='https://www.zhihu.com/question/'+str(num)
    print('获取知乎页面:  ',url)
    html=requests.get(url,headers=headers).text
    name=re.findall(r'data-reactid="4">(.*?))</title>',html)[0]
    sum=re.findall(r'<span>(\d*) 个回答',html)[0]
    print('----%s----共个%s回答'%(name,sum))
    return int(sum)