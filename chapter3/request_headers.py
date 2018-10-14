# -*- coding: utf-8 -*-
# @Time         : 2018/9/26 15:36
# @Author       : sodalife
# @File         : request_headers.py
# @Description  : 对请求头进行处理
import requests

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
headers = {'User-Agent': user_agent}
r = requests.get('http://www.baidu.com/', headers = headers)
print(r.content.decode('utf-8'))
