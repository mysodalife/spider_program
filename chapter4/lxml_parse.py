# -*- coding: utf-8 -*-
# @Time         : 2018/10/12 16:58
# @Author       : sodalife
# @File         : lxml_parse.py
# @Description  : 直接使用lxml 来解析库
from lxml import etree

html_str = """
<html>
    <head><title>The Dormouse's story</title></head>
    <body>
      <p class="title tail"><b>The Dormouse's story</b></p><p class="story">Once upon a time there were three little sisters; and their names were
      <a href="http://example.com/elsie" class="sister" id="link1"><!--Elsie--></a>
      <a href="http://example.com/lacie" class="sister" id="link2"><!--Lacie--></a> and
      <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
      and they lived at the bottom of a well.
      </p></body>
    <p class="story">...</p>
</html>
"""
# html = etree.HTML(html_str)  # 这里是直接读取的是 字符串
# result = etree.tostring(html)
# print(result)
#
# # 还可以直接读取 html 文件 利用 etree.parse 方法
#
# html = etree.HTML(html_str)
# result = etree.tostring(html, pretty_print=True)
# print(result)
# 抽取出其中所有的链接
html = etree.HTML(html_str)
urls = html.xpath('.//*[@class="sister"]/@href')
print(urls)