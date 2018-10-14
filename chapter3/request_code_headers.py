# -*- coding: utf-8 -*-
# @Time         : 2018/9/26 15:40
# @Author       : sodalife
# @File         : request_code_headers.py
# @Description  : 对请求码进行处理
import requests

result = requests.get('http://www.baidu.com/')
if result.status_code == requests.codes.ok:
    print(result.text)
    print(result.status_code)
    print(result.headers.get('Content-Type'))
else:
    result.raise_for_status()
