# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.crawler import Crawler
from .items import *
import re
import mongoengine


class YunqiBookList(mongoengine.DynamicDocument):
    novelId = mongoengine.StringField()
    novelName = mongoengine.StringField()
    novelLink = mongoengine.StringField()
    novelAuthor = mongoengine.StringField()
    novelType = mongoengine.StringField()
    novelStatus = mongoengine.StringField()
    novelUpdateTime = mongoengine.StringField()
    novelWords = mongoengine.StringField()
    novelImageUrl = mongoengine.StringField()


class YunqiBookDetail(mongoengine.DynamicDocument):
    novelId = mongoengine.StringField()
    novelLabel = mongoengine.StringField()
    novelAllClick = mongoengine.StringField()
    novelMonthClick = mongoengine.StringField()
    novelWeekClick = mongoengine.StringField()
    novelAllPopular = mongoengine.StringField()
    novelMonthPopular = mongoengine.StringField()
    novelWeekPopular = mongoengine.StringField()
    novelCommentNum = mongoengine.StringField()
    novelAllComm = mongoengine.StringField()
    novelMonthComm = mongoengine.StringField()
    novelWeekComm = mongoengine.StringField()


class YunqicrawlPipeline(object):

    def __init__(self, mongo_host, port, username, database):
        self.mongo_host = mongo_host
        self.port = port
        self.username = username
        self.database = database

    def process_item(self, item, spider):
        if isinstance(item, YunqiBookListItem):
            self._process_booklist_item(item)
        else:
            self._process_bookdetail_item(item)

    @classmethod
    def from_crawler(cls, crawler: Crawler):
        return cls(mongo_host=crawler.settings.get('MONGODB_HOST'), port=crawler.settings.get('MONGODB_PORT'),
                   username=crawler.settings.get('MONGODB_USERNAME'), database=crawler.settings.get("MONGODB_DATABASE"))

    def open_spider(self, spider):
        mongoengine.connection.disconnect()
        mongoengine.connect(self.database, host=self.mongo_host, port=self.port, username=self.username,
                            password='duhan')

    def close_spider(self, spider):
        mongoengine.connection.disconnect()

    def _process_booklist_item(self, item):
        document = YunqiBookList()
        document.novelId = item['novelId']
        document.novelName = item['novelName']
        document.novelLink = item['novelLink']
        document.novelAuthor = item['novelAuthor']
        document.novelType = item['novelType']
        document.novelStatus = item['novelStatus']
        document.novelUpdateTime = item['novelUpdateTime']
        document.novelWords = item['novelWords']
        document.novelImageUrl = item['novelImageUrl']
        document.save()

    def _process_bookdetail_item(self, item):
        '''
        对小说中的细节信息进行一下数据清洗，提取其中的数字信息
        :param item:
        :return:
        '''
        document = YunqiBookDetail()
        document.novelId = item['novelId']

        pattern = re.compile(r'\d+')

        item['novelLabel'] = item['novelLabel'].strip().replace('\n', '')
        document.novelLabel = item['novelLabel']

        match = pattern.search(item['novelAllClick'])
        document.novelAllClick = match.group() if match else item['novelAllClick']

        match = pattern.search(item['novelMonthClick'])
        document.novelMonthClick = match.group() if match else item['novelMonthClick']

        match = pattern.search(item['novelWeekClick'])
        document.novelWeekClick = match.group() if match else item['novelWeekClick']

        match = pattern.search(item['novelAllPopular'])
        document.novelAllPopular = match.group() if match else item['novelAllPopular']

        match = pattern.search(item['novelMonthPopular'])
        document.novelMonthPopular = match.group() if match else item['novelMonthPopular']

        match = pattern.search(item['novelWeekPopular'])
        document.novelWeekPopular = match.group() if match else item['novelWeekPopular']

        match = pattern.search(item['novelAllComm'])
        document.novelAllComm = match.group() if match else item['novelAllComm']

        match = pattern.search(item['novelMonthComm'])
        document.novelMonthComm = match.group() if match else item['novelMonthComm']

        match = pattern.search(item['novelMonthComm'])
        document.novelWeekComm = match.group() if match else item['novelWeekComm']

        document.novelCommentNum = item['novelCommentNum']

        document.save()
