# -*- coding: utf-8 -*-
# @Time         : 2018/10/13 15:11
# @Author       : sodalife
# @File         : SpiderMan.py
# @Description  : 爬虫调度器
# 爬虫调度器：URL调度器 URL下载器 URL解析器 数据存储器
from .DataOutput import DataOutput
from .HtmlDownloader import HtmlDownloader
from .URLManager import URLManager
from .HtmlParser import HtmlParser
from email.mime.text import MIMEText
from email.header import Header
from email.utils import parseaddr, formataddr
import smtplib


def format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


class SpiderMan(object):
    def __init__(self):
        self.manager = URLManager()
        self.downloader = HtmlDownloader()
        self.parser = HtmlParser()
        self.output = DataOutput()

    def crawl(self, root_url):
        self.manager.add_new_url(root_url)
        while self.manager.has_new_urls() and self.manager.old_url_size() < 100:
            try:
                new_url = self.manager.get_new_url()
                text = self.downloader.download(new_url)
                new_urls, data = self.parser.parser(new_url, text)
                print(new_urls, data)
                self.manager.add_new_urls(new_urls)
                self.output.store_data(data)
                print(f' 已经抓取了 {self.manager.old_url_size()} 个链接')
            except Exception as e:
                send_mail('crawl failed.')
        self.output.output_html()


def send_mail(info: str):
    msg = MIMEText(info, 'plain', 'utf-8')
    msg['From'] = '17611259722@163.com'
    msg['To'] = '404997294@qq.com'
    msg['Subject'] = Header('Error report', 'utf-8')
    server = smtplib.SMTP('smtp.163.com', 25)
    server.login('17611259722@163.com', 'duhan404997294')
    server.sendmail('17611259722@163.com', ['404997294@qq.com'], msg.as_string())


if __name__ == '__main__':
    spider_man = SpiderMan()
    spider_man.crawl('https://baike.baidu.com/item/%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB/5162711?fr=aladdin')