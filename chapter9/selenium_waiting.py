# -*- coding: utf-8 -*-
# @Time         : 2018/10/23 21:33
# @Author       : sodalife
# @File         : selenium_waiting.py
# @Description  : selenium 的等待策略

# 由于广泛使用了ajax 技术
# 这里是显式等待 知道某个条件出现为止
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get('https://www.baidu.com/')
try:
    # 显示等待10秒 直到元素出现
    element = WebDriverWait(driver=driver, timeout=10).until(EC.presence_of_element_located(By.ID, "myDynamicElement"))
finally:
    driver.quit()

# 这里是隐式等待
# 只要设置了隐式等待系统中就默认对每个指令都指定这么长的时间 一直伴随着这个 webdriver的生命周期
from selenium import webdriver
driver = webdriver.Chrome()
driver.implicitly_wait(10) # 设置这个语句后 每个语句都会执行等待时间