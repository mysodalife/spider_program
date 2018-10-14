# -*- coding: utf-8 -*-
# @Time         : 2018/9/27 14:35
# @Author       : sodalife
# @File         : re_split.py
# @Description  : 按照匹配的字符串将string 分割
import re
pattern = re.compile(r'[a-zA-z]')
result = re.split(pattern, 'G20178700')
print(result)
