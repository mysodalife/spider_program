# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CnblogsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = scrapy.Field()
    title = scrapy.Field()
    time = scrapy.Field()
    content = scrapy.Field()
    cimage_urls = scrapy.Field() # 存储要下载的图片的 url
    cimages = scrapy.Field() # 存储图片下载的结果
