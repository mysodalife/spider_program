# -*- coding: utf-8 -*-
# @Time         : 2018/10/23 20:20
# @Author       : sodalife
# @File         : selenium_page_operation.py
# @Description  : 利用selenium进行页面操作
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains

# 1. 页面交互和填充表单
driver = webdriver.Chrome()

driver.get('file:///D:/spider_program/chapter9/login.html')

username = driver.find_element_by_name('username')
password = driver.find_element_by_name('password')
login_button = driver.find_element_by_xpath('//input[@type="submit"]')

# 2. 填充必要的信息 并模拟点击
username.clear()
password.clear()
username.send_keys('sodalife')
password.send_keys('password')
# login_button.click()

# 利用 select 来选择 html 中的选择框

select = Select(driver.find_element_by_xpath('//form/select'))
# select.select_by_index()
# select.select_by_value()
# select.select_by_visible_text()

# 元素拖拽 找到目标元素 找到源元素 利用 ActionChains 实现
element = driver.find_element_by_name('source')
target = driver.find_element_by_name('target')
action_chains = ActionChains(driver)
action_chains.drag_and_drop(source=element,target=target).perform()
