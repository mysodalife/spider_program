# -*- coding: utf-8 -*-
# @Time         : 2018/9/26 14:21
# @Author       : sodalife
# @File         : requests_post.py
# @Description  : 利用 requests 实现POST 请求
import requests
postdata = {'username': 'username', 'password': 'password'}
requests.post('http://www.example.com/login', data=postdata)
