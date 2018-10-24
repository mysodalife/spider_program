# -*- coding: utf-8 -*-
# @Time         : 2018/10/12 15:05
# @Author       : sodalife
# @File         : beautifulsoup_namedtuple.py
# @Description  : 命名 元组
from collections import namedtuple
import csv

# with open('qiye.csv', 'r') as f:
#     f_csv = csv.reader(f)
#     headers = next(f_csv)
#     Row = namedtuple('Row', headers)  # 命名元组 返回一个tuple的子类 带有名称 类的名字是 Row   headers 提供了头的名称
#     for r in f_csv:
#         row = Row(*r)  # 创建一个 Row 实例 名字是
#         print(row.Name, row.Password)
#         print(row)

with open('qiye.csv', 'r') as f:
    reader = csv.DictReader(f)  # 获取到整个的dict对象
    for line in reader:
        print(line.get('Name'), line.get('Password'))

