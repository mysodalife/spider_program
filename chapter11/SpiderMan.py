# -*- coding: utf-8 -*-
# @Time         : 2018/10/27 19:21
# @Author       : sodalife
# @File         : SpiderMan
# @Description  : 爬虫的调度程序
from chapter11.Spider_Dataoutput import SpiderDataOutput
from chapter11.Spider_parser import SpiderParser
from chapter11.SpiderDownloader import SpiderDownloader


class SpiderMan(object):

    def __init__(self):
        # 调度器的初始化函数用来
        self.downloader = SpiderDownloader()
        self.parser = SpiderParser()
        self.output = SpiderDataOutput()

    def crawl(self, root_url):
        content = self.downloader.download(root_url)
        for info in self.parser.get_kw_cat(content):
            print(info)
            cat_name = info['cat_name']
            detail_url = f'http://ts.kuwo.cn/service/getlist.v31.php?act=detail&id={info["id"]}'
            # 这里并没有设置 URL管理器来将新产生的 url 放入到整个
            content = self.downloader.download(detail_url)
            details = self.parser.get_kw_detail(content)
            self.output.output_html(self.output.filepath, details)
        self.output.output_end(self.output.filepath)


if __name__ == '__main__':
    spider = SpiderMan()
    spider.crawl('http://ts.kuwo.cn/service/getlist.v31.php?act=cat&id=50')
