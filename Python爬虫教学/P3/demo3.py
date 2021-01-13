import requests
def getSession():
    s = requests.session()#保持这个登录后的session，用来访问其他页面
    data = {
        '_xsrf':'72c468e2d131f55f48741fb7071277f8',
        'password':'***',
        'captcha_type':'cn',
        'phone_num':'1881**83119'
    }
    url = 'https://www.zhihu.com/login/phone_num'
    html = s.post(url,data)
    return s

