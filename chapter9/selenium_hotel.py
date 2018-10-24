# -*- coding: utf-8 -*-
# @Time         : 2018/10/24 16:10
# @Author       : sodalife
# @File         : selenium_hotel.py
# @Description  : 指定一个完整的爬虫
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import datetime
import codecs
from bs4 import BeautifulSoup
from selenium.webdriver import Chrome


class QunaSpider(object):

    def get_hotel(self,driver:Chrome,to_city, fromdate, todate):
        ele_tocity = driver.find_element_by_name('toCity')
        ele_fromdate = driver.find_element_by_name('fromDate')
        ele_search = driver.find_element_by_class_name('button-search')
        ele_todate = driver.find_element_by_name('toDate')

        ele_tocity.click()
        ele_tocity.clear()
        ele_tocity.send_keys(to_city)

        ele_fromdate.clear()
        ele_fromdate.send_keys(fromdate)
        ele_todate.clear()
        ele_todate.send_keys(todate)

        page_num = 0
        while True:
            try:
                WebDriverWait(driver,10).until(EC.title_contains(to_city))
            except Exception as e:
                print(e)
                break
            # 这里已经拿到了完整的页面
            time.sleep(5)

            # 操作浏览器滑到底部
            js = 'window.scrollTo(0, document.body.scrollHeight)'
            driver.execute_script(js)
            time.sleep(5)

            htm_const = driver.page_source

            soup = BeautifulSoup(htm_const, 'html.parser',from_encoding='utf-8')
            infos = soup.find_all('div',class_='item_hotel_info')

            # 将清洗得到的内容写入到文件中
            f = codecs.open(to_city + fromdate + u'.html','a','utf-8')
            for info in infos:
                f.write(str(page_num) + '--' * 50)
                content = info.get_text().replace(" ", "").replace("\t", "").strip()
                for line in [ln for ln in content.splitlines() if ln.strip()]:
                    f.write(line)
                    f.write('\r\n')
            f.close()

            try:
                element = WebDriverWait(driver,10).until(EC.visibility_of(driver.find_element_by_css_selector('.item.next')))
                element.click()
                page_num += 1
                time.sleep(10)
            except Exception as e:
                print(e)
                break
    def crawl(self,root_url,to_city):
        today = datetime.date.today().strftime('%Y-%m-%d')
        tomorrow = datetime.date.today() + datetime.timedelta(days=1)
        tomorrow = tomorrow.strftime('%Y-%m-%d')
        driver = Chrome()
        driver.set_page_load_timeout(50) # 对于整个浏览器设置加载时间
        driver.get(root_url)
        driver.maximize_window() # 浏览器最大化显示 自动化的测试工具
        driver.implicitly_wait(10) # 隐式等待
        self.get_hotel(driver,to_city,today,tomorrow)


if __name__ == '__main__':
    spider = QunaSpider()
    spider.crawl('http://hotel.qunar.com/',u'上海')