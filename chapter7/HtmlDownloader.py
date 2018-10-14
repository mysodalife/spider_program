# -*- coding: utf-8 -*-
# @Time         : 2018/10/14 16:17
# @Author       : sodalife
# @File         : HtmlDownloader.py
# @Description  : 爬虫节点的
import requests
class HtmlDownloader(object):

    def download(self,url):
        if url is None:
            return
        user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
        header = {'User-Agent':user_agent}
        response = requests.get(url=url, headers=header)
        if response.status_code == 200:
            response.encoding = 'utf-8'
            return response.text
        return None