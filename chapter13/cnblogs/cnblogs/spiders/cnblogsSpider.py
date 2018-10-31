# -*- coding: utf-8 -*-
# @Time         : 2018/10/30 11:17
# @Author       : sodalife
# @File         : cnblogsSpider
# @Description  : Spider文件
from ..items import CnblogsItem
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider
from scrapy.http.request import Request
from scrapy.spiders.feed import XMLFeedSpider
from scrapy import Spider
from scrapy.loader import ItemLoader
from scrapy.http.request.form import FormRequest
from scrapy.http.response import Response
from scrapy.loader.processors import TakeFirst, MapCompose, Join
from scrapy.spiders.crawl import Rule


class CnblogsSpider(Spider):
    name = 'spider'
    allowed_domains = ['cnblogs.com']
    start_urls = ['http://www.cnblogs.com/qiyeboy/default.html?page=1']

    #  在
    custom_settings = {
        'ITEM_PIPELINES': {
            'scrapy.pipelines.images.ImagesPipeline': 1,
            'cnblogs.pipelines.MongoPipeline': 300,
        }
    }

    def parse(self, response):
        loader = ItemLoader(item=CnblogsItem, response=response)
        loader.add_xpath('name', '//div[@class="product_name"]')
        loader.add_xpath('name', '//div[@class="product_title"]')
        loader.add_xpath('price', '//p[@id="price"]')
        loader.add_css('stock', 'p #stock')
        loader.add_value('last_updated', 'today')
        return loader.load_item()  # 这里返回的是item


class CnblogsCrawlSpider(CrawlSpider):
    name = 'crawlcnblogs'
    allowed_domains = ['cnblogs.com']
    start_urls = ['http://www.cnblogs.com/qiyeboy/default.html?page=1']
    rules = (Rule(LinkExtractor(allow=('/qiyeboy/default.html?page=\d{1,}',)), follow=True, callback='parse_item'),)

    def parse_item(self, response):
        papers = response.xpath('.//*[@class="day"]')
        for paper in papers:
            url = paper.xpath('.//*[@class="postTitle"]/a/@href').extract()[0]
            title = paper.xpath('.//*[@class="postTitle"]/a/text()').extract()[0]
            time = paper.xpath('.//*[@class="dayTitle"]/a/text()').extract()[0]
            content = paper.xpath('.//*[@class="postTitle"]/a/text()').extract()[0]
            item = CnblogsItem(url=url, title=title, time=time, content=content)
            request = Request(url=url, callback=self.parse_body)
            request['meta'] = item
            yield request

    def parse_body(self, response):
        item = response['meta']
        body = response.xpath('.//*[@class="postBody"]')
        item['cimage_urls'] = body.xpath('.//img//@src').extract()  # 将 url 添加到整个
        yield item


class XMLSpider(XMLFeedSpider):
    name = 'xmlspider'
    allowed_domains = ['cnblogs.com']
    start_urls = ['http://feed.cnblogs.com/blog/u/269038/rss']
    iterator = 'html'
    itertag = 'entry'

    def adapt_response(self, response):
        '''
        在 response 交给 spider 处理之前 处理一下
        :param response: 生成的 response
        :return:
        '''
        return response

    def parse_node(self, response, selector):
        '''
        当节点符合 itertag  执行一个该函数
        :param response:
        :param selector: response 对应的 selector
        :return: 返回 item 或者 request
        '''
        print(selector.xpath('id/text()').extract()[0])
        print(selector.xpath('title/text()').extract()[0])
        print(selector.xpath('summary/text()').extract()[0])


# Request 和 Response 都是在 spider中进行处理的
class LoginSpider(Spider):
    name = 'example.com'
    allowed_domains = ['example.com']
    start_urls = ['http://www.example.com/users/login.php']

    def parse(self, response):
        # 使用 FormRequest 得到了Response 可以处理一些隐藏表单
        yield FormRequest.from_response(response=response, formdata={'username': 'sodalife', 'password': 'secret'},
                                        callback=self.after_login)

    def after_login(self, response: Response):
        if 'authentication failed' in response.body:
            self.logger.error("Login failed.")
            return
