# -*- coding: utf-8 -*-
# @Time         : 2018/9/27 14:07
# @Author       : sodalife
# @File         : re_instance.py
# @Description  : 测试一下正则表达式模块
import re

pattern = re.compile(r'\d+')  # 获取Pattern 实例
result1 = re.match(pattern, '192abc')  # 如果返回字符串 如果失败 返回 None
if result1:
    print(result1.group())
else:
    print('match failure.')
result2 = re.match(pattern, 'abc192')  # 返回匹配的结果 从开头就不符合 就直接返回None
if result2:
    print(result2.group())
else:
    print('match failure2.')
