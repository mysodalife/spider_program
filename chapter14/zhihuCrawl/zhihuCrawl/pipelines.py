# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

# pipeline 主要将整个item 存放到MongoDB中 放到2个数据库中
from scrapy.crawler import Crawler
import mongoengine as me
from .items import *


class UserInfo(me.Document):
    def __init__(self, user_id, user_image_url, name, description, followee_num, follower_num):
        super(UserInfo, self).__init__()
        self.user_id = user_id
        self.user_image_url = user_image_url
        self.name = name
        self.description = description
        self.followees_num = followee_num
        self.followers_num = follower_num

    user_id = me.StringField()
    user_image_url = me.StringField()
    name = me.StringField()
    description = me.StringField()
    followees_num = me.StringField()
    followers_num = me.StringField()


class Relation(me.Document):
    def __init__(self, user_id, relation_type, relation_id):
        super(Relation, self).__init__()
        self.user_id = user_id
        self.relation_type = relation_type
        self.relations_id = relation_id

    user_id = me.StringField()
    relation_type = me.StringField()
    relations_id = me.StringField()


class ZhihucrawlPipeline(object):

    def __init__(self, mongo_host, port, database, username):
        self.mongo_host = mongo_host
        self.port = port
        self.database = database
        self.username = username

    def process_item(self, item, spider):
        '''
        process_item 必须返回item 或者 DropItem 来进行
        :param item:
        :param spider:
        :return:
        '''
        if isinstance(item, UserInfoItem):
            self._process_user_item(item)
        else:
            self._process_relation_item(item)
        return item

    @classmethod
    def from_crawler(cls, crawler: Crawler):
        return cls(mongo_host=crawler.settings.get('MONGO_HOST'), port=crawler.settings.get('MONGO_PORT'),
                   database=crawler.settings.get('DATABASE'), username=crawler.settings.get('MONGO_USERNAME'))

    def open_spider(self, spider):
        me.connect(self.database, host=self.mongo_host, port=self.port, username=self.username, password='duhan')

    def close_spider(self, spider):
        me.connection.disconnect()

    def _process_user_item(self, item):
        '''
        处理一下用户个人的item 存到数据库中
        :param item:
        :return:
        '''
        user = UserInfo(user_id=item['user_id'], user_image_url=item['user_image_url'], name=item['name'],
                        description=item['description'], followee_num=item['followees_num'],
                        follower_num=item['followers_num'])
        user.save()

    def _process_relation_item(self, item):
        relation = Relation(user_id=item['user_id'], relation_type=item['relation_type'],
                            relation_id=item['relations_id'])
        relation.save()
