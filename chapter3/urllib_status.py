# -*- coding: utf-8 -*-
# @Time         : 2018/9/25 21:14
# @Author       : sodalife
# @File         : urllib_status.py
# @Description  : 获取HTTP请求的状态码( 通过response 对象的 getcode() 或者 status属性)
from urllib import request
try:
    response = request.urlopen('http://www.google.com')
except request.HTTPError as e:
    if hasattr(e, 'code'):
        print('Error code', e.code)
