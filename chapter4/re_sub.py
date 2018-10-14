# -*- coding: utf-8 -*-
# @Time         : 2018/9/27 14:53
# @Author       : sodalife
# @File         : re_sub.py
# @Description  : re.sub(pattern, repl, string[,count]) 使用 repl 来替换 string 每一个匹配的字符串
import re

p = re.compile(r'(?P<word1>\w+)  (?P<word2>\w+)')
s = 'i say, hello  world!'
result = re.sub(p, r'\g<word2>  \g<word1>', s)
print(result)
result2 = re.sub(p, r'\2  \1', s)
print(result2)


def func(match):
    return match.group(2).title()  +  '  '  +  match.group(1).title()   # 返回的字符串中不能包含组号了


result3 = re.sub(p, func, s)
print(result3)
