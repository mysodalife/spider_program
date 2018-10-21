# -*- coding: utf-8 -*-
# @Time         : 2018/10/21 17:09
# @Author       : sodalife
# @File         : movie_htmldownloader.py
# @Description  : html 下载器
import requests


class HtmlDownloader(object):

    def downloader(self, url):
        if url is None:
            return
        user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
        headers = {'User-Agent': user_agent}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            response.encoding = 'utf-8'
            return response.text
        return None
