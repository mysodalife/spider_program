# -*- coding: utf-8 -*-
# @Time         : 2018/9/27 14:39
# @Author       : sodalife
# @File         : re_findall.py
# @Description  : 找到所有匹配的子串
import re
pattern = re.compile(r'\d+')
print(re.findall(pattern, 'A1B2C3D4'))  # 返回list
