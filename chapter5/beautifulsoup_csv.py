# -*- coding: utf-8 -*-
# @Time         : 2018/10/12 11:37
# @Author       : sodalife
# @File         : beautifulsoup_csv.py
# @Description  : csv 文件来存储
import csv
import requests
import chardet
import re
from lxml import etree

User_Agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
headers = {'User-Agent': User_Agent}
response = requests.get('http://seputu.com', headers=headers)
response.encoding = chardet.detect(response.content)['encoding']
html = etree.HTML(response.text)
mulus = html.xpath('.//div[@class="mulu"]')
pattern = re.compile(r'\s*\[(.*)\]\s+(.*)')
rows = []
for mulu in mulus:
    h2_text = mulu.xpath('.//h2/text()')
    if len(h2_text) > 0:
        title = h2_text[0]
        print(title.encode('utf-8'))
        a_s = mulu.xpath('./div[@class="box"]/ul/li/a')
        for a in a_s:
            href = a.xpath('./@href')[0]
            box_title = a.xpath('./@title')[0]
            match = re.search(pattern, box_title)
            if match is not None:
                date = match.group(1)  # bytes 转 str
                real_title = match.group(2)
                content = [title, real_title, href, date]
                rows.append(content)
headers = ['title', 'read_title', 'href', 'date']
with open('qiye.csv', 'w', newline='') as f:
    f_csv = csv.writer(f)
    f_csv.writerow(headers)
    f_csv.writerows(rows)
