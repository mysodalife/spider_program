# -*- coding: utf-8 -*-
# @Time         : 2018/9/25 20:32
# @Author       : sodalife
# @File         : urllib_cookie.py
# @Description  :
from urllib import request
from http.cookiejar import CookieJar
url = 'https://www.baidu.com'
cookie = CookieJar() # 利用 CookieJar来管理 cookie 值
handler = request.HTTPCookieProcessor(cookie)
opener = request.build_opener(handler)
resp = opener.open(url)
cookieStr = ''
for item in cookie:
    cookieStr = cookieStr + item.name + ' = ' + item.value + ';'
print(cookieStr)

# 自己添加请求中的cookie 这里的request.urlopen 在底层调用的是
opener = request.build_opener()
opener.addheaders.append(('Cookie', 'email=' + 'xxxxxxxx@163.com'))
req = request.Request('http://www.zhihu.com')
response = opener.open(req, timeout=2)  # 这里传进去的参数可是是一个url 也可以是一个request的对象
print(response.getheaders())
retdata = response.read()
print(response.status)
