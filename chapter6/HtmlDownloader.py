# -*- coding: utf-8 -*-
# @Time         : 2018/10/13 10:56
# @Author       : sodalife
# @File         : HtmlDownloader.py
# @Description  : HTML 下载器 负责下载所需的网页
import requests


class HtmlDownloader(object):

    def download(self, url):
        if url is None:
            return None
        User_Agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
        headers = {'User-Agent': User_Agent}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            response.encoding = 'utf-8'
            return response.text
        return None
