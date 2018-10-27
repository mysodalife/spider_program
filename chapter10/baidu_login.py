# -*- coding: utf-8 -*-
# @Time         : 2018/10/26 10:12
# @Author       : sodalife
# @File         : baidu_login.py
# @Description  : 模拟登陆百度云 这里涉及到加密数据的处理
import base64
import json
import re
from urllib.request import quote
import requests
import time
import PyV8 # python 中执行js 代码
from crypto.Cipher import PKCS1_v1_5
from crypto.PublicKey import RSA

# 没必要用到 selenium 直接就是发请求 得到返回结果
if __name__ == '__main__':
    # 这里创建一个会话，每次请求时都需要自动加 cookie 可用于登陆请求
    s = requests.Session()
    s.get('http://yun.baidu.com')
    # 下面这是简单的粘贴了 原始的js 代码 并没有改变 加载原网站的 js 脚本并执行
    js = '''
        function callback(){
           return 'bd__cbs__' + Math.floor(2147483648 * Math.random()).toString(36);
        }
        function gid(){
          return 'xxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g,function(e){
             var t = 16 * Math.random() | 0;
             n =  'x' == e ? t : 3 & t | 8;
             return n.toString(16);
          }).toUpperCase();
        }
    '''
    # PyV8 就是让执行浏览器自带的脚本语言
    ctxt = PyV8.JSContext()
    ctxt.eval(js)