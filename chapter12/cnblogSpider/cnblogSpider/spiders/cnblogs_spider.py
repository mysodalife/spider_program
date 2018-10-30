# -*- coding: utf-8 -*-
# @Time         : 2018/10/28 10:12
# @Author       : sodalife
# @File         : cnblogs_spider
# @Description  : 记录下创建一个新的 spider类
import scrapy
from ..items import CnblogspiderItem
from scrapy.crawler import CrawlerProcess, CrawlerRunner
from scrapy.utils.project import get_project_settings
from scrapy.utils.log import configure_logging
from twisted.internet import reactor
from scrapy.http import Response
from scrapy.spider import CrawlSpider
from scrapy.spiders.crawl import Rule
from scrapy.spiders.feed import XMLFeedSpider
from scrapy.contrib.linkextractors import LinkExtractor


class CnblogsSpider(scrapy.Spider):
    '''
    每一个spider 必须包含3个属性：1. name 用来区别不同的名字 2. start_urls 用来指定初始的url 3. parse 用来对response 进行解析
    '''
    name = 'cnblogs'
    allowed_domains = ['cnblogs.com']
    start_urls = ['http://www.cnblogs.com/qiyeboy/default.html?page=1']

    def parse(self, response: Response):
        '''
        负责解析 scrapy 传过来的 Response 对象 解析数据 并且将继续跟进的url 传过来
        :param response: Response 对象
        :return: Request Item 的 可迭代对象
        '''

        # from scrapy.shell import inspect_response
        # inspect_response(relllponse,self)

        papers = response.xpath('.//*[@class="day"]')
        for paper in papers:
            # 选择器
            url = paper.xpath('.//*[@class="postTitle"]/a/@href').extract()[0]  # 抽出链接
            title = paper.xpath('.//*[@class="postTitle"]/a/text()').extract()[0]  # 获取到标题
            time = paper.xpath('.//*[@class="dayTitle"]/a/text()').extract()[0]  # 发表时间
            content = paper.xpath('.//*[@class="postTitle"]/a/text()').extract()[0]  # 摘要
            item = CnblogspiderItem(url=url, title=title, time=time, content=content)
            request = scrapy.Request(url=url, callback=self.parse_body)  # 重新提交一个 request
            request.meta['item'] = item  # 利用 meta 字段来
            yield request  # 使用 item 来提交数据

        # 翻页功能的实现本质上构造 Request 并交给 scrapy 的功能
        next_page = scrapy.Selector(response=response).re(u'<a href="(\S*)">下一页</a>')  # 这里有一个分组
        if next_page:
            yield scrapy.Request(url=next_page[0], callback=self.parse)

    def parse_body(self, response):
        '''
        对网页的 body 字段进行解析
        :param response: download 返回的 response
        :return:
        '''
        item = response.meta['item']
        body = scrapy.Selector(response).xpath('.//*[@class="postBody"]')
        item['cimage_urls'] = body.xpath('.//img//@src').extract()  # 提取图片的连接
        yield item


# class CnblogsSpiderFromCrawlSpider(CrawlSpider):
#     '''
#     继承 CrawlSpider 来爬取普通的网站
#     '''
#     name = 'blogs'
#     allowed_domains = ['cnblogs.com']
#     start_urls = ['http://www.cnblogs.com/qiyeboy/default.html?page=1']
#     rules = (Rule(LinkExtractor(allow=("qiyeboy/default.html?page=\d{1,}",)), follow=True, callback="parse_item"),)
#
#     def parse_item(self, response: Response):
#         papers = response.xpath('.//*[@class="day"]')[0]
#         for paper in papers:
#             url = paper.xpath('.//*[@class="postTitle"]/a/@href').extract()[0]
#             title = paper.xpath('.//*[@class="postTitle"]/a/text()').extract()[0]
#             time = paper.xpath('.//*[@class="dayTitle"]/a/text()').extract()[0]
#             content = paper.xpath('.//*[@class="postTitle"]/a/text()').extract()[0]
#             request = scrapy.Request(url=url, callback=self.parse_body)
#             item = CnblogspiderItem(url=url, title=title, time=time, content=content)
#             request['meta'] = item  # 在这里记录了一下最原始的 item 是什么样子的
#             yield request
#
#     def parse_body(self, response: Response):
#         item = response['meta']
#         body = response.xpath('.//*[@class="postBody"]')
#         item['cimage_urls'] = body.xpath('.//img//@src').extract()
#         yield item


# class XMLSpider(XMLFeedSpider):
#     '''
#     XMLFeedSpider 继承 Spider 所以之前的属性也适用
#     '''
#     name = 'cnblogs'
#     start_urls = ['http://feed.cnblogs.com/blog/u/269038/rss']
#     allowed_domains = ['cnblogs.com']
#     iterator = 'html'  # 使用哪个迭代器
#     itertag = 'entry'  # 开始的节点
#
#     def adapt_response(self, response):
#         '''
#         在 response 返回给spider处理之前 处理一下
#         :param response: 返回的response
#         :return:
#         '''
#         return response
#
#     def parse_node(self, response, selector):
#         '''
#         当节点提供满足要求的 itertag 的时候该方法会被调用
#         :param response: 返回的 Response
#         :param selector: response 对应的 Selector
#         :return: 返回 item 或者 Response 的可迭代对象
#         '''
#         print(selector.xpath('id/text()').extract()[0])
#         print(selector.xpath('title/text()').extract()[0])
#         print(selector.xpath('summary/text()').extract()[0])

# 除了使用 scrapy crawl spider_name 来启动爬虫外 ，我们还使用 API的方式启动爬虫

# 第一种方法: 使用 CrawlProcess类

# if __name__ == '__main__':
#     # 创建 CrawlerProcess 类来创建 twisted refactor
#     process = CrawlerProcess({'USER_AGENT':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'})
#     process.crawl(CnblogsSpider)  # 传入所在的类
#     process.start()
#
#     process = CrawlerProcess(get_project_settings())
#     process.crawl('cnblogs') # 传入 spider 的名字
#     process.start()
#
# # 第二种 使用CrawlRunner类 这种方式需要 自己自行关闭 Twisted refactor
#
# if __name__ == '__main__':
#     configure_logging({'LOG_FORMAT':'%(levelname)s: %(message)s'})
#     runner = CrawlerRunner()
#     d = runner.crawl(CnblogsSpider) # 添加爬虫
#     d.addBoth(lambda _:reactor.stop()) # 添加结束的回调函数
#     reactor.run()
