# -*- coding: utf-8 -*-
# @Time    : 2019-06-14 12:19
# @Author  : ctios
# @Software: PyCharm
from selenium import webdriver
import time
driver = webdriver.Chrome()
url = 'http://auth.bupt.edu.cn/authserver/login?service=http%3a%2f%2fyjxt.bupt.edu.cn%2fULogin.aspx'
driver.get(url)
userInput = driver.find_element_by_id("username")
userInput.send_keys("2019140669")
pswdInput = driver.find_element_by_id("password")
pswdInput.send_keys("05251550")
submit = driver.find_element_by_xpath('//*[@id="casLoginForm"]/input[4]')
submit.click()
a=driver.page_source

