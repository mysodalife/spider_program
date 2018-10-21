# -*- coding: utf-8 -*-
# @Time         : 2018/10/21 17:30
# @Author       : sodalife
# @File         : moive_htmlparser.py
# @Description  : 解析html
'''
1. 提前挡墙正在上映的电影
2. 从动态加载的链接中提前我们所需要的字段
'''

import re


class HtmlParser(object):

    def parse_url(self, response):
        pattern = re.compile(r'(http://movie.mtime.com/(\d+)/)')
        urls = pattern.findall(response)
        if urls is None:
            return None
        else:  # 注意到url 一定要去重
            return list(set(urls))

    def parser_json(self, page_url, response):
        '''
        解析相应
        :param page_url:
        :param response:
        :return:
        '''
