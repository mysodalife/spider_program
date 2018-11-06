# -*- coding: utf-8 -*-
# @Time         : 2018/11/6 15:30
# @Author       : sodalife
# @File         : redis_operation_hash
# @Description  : 操作 redis 的 hash 类型的数据
import redis

r = redis.Redis(host='222.199.193.65', port=6379)
# hash

# hset(name, key value) name field value
# r.hset('student', 'name', 'qiye')

# hmset(name, mapping) 设置多个值  mapping 字典
# r.hmset('student', {'name': 'qiye', 'age': 20})

# hget(name, key) 获取到 name 中的 key
# print(r.hget('student', 'age'))
# hmget(name, keys, *args)
# name -> name
# keys -> 要获取的keys 的集合  list类型
# *args -> 要获取的key 如： k1, k2 , k3

print(r.hmget('student', 'age', 'name'))
print(r.hmget('student', ['name', 'age']))
