# -*- coding: utf-8 -*-
# @Time         : 2018/11/5 17:35
# @Author       : sodalife
# @File         : bloomFilter
# @Description  : 布隆过滤器
from pybloom_live import BloomFilter
from pybloom_live import ScalableBloomFilter # 动态扩展的布隆过滤器
f = BloomFilter(capacity=1000, error_rate=0.001)
m = [ f.add(x) for x in range(10)]
print( 11 in f)
print( 4 in f)

# 动态扩展的容器
sbf = ScalableBloomFilter(mode=ScalableBloomFilter.SMALL_SET_GROWTH)
count = 10000
for i in range(0,count):
    sbf.add(i)
print(10001 in sbf)
print(4 in sbf)