# -*- coding: utf-8 -*-
# @Time         : 2018/10/31 19:36
# @Author       : sodalife
# @File         : extensions
# @Description  : scrapy 的扩展
import logging
from scrapy import signals
from scrapy.exceptions import NotConfigured

logger = logging.getLogger(__name__)


class SpiderOpenCloseLogging(object):

    def __init__(self, item_count):
        '''
        扩展在 扩展类被实例化时进行加载， 实例化代码必须在 初始化函数中构造
        :param item_count:
        '''
        self.item_count = item_count
        self.items_scraped = 0

    @classmethod
    def from_crawler(cls, crawler):
        # 先检查一下是否存在相应的配置 如果不存在 就抛出异常 禁用扩展
        if not crawler.settings.getbool('MYEXT_ENABLED'):
            raise NotConfigured
        item_count = crawler.settings.getint('MYEXT_ITEMCOUNT', 1000)

        # 创建一个实例化的扩展
        ext = cls(item_count=item_count)

        # 将各个信号绑定到对应的处理函数
        crawler.signals.connect(ext.spider_opened, signal=signals.spider_opened)
        crawler.signals.connect(ext.spider_closed, signal=signals.spider_closed)
        crawler.signals.connect(ext.item_scraped, signal=signals.item_scraped)

    def spider_opened(self, spider):
        logger.info("opened spider %s", spider.name)

    def spider_closed(self, spider):
        logger.info("closed spider %s", spider.name)

    def item_scraped(self, item, spider):
        self.items_scraped += 1
        if self.items_scraped % self.item_count == 0:
            logger.info("scraped %d items.", self.items_scraped)
