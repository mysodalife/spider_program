# -*- coding: utf-8 -*-
# @Time         : 2018/10/14 16:31
# @Author       : sodalife
# @File         : HtmlParser.py
# @Description  : 爬虫节点的 html 解析器
import re
from urllib.request import urljoin
from bs4 import BeautifulSoup


class HtmlParser(object):

    def pareser(self, page_url, html_content):
        '''
        解析页面内容 抽取出各个部分的
        :param page_url: 待抽取的url
        :param html_content: 解析的 html 文档内容
        :return: 抽取的url 和 抽取的内容
        '''
        if page_url is None and html_content is None:
            return
        soup = BeautifulSoup(html_content, 'html.parser')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data

    def _get_new_urls(self, page_url: str, soup: BeautifulSoup):
        new_urls = set()
        root_url = page_url.split('/item')[0]
        links = soup.find_all('a', href=re.compile(r'^/item/[0-9a-zA-z%]+'), target='_blank')
        for link in links:
            new_url = link.get('href')
            new_full_url = urljoin(root_url, new_url)
            new_urls.add(new_full_url)
        return new_urls

    def _get_new_data(self, page_url: str, soup: BeautifulSoup):
        data = {}
        data['url'] = page_url
        title = soup.find('dd', class_='lemmaWgt-lemmaTitle-title').find('h1')
        data['title'] = title.string
        summary = soup.find('div', class_='lemma-summary')
        data['summary'] = summary.get_text()
        return data
