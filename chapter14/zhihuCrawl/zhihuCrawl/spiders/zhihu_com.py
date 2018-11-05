# -*- coding: utf-8 -*-
from scrapy import Spider
from scrapy import Request
from ..items import UserInfoItem, RelationItem
import json
import re


class ZhihuSpider(Spider):
    name = 'zhihu.com'
    allowed_domains = ['zhihu.com']
    start_urls = ['https://www.zhihu.com/people/qi-ye-59-20/activities']
    cookies = {
        '_xsrf': 'ETe5Rm74CIQSYjRuK3RTBgY3t0oGLb00',
        '_zap': '093ea483-06f9-48c6-bdc3-edd3afd396b4',
        'capsion_ticket': '2|1:0|10:1541063529|14:capsion_ticket|44:ZTgzYzRhYzJiYjM1NGJiZThhZjIzNDc4YWY2NTI0MTE=|dd4a0714ba81c49febabf076dfc6d948748fac6df1eee23bb154bf6ab8877809',
        'd_c0': 'ACAoHXy2cw6PTk8RlPNCjCtHxQfctvrYQvQ=|1541063525',
        'q_c1': '5ec552549b124d3392d1902f828cb70c|1541063548000|1541063548000',
        'tgw_l7_route': 'b3dca7eade474617fe4df56e6c4934a3',
        'tst': 'f',
        'z_c0': '2|1:0|10:1541063546|4:z_c0|92:Mi4xM2l0dkJ3QUFBQUFBd0djTWZMWnpEaVlBQUFCZ0FsVk5laEhJWEFERnE2azlyRkZYU3I4cEZIM3d4LUd4UUpaUVFn|e64c2f8b4849805cb95498324820c5d47359e199b2e1f31b200064ef8c3ac7d9'
    }

    def start_requests(self):
        '''
        最开始从这个函数产生 request
        :return:
        '''
        for url in self.start_urls:
            yield Request(url=url, cookies=self.cookies, callback=self.parse)

    def parse(self, response):
        '''
         用户头像链接： //img[@class="Avatar Avatar--large UserAvatar-inner"]/@src
         用户昵称：//span[@class="ProfileHeader-name"]/text()
         用户简介：//span[@class="RichText ztext ProfileHeader-headline"]/text()
         关注的数量： //*[@id="root"]/div/main/div/div[2]/div[2]/div[2]/div/a[1]/div/strong/text()
         被关注的数量： //*[@id="root"]/div/main/div/div[2]/div[2]/div[2]/div/a[2]/div/strong/text()
         关注者的页面链接：//*[@id="root"]/div/main/div/div[2]/div[2]/div[2]/div/a[1]/@href
         被关注者的页面链接：//*[@id="root"]/div/main/div/div[2]/div[2]/div[2]/div/a[2]/@href
        '''
        # 下面开始解析数据 从请求解析中获得我们想要的数据
        user_id = response.url.split('/')[-2]
        user_image_url = response.xpath('//img[@class="Avatar Avatar--large UserAvatar-inner"]/@src').extract()[0]
        name = response.xpath('//span[@class="ProfileHeader-name"]/text()').extract()[0]
        description = response.xpath('//span[@class="RichText ztext ProfileHeader-headline"]/text()').extract()[0]
        followees_num = \
            response.xpath('//*[@id="root"]/div/main/div/div[2]/div[2]/div[2]/div/a[1]/div/strong/text()').extract()[
                0]  # 关注了多少人
        followers_num = \
            response.xpath('//*[@id="root"]/div/main/div/div[2]/div[2]/div[2]/div/a[2]/div/strong/text()').extract()[
                0]  # 粉丝有多少
        relations_urls = response.xpath('//a[@class="Button NumberBoard-item Button--plain"]/@href').extract()

        # 构造一下 useritem 返回 item
        user_info_item = UserInfoItem(user_id=user_id, user_image_url=user_image_url, name=name,
                                      description=description, followees_num=followees_num, followers_num=followers_num)
        yield user_info_item  # 这里已经将整个用户的 item 提取出来

        # 这里根据关系的类型 构造 url 来发送请求
        for url in relations_urls:  # 在这里判断一下是关注还是被关注
            if 'following' in url:
                relation_type = 'following'
            else:
                relation_type = 'followers'
            yield Request(url=response.urljoin(url=url), errback=self.parse_err, callback=self.parse_relation, meta={
                'user_id': user_id,
                'relation_type': relation_type,
                'dont_merge_cookies': True,  # 不要将现有的cookie 进行合并
            })  # 这里产生请求继续跟进请求

    def parse_err(self, response):
        self.logger.error("some error has occurred in your spdier.")

    def parse_relation(self, response):
        '''
        这里重新提交一下请求
        :param response:
        :return:
        '''
        meta_info = response.meta  # 获取到元数据
        user_id = meta_info['user_id']  # 获取到 用户名
        relation_type = meta_info['relation_type']  # 获取到关系的类型
        if relation_type == 'following':
            url = 'https://www.zhihu.com/api/v4/members/qi-ye-59-20/followees?include=data%5B*%5D.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics&offset=0&limit=20'
        else:
            url = 'https://www.zhihu.com/api/v4/members/qi-ye-59-20/followers?include=data%5B*%5D.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics&offset=0&limit=20'
        yield Request(url=url, errback=self.parse_err, callback=self.parse_relation_json, meta={
            'relation_type': relation_type,
            'dont_merge_cookies': True,
            'user_id': user_id,
        })

    def parse_relation_json(self, response):
        '''
        对返回来的 json 数据进行转化
        :param response:
        :return:
        '''
        user_id = response.meta.get('user_id')
        relation_type = response.meta.get('relation_type')  # 是什么类型的
        ts = json.loads(response.text)  # 获取到json 数据
        paging = ts.get('paging')
        data = ts.get('data')
        for person in data:
            relation = RelationItem(user_id=user_id, relation_type=relation_type, relations_id=person.get('id'))
            yield relation
        if paging['is_end'] is False:
            # 最后一个了， 也就不需要进行再次发送请求了
            # 这里说明后面还有 改变一下offset 就行了
            pattern = re.compile(r'offset=(\d+)')
            current_offset = pattern.findall(response.url)  # 获取到当前的偏移量
            current_offset = int(current_offset[0])
            # self.logger.error('**************' + str(current_offset))
            current_offset = current_offset + 20
            # self.logger.error('**************' + str(current_offset))
            rsp_url = response.url
            rsp_url = re.sub(pattern, 'offset=' + str(current_offset), rsp_url)
            self.logger.error('+++++++++++++++++++++' + rsp_url)
            req = Request(url=rsp_url, errback=self.parse_err, callback=self.parse_relation_json, meta={
                'relation_type': relation_type,
                'dont_merge_cookies': True,
                'user_id': user_id,
            })
            yield req
