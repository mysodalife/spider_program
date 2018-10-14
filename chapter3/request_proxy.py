# -*- coding: utf-8 -*-
# @Time         : 2018/9/26 16:38
# @Author       : sodalife
# @File         : request_proxy.py
# @Description  : request 的代理
import requests

proxies = {  # 映射协议或主机名到 代理的URL
    'http': 'http://0.10.1.10:3128',
    'https': 'http://10.10.1.10:1080'
}
requests.get('http://example.org', proxies=proxies)
