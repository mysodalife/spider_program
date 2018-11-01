# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CnblogspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = scrapy.Field()
    title = scrapy.Field()
    time = scrapy.Field()
    content = scrapy.Field()
    cimage_urls = scrapy.Field() # 存放 图片下载的url list类型
    cimages = scrapy.Field() # 存放图片下载的结果


class newCnblogItem(scrapy.Item):
    body = scrapy.Field()