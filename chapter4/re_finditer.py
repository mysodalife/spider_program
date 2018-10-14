# -*- coding: utf-8 -*-
# @Time         : 2018/9/27 14:48
# @Author       : sodalife
# @File         : re_finditer.py
# @Description  : 匹配整个字符串 并且以迭代器的形式返回全部 Match对象
import re

pattern = re.compile(r'\d+')
matchiter = re.finditer(pattern, 'A1B2C3D4')
for match in matchiter:
    print(match.group())
