# -*- coding: utf-8 -*-
# @Time         : 2018/9/26 16:11
# @Author       : sodalife
# @File         : request_session.py
# @Description  : request的 sesssion
import requests

# 如果希望每次请求像浏览器一样， 自动加cookie 就需要用到 session
# 在连续访问网页 和处理登录请求时常用
s = requests.Session()
login_url = 'http://www.baidu.com/login'
r = s.get(login_url, allow_redirects=True)  # 先获取到整个默认的cookie
datas = {'name': 'qiye', 'password': 'qiye'}
result = s.post(login_url, data=datas, allow_redirects=True)
print(result.text)
