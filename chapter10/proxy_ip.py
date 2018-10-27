# -*- coding: utf-8 -*-
# @Time         : 2018/10/27 11:29
# @Author       : sodalife
# @File         : proxy_ip
# @Description  : 设置IP代理 频繁更换IP地址 会让服务器认为你是爬虫 需要不断的更换IP地址
# 从 github 上下载的代码下载
import requests
import json

# 向本地发一个请求 来获取免费获取的 IP地址
# 书上的代码有落后  github 上的代码
r = requests.get('http://127.0.0.1:8000/?types=0&count=5&country=国内') # 返回json数据
ip_ports = json.loads(r.text)
print(ip_ports)
ip = ip_ports[0][0] # 更新了 IP 地址
port = ip_ports[0][1]  # 找到了Ip地址

# 为 request 设置代理
proxies = {
    'http': f'http://{ip}:{port}',
    'https': f'http://{ip}:{port}'
}
r = requests.get('http://ip.chinaz.com/', proxies=proxies)
r.encoding = 'utf-8'
print(r.text)
