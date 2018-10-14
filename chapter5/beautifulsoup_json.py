# -*- coding: utf-8 -*-
# @Time         : 2018/10/12 9:26
# @Author       : sodalife
# @File         : beautifulsoup_json.py
# @Description  : 爬取 seputu.com 的数据 并存储为 json
import requests
import chardet
from bs4 import BeautifulSoup
import json

userAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
headers = {'User-Agent': userAgent}
response = requests.get('http://seputu.com', headers=headers)
encoding = chardet.detect(response.content)['encoding']
response.encoding = encoding  # 猜测返回内容的编码
soup = BeautifulSoup(response.text, 'html.parser', from_encoding=encoding)

file_content = []
for content in soup.find_all('div', class_='mulu'):
    title = content.select('center h2')
    if len(title) > 0:
        print(title[0].string)
        list = []
        chapter_list = content.select('div.box ul li a')
        for chapter in chapter_list:
            href = chapter.get('href')
            box_title = chapter.get('title')
            list.append({'href': href, 'box_title': box_title})
        file_content.append({'title': title[0].string, 'content': list})
with open('qiye.json', 'w') as fp:
    json.dump(file_content, fp=fp, indent=4)

# Python使用 unicode 进行编码
