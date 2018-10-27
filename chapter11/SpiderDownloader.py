# -*- coding: utf-8 -*-
# @Time         : 2018/10/27 16:50
# @Author       : sodalife
# @File         : SpiderDownloader
# @Description  : 通过伪装成 移动端来爬取 酷我听书API的信息

import requests


# html 下载器
class SpiderDownloader(object):

    def download(self, url):
        if url is None:
            return
        User_Agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
        headers = {'User-Agent': User_Agent}
        response = requests.get(url=url, headers=headers)
        if response.status_code == 200:
            response.encoding = 'utf-8'
            return response.text
        return None
