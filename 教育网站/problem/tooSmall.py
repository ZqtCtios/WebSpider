import os
import threading
import urllib
import mkdp
import time
import datetime
import pymysql
import requests
from bs4 import BeautifulSoup

# 12.38
db = pymysql.connect(
    "localhost",
    "root",
    "edu123456",
    "hdkt_dev",
    use_unicode=True,
    charset="utf8")
cursor = db.cursor()

def getdata():
    sql = 'SELECT id,fp,rcode FROM down WHERE ok=1 '
    cursor.execute(sql)
    data = cursor.fetchall()
    return data