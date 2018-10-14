# -*- coding: utf-8 -*-
# @Time         : 2018/9/26 14:04
# @Author       : sodalife
# @File         : urllib_proxy.py
# @Description  : 设置代理
from urllib import request
# 设置代理
proxy_handler = request.ProxyHandler({'http':'http://www.example.com:3128/'}) # 这个是代理吧
proxy_auth_handler = request.ProxyBasicAuthHandler()
proxy_auth_handler.add_password('realm', 'host', 'username', 'password')
opener = request.build_opener(proxy_handler,proxy_auth_handler)  # 可变参数
with opener.open('http://www.example.com/login.html') as f:
    pass