import requests
# 导入requests库
import re
# 导入re库
url = 'http://qq.yh31.com/zjbq/0551964.html'
# 需要爬取的地址
html = requests.get(url).text
# 获得相应的html
# print(html)
p = re.compile(r'<img src="/tp/zjbq/(.*?)" alt="" />')
# 正则表达式
item = re.findall(p, html)
# 在html找到相应元素保存在item中
for filename in item:
    print('http://qq.yh31.com/tp/zjbq/' + filename)
    #输出地址
for filename in item:
    f=open(filename,'wb')
    url='http://qq.yh31.com/tp/zjbq/' + filename
    content=requests.get(url).content
    #content返回图片的二进制信息
    f.write(content)
    f.close()

