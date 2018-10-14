# -*- coding: utf-8 -*-
# @Time         : 2018/10/14 16:31
# @Author       : sodalife
# @File         : HtmlParser.py
# @Description  : 爬虫节点的 html 解析器
from bs4 import BeautifulSoup


class HtmlParser(object):

    def pareser(self, page_url, html_content):
        soup = BeautifulSoup(html_content, 'html.parser')

    def _get_new_urls(self, page_url: str, soup: BeautifulSoup):
        pass

    def _get_new_data(self, page_url: str, soup: BeautifulSoup):
        pass
