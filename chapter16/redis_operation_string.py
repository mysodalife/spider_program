# -*- coding: utf-8 -*-
# @Time         : 2018/11/6 14:42
# @Author       : sodalife
# @File         : redis_operation_string
# @Description  : 使用 redis 操作string
from binascii import hexlify
import redis

r = redis.Redis(host='222.199.193.65', port=6379)

# set 键值对
# r.set('name', 'sodalife', ex=3)  # 过期时间是 3 秒
# print(r.get('name'))

# setnx 只有当name 不存在的时候才进行设置操作
# r.setnx('name', 'duhan')
# print(r.get('name'))

# setex 设置键值对 (name, value, time_secs)
# r.setex('age', '34', 1)
# print(r.get('age'))

# psetex (name, time_ms, value)
# 设置键值对
# r.psetex('name', 3000, 'duhan_sodalife')
# print(r.get('name'))
# time.sleep(4)
# print(r.get('name'))

# mset(*args,**kwargs) 批量设置
# r.mset(name='sodalife',age=20, country='China',address='hebei')
# print(r.get('country'))

# mget(keys, *args) 批量获取
# print(r.mget('age','country','address'))

# getset(name, value) 设置新的值，并且获取到原来的值
# print(r.getset('address','beijing'))

# getrange(key, start, end) # 根据字节获取到子字符串 ---> 汉字是3个字节 字母1个字节
# r.set('name', 'sodalife')
# print(r.getrange('name', 0, 0))

# setrange(name, offset, value) # 从指定的字符串来修改
# r.set('name', 'lebron james')
# r.setrange('name', 1, 'asdadasdad')  # offset 是偏移量
# print(r.get('name'))


# sbit(name, offset, value) 对 name 对应值进行二进制形式进行位操作
# r.set('name', 'qiye')
# print(bin(int(hexlify(r.get('name')), 16)))
# r.setbit('name', 2, 0) # 偏移量是2 进行设置为0
# print(bin(int(hexlify(r.get('name')),16)))

# getbit(name, offset) 获取到某一个位置的二进制
# print(r.getbit('name',1))

# bitcount(key,start=None, end=None) 获取到 name 对应值的二进制形式中的 1 的个数
# print(r.bitcount('name', start=0, end=1))
# print(r.get('name'))
# print(bin(int(hexlify(r.get('name')),16)))

# strlen(name) 获取到对应 name 的长度
# print(r.strlen('name'))

# append(name)
print(r.append('name',' sometimes it is handsome boy'))
print(r.get('name'))