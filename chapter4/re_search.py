# -*- coding: utf-8 -*-
# @Time         : 2018/9/27 14:31
# @Author       : sodalife
# @File         : re_search.py
# @Description  :
import re
# re.search 函数会扫描整个字符串 而不像 match 函数一样只从开头匹配
pattern = re.compile(r'\d+')
result1 = re.search(pattern, 'abc192edf345')  # 得到返回结果就返回 并不返回所有的
if result1:
    print(result1.group())
else:
    print('match failure.')
