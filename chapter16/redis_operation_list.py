# -*- coding: utf-8 -*-
# @Time         : 2018/11/6 15:54
# @Author       : sodalife
# @File         : redis_operation_list
# @Description  : 来操作 list 类型
import redis

r = redis.Redis(host='222.199.193.65', port=6379)

# lpush(name, values) 每次新添加的内容放到列表的最左边， 添加到右边是 rpush
r.lpush('digit', 11, 22, 33)

# linsert(name, where, refvalue, value)
# name 对应的列表里面的某一个值 的前和后 插入一个新的值
r.linsert('digit', 'after', '22', '44')

# lset(name, index, value) 对某个索引进行赋值
r.lset('digit', 4, 44)

# lrem(name, value, num) 在 name 对应的list 中删除的值 num 代表第几次出现的时候 num = 0时 删除所有的指定值
r.lrem('digit', '22', 1)

# lpop(name) 从左侧返回第一个元素 移除并返回
r.lpop('digit')
