# -*- coding: utf-8 -*-
# @Time         : 2018/9/25 19:28
# @Author       : sodalife
# @File         : urlib2.py
# @Description  : python http 请求中的 urllib 实现
from urllib import request

with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
    data = f.read()  # 读取返回内容
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s : %s' % (k, v))
    print('Data: ', data.decode('utf-8'))


# 如果想要模拟浏览器去访问对象 那么就需要用到 request
req = request.Request('http://www.douban.com/')
req.add_header('User-Agent',
               'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
with request.urlopen(req) as f:
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data: ', f.read().decode('utf-8'))


