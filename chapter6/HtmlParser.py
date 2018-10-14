# -*- coding: utf-8 -*-
# @Time         : 2018/10/13 11:02
# @Author       : sodalife
# @File         : HtmlParser.py
# @Description  : HTML 解析器
import re
from bs4 import BeautifulSoup
from urllib.parse import urljoin


class HtmlParser(object):

    def parser(self, page_url, html_content):
        '''
        :param page_url: 当前页面的url
        :param html_content: html 下载器返回的内容
        :return: 返回URL和数据
        '''
        if page_url is None or html_content is None:
            return
        soup = BeautifulSoup(html_content, 'html.parser')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data

    def _get_new_urls(self, page_url:str, soup:BeautifulSoup):
        '''

        :param page_url: 页面的url
        :param soup: beautifulsoup 对象
        :return: 最新的url
        '''
        new_urls = set()
        links = soup.find_all('a', href=re.compile(r'^/item/[0-9a-zA-z%]+'), target='_blank')
        for link in links:
            new_url = link.get('href')
            root_url = page_url.split('/item')[0]
            new_full_url = urljoin(root_url, new_url)
            new_urls.add(new_full_url)
        return new_urls

    def _get_new_data(self, page_url, soup):
        '''
        :param page_url: 页面的url
        :param soup: beautifulsoup 对象
        :return: 最新的数据
        '''
        data = {}
        data['url'] = page_url
        title = soup.find('dd', class_='lemmaWgt-lemmaTitle-title').find('h1')
        data['title'] = title.string
        summary = soup.find('div', class_='lemma-summary')
        data['summary'] = summary.get_text()
        return data