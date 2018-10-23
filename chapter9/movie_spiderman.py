# -*- coding: utf-8 -*-
# @Time         : 2018/10/22 11:45
# @Author       : sodalife
# @File         : movie_spiderman.py
# @Description  : 爬虫调度器
import time
from chapter9.movie_dataoutput import DataOutPut
from chapter9.movie_htmldownloader import HtmlDownloader
from chapter9.moive_htmlparser import HtmlParser


class SpiderMan(object):
    def __init__(self):
        self.downloader = HtmlDownloader()
        self.parser = HtmlParser()
        self.output = DataOutPut()

    def crawl(self, root_url):
        '''
        :param root_url: 最跟的url
        :return:
        '''
        content = self.downloader.download(root_url)
        urls = self.parser.parse_url(content)  # 获取所有的url
        for url in urls:
            try:
                t = time.strftime('%Y%m%d%H%M%S3282', time.localtime())
                #  下面这个是脚本发送的请求的url
                rank_url = f'http://service.library.mtime.com/Movie.api?Ajax_CallBack=true&Ajax_CallBackType=Mtime.Library.Services&Ajax_CallBackMethod=GetMovieOverviewRating&Ajax_CrossDomain=1&Ajax_RequestUrl={url[0]}&t={t}&Ajax_CallBackArgument0={url[1]}'
                rank_content = self.downloader.download(rank_url)
                data = self.parser.parser_json(rank_url, rank_content)
                self.output.store_data(data)
            except Exception as e:
                print(e, 'Crawl failed.')
        self.output.output_end()
        print('crawl success')


if __name__ == '__main__':
    spider = SpiderMan()
    spider.crawl('http://theater.mtime.com/China_Beijing/')
