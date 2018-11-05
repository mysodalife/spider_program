# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhihucrawlItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class UserInfoItem(scrapy.Item):
    user_id = scrapy.Field()  # 用户id
    user_image_url = scrapy.Field()  # 用户头像 url
    name = scrapy.Field()  # 用户名
    description = scrapy.Field()
    followees_num = scrapy.Field()  # 关注了的人数
    followers_num = scrapy.Field()  # 被关注的人数


class RelationItem(scrapy.Item):
    user_id = scrapy.Field()  # 用户id 自己的用户id
    relation_type = scrapy.Field()  # 关系类型
    relations_id = scrapy.Field()  # 和我有关系的人的 id 列表
