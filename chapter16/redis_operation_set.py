# -*- coding: utf-8 -*-
# @Time         : 2018/11/6 16:18
# @Author       : sodalife
# @File         : redis_operation_set
# @Description  : 操作 redis中的 set 类型
import redis

r = redis.Redis(host='222.199.193.65', port=6379)

# sadd(names, values)
r.sadd('num', 33, 44, 55, 66)

# scard(name) 获取 name 对应的集合中的元素的个数
print(r.scard('num'))

# smembers(name) 获取到 name 对应的集合中的所有成员
print(r.smembers('num'))

r.sadd('num1', 1, 2, 3, 4, 5, 6)
r.sadd('num2', 5, 6, 7, 8, 9)
# sdiff(keys,*args) 获取多个 name 对应集合的差集
# sinter(keys, *args) 求多个集合的交集
# sunion(keys, *args) 求多个集合的并集
print(r.sdiff('num1', 'num2'))
print(r.sinter('num1', 'num2'))
print(r.sunion('num1', 'num2'))
