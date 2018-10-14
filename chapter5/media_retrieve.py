# -*- coding: utf-8 -*-
# @Time         : 2018/10/12 19:40
# @Author       : sodalife
# @File         : media_retrieve.py
# @Description  : 多媒体文件抽取 将多媒体文件下载到本地
import urllib
from lxml import etree
import requests


# 利用 urllib 的 urlretrieve 函数来实现多媒体文件的存取
# urllib.urlretrieve(url, filename, reporthook, data)
def schedule(blocknum, blocksize, totalsize):
   '''

   :param blocknum: 已经下载的数据块
   :param blocksize: 数据块的大小
   :param totalsize: 总大小
   :return:
   '''
   per = (blocknum * blocksize) / totalsize * 100.0
   if per > 100:
       per = 100
   print('当前下载进度是:', per)


User_Agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
headers = {'User-Agent':User_Agent}
response = requests.get('http://www.ivsky.com/tupian/ziranfengguang/', headers=headers)
html = etree.HTML(response.text)
srcList = html.xpath('.//img/@src')
i = 0
for src in srcList:
    urllib.request.urlretrieve(src, 'img' + str(i) + '.jpg', schedule)
    i = i + 1