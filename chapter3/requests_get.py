# -*- coding: utf-8 -*-
# @Time         : 2018/9/26 14:17
# @Author       : sodalife
# @File         : requests_get.py
# @Description  : 利用 requests 实现
import requests
import chardet

response = requests.get('https://www.baidu.com')
print(response.url)
print(response.content)

# 实现一下带参数的 get 请求
get_params = {'keyword': 'keyword', 'index': 1}
result = requests.get('https://www.baidu.com', params=get_params)
print(result.content.decode('utf-8'))  # r.content 是一个字节形式 r.text 是一个文本形式
print(result.encoding)
print(result.url)

# 返回的 result.encode 是根据返回的头进行编码进行猜测的
r = requests.get('https://www.baidu.com')
r.encoding = chardet.detect(r.content)['encoding']
print(r.text)

# result.get 是一次性返回所有的结果               stream = True 字节流读取
result = requests.get('http://www.baidu.com/', stream=True)  #以流的方式进行读取的字节流
print(result.raw.read(10))
