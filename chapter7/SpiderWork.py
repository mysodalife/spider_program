# -*- coding: utf-8 -*-
# @Time         : 2018/10/16 20:26
# @Author       : sodalife
# @File         : SpiderWork.py
# @Description  : 爬虫节点的工作流程
from multiprocessing.managers import BaseManager
from chapter7.HtmlDownloader import HtmlDownloader
from chapter7.HtmlParser import HtmlParser
# import sys
# sys.setrecursionlimit(2000)


class SpiderWork(object):

    def __init__(self):
        BaseManager.register('get_task_queue')
        BaseManager.register('get_result_queue')
        server_addr = '222.199.193.65'
        print('Connect to server %s' % server_addr)
        self.m = BaseManager(address=(server_addr, 8001), authkey='baike'.encode('utf-8'))
        self.m.connect()
        self.task = self.m.get_task_queue()
        self.result = self.m.get_result_queue()
        self.downloader = HtmlDownloader()
        self.parser = HtmlParser()
        print('init finish')

    def crawl(self):
        while True:
            try:
                if not self.task.empty():
                    url = self.task.get()
                    if url == 'end':
                        print('控制节点通知爬虫节点结束工作')
                        self.result.put({'new_urls': 'end', 'data': 'data'})
                        return
                    print('爬虫节点正在解析 %s' % url.encode('utf-8'))
                    content = self.downloader.download(url)
                    new_urls, data = self.parser.pareser(url, content)
                    self.result.put({'new_urls': new_urls, 'data': data})
            except EOFError as e:
                print('连接工作节点失败')
                return
            except Exception as e:
                print(e)
                print('crawl failed')


if __name__ == '__main__':
    spider = SpiderWork()
    spider.crawl()
