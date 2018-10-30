# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
from scrapy.exceptions import DropItem
from scrapy.contrib.pipeline.images import ImagesPipeline
from scrapy import Request


class CnblogspiderPipeline(object):

    def __init__(self):
        self.file = open('papers.json', 'wb')

    def process_item(self, item, spider):
        '''
        :param item: 爬取到的 item
        :param spider: 爬取到该item 的spider
        :return: 要么返回 item 要么返回 dropitem的异常
        '''
        if item['title']:
            # 利用dict 和item 进行转化
            line = (json.dumps(dict(item)) + "\n").encode('utf-8')
            self.file.write(line)
            return item
        else:
            raise DropItem('Missing title in %s' % (item,))


class MyImagePipeline(ImagesPipeline):
    def item_completed(self, results, item, info):
        '''
        下载结束的会调用
        :param results: 得到的一个list
        :param item:
        :param info:
        :return: 返回的结果的结果是一样的 要么返回整个item 要么抛出 DropItem的异常
        '''
        image_paths = [ x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem('Item contains no Image')
        item['image_paths'] = image_paths
        return item # 这里是返回  item

    def get_media_requests(self, item, info):
        '''
        得到的item
        :param item: 得到的item
        :param info:
        :return: 返回整个的 Request
        '''
        for image_url in item['cimage_urls']:
            yield Request(image_url) # 返回很多 request