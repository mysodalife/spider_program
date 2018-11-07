# -*- coding: utf-8 -*-
import scrapy
from ..items import YunqiBookListItem, YunqiBookDetailItem
from scrapy.http.response import Response


class YunqiQqComSpider(scrapy.Spider):
    name = 'yunqi.qq.com'
    allowed_domains = ['qq.com']
    start_urls = ['http://yunqi.qq.com/bk/so2/n30p1']

    def parse(self, response: Response):
        '''
        第一个返回回来的response
        :param response:
        :return:
        '''
        books = response.xpath('//div[@class="book"]')
        for book in books:
            novelImageUrl = book.xpath('.//img/@src').extract_first()
            novelId = book.xpath('.//div[@class="book_info"]/h3/a/@id').extract_first()
            novelName = book.xpath('.//div[@class="book_info"]/h3/a/text()').extract_first()
            novelLink = book.xpath('.//div[@class="book_info"]/h3/a/@href').extract_first()
            novelInfos = book.xpath('.//div[@class="book_info"]/dl/dd[@class="w_auth"]')
            if len(novelInfos) > 4:
                novelAuthor = novelInfos[0].xpath('./a/text()').extract_first()
                novelType = novelInfos[1].xpath('./a/text()').extract_first()
                novelStatus = novelInfos[2].xpath('./a/text()').extract_first()
                novelUpdateTime = novelInfos[3].xpath('./a/text()').extract_first()
                novelWords = novelInfos[4].xpath('./a/text()').extract_first()
            else:
                novelAuthor = ''
                novelType = ''
                novelStatus = ''
                novelUpdateTime = ''
                novelWords = ''
            bookListItem = YunqiBookListItem(novelImageUrl=novelImageUrl, novelId=novelId, novelName=novelName,
                                             novelLink=novelLink, novelAuthor=novelAuthor, novelType=novelType,
                                             novelStatus=novelStatus, novelUpdateTime=novelUpdateTime,
                                             novelWords=novelWords)
            yield bookListItem  # 交给 pipeline 去处理

            # TODO: 增加翻页的功能 解析下一页的小说数据
            request = scrapy.Request(url=novelLink, callback=self.parse_book_detail, meta={'novelId': novelId})
            yield request

    def parse_book_detail(self, response: Response):
        '''
        解析一本书的部分内容
        :param response: 每本书的细节
        :return:
        '''
        novelId = response.meta['novelId']
        novelLabel = response.xpath('.//div[@class="tags"]/text()').extract_first()

        novelAllClick = response.xpath('.//*[@id="novelInfo"]/table/tr[2]/td[1]/text()').extract_first()
        novelAllPopular = response.xpath('.//*[@id="novelInfo"]/table/tr[2]/td[2]/text()').extract_first()
        novelAllComm = response.xpath('.//*[@id="novelInfo"]/table/tr[2]/td[3]/text()').extract_first()

        novelMonthClick = response.xpath('.//*[@id="novelInfo"]/table/tr[3]/td[1]/text()').extract_first()
        novelMonthPopular = response.xpath('.//*[@id="novelInfo"]/table/tr[3]/td[2]/text()').extract_first()
        novelMonthComm = response.xpath('.//*[@id="novelInfo"]/table/tr[3]/td[3]/text()').extract_first()

        novelWeekClick = response.xpath('.//*[@id="novelInfo"]/table/tr[4]/td[1]/text()').extract_first()
        novelWeekPopular = response.xpath('.//*[@id="novelInfo"]/table/tr[4]/td[2]/text()').extract_first()
        novelWeekComm = response.xpath('.//*[@id="novelInfo"]/table/tr[4]/td[3]/text()').extract_first()

        novelCommentNum = response.xpath('.//*[@id="novelInfo_commentCount"]/text()').extract_first()
        bookDetailItem = YunqiBookDetailItem(novelId=novelId, novelLabel=novelLabel, novelAllClick=novelAllClick,
                                             novelMonthClick=novelMonthClick, novelWeekClick=novelWeekClick,
                                             novelAllPopular=novelAllPopular, novelMonthPopular=novelMonthPopular,
                                             novelWeekPopular=novelWeekPopular, novelCommentNum=novelCommentNum,
                                             novelAllComm=novelAllComm, novelMonthComm=novelMonthComm,
                                             novelWeekComm=novelWeekComm)
        yield bookDetailItem
