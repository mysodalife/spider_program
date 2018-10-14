# -*- coding: utf-8 -*-
# @Time         : 2018/9/25 21:23
# @Author       : sodalife
# @File         : urllib_redirect.py
# @Description  : 检查是否是重定向 只需要查看 request 和 response 的 url 是否是一致的就可以了
from urllib import request
req = request.Request('http://www.zhihu.com')
# 伪装成 chrome 浏览器
req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36')
response = request.urlopen(req)
print(response.geturl())

# 如果不想自动重定向 可以自定义 HTTPRedirectHandler 类


class RedirectHandler(request.HTTPRedirectHandler):

    def http_error_302(self, req, fp, code, msg, headers):
        result = request.HTTPRedirectHandler.http_error_301(self, req, fp, code, msg, headers)
        result.status = code
        result.newurl = result.geturl()
        return result


opener = request.build_opener(RedirectHandler)
opener.open('http://www.zhihu.com')