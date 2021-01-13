import os
import threading
import urllib
import requests
from bs4 import BeautifulSoup

#12.38

headers = {}
proxyHost = "http-dyn.abuyun.com"
proxyPort = "9020"

# 代理隧道验证信息
proxyUser = "HO2R82620331664D"
proxyPass = "3EE5F896C43DFAF0"

proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
    "host": proxyHost,
    "port": proxyPort,
    "user": proxyUser,
    "pass": proxyPass,
}

proxies = {
    "http": proxyMeta,
    "https": proxyMeta,
}
proxy_support = urllib.request.ProxyHandler(proxies=proxies)
import time
t=time.time()

def get():
    urllib.request.urlretrieve('https://www.cnblogs.com/feng18/p/5749045.html','x.html')
    print(time.time()-t)
get()