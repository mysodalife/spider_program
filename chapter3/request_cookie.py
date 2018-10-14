# -*- coding: utf-8 -*-
# @Time         : 2018/9/26 15:55
# @Author       : sodalife
# @File         : request_cookie.py
# @Description  : 设置cookie
import requests

r = requests.get('http://www.baidu.com')
# 这里是接收到的 cookie
for item in r.cookies.values():
    print(item)

# 设置成返回的 cookie 值
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
name = 'qiye'
headers = {'User-Agent': user_agent}
cookie = {'username': name, 'age': '10'}  # 必须传过去字符
result = requests.get('http://www.baidu.com', headers=headers, cookies=cookie)
print(result.text)
