# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy import Request, Spider
from scrapy.exceptions import DropItem
import pymongo
from scrapy.crawler import Crawler
from scrapy.pipelines.images import ImagesPipeline


class CnblogsPipeline(object):
    def process_item(self, item, spider):
        return item


class MyImagePipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        for image_url in item['cimage_urls']:
            yield Request(url=image_url)

    def item_completed(self, results, item, info):
        images = [x['path'] for ok, x in results if ok]
        if not images:
            raise DropItem('image download failed.')
        item['cimages'] = images
        yield item  # 返回 item


class MongoPipeline(object):
    collection_name = 'scrapy_items'

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawl(cls, crawl: Crawler):
        '''
        从一个 crawler 对象构造 pipeline
        :param crawl: 是一个 Crawler 对象 Crawler对象可以访问到 scrapy 所有的核心组件 settings  signals
        :return:
        '''
        return cls(mongo_uri=crawl.settings.get('MONGO_URI'), mongo_db=crawl.settings.get('MONGO_DATABASE', 'items'))

    def open_spider(self, spider: Spider):
        '''
        打开 spider 的时候调用
        :param spider:
        :return:
        '''
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider: Spider):
        '''
        关闭spider时候调用
        :param spider:
        :return:
        '''
        self.client.close()

    def process_item(self, item, spider):
        '''
        process_item 要么 return item 要么 抛出 DropItem
        :param item:
        :param spider:
        :return:
        '''
        self.db[self.collection_name].insert(dict(item))
        return item
