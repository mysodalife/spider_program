# -*- coding: utf-8 -*-
# @Time         : 2018/9/26 16:30
# @Author       : sodalife
# @File         : request_redirect.py
# @Description  : request 的重定向
import requests

# 只需要设置 requests的 get 和 POST 设置 allow_redirects为 True 和 False
s = requests.get('http://www.github.com', allow_redirects=True)

# 通过 s.history 查看所有重定向之前的地址
print(s.history)  # 有 2个重定向
print(s.url)
print(s.status_code)
