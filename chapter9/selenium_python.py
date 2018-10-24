# -*- coding: utf-8 -*-
# @Time         : 2018/10/23 19:27
# @Author       : sodalife
# @File         : selenium_python.py
# @Description  : 使用selenium+python+phantomjs 进行爬虫
'''
selenium: 自动化的测试工具 负责驱动浏览器 并且和python对接
phantom: 渲染和解析js
python: 用来做后期的处理
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get('http://www.baidu.com/')
assert u'百度' in driver.title
elem = driver.find_element_by_name('wd') # 找到相关的元素
elem.clear() # 清空里面的内容
elem.send_keys(u'网络爬虫') # 输入内容
elem.send_keys(Keys.RETURN)
time.sleep(3)
assert u'网络爬虫' not in driver.page_source
driver.close()