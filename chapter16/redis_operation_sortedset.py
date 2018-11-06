# -*- coding: utf-8 -*-
# @Time         : 2018/11/6 16:33
# @Author       : sodalife
# @File         : redis_operation_sortedset
# @Description  : redis的 sorted set 类型
import redis

r = redis.Redis(host='222.199.193.65')

# zadd(name, *args, **kwargs)
r.zadd('z_num', num1=11, num2=22, num3=33, num4=44)

# zcard(name) 获取到总个数
print(r.zcard('z_num'))

# zrange(name,start,end,desc=False, withscores=False, score_cast_func=float) 按照索引的范围来获取到 name 对应的有序集合的
# name sorted_set 的name
# start 有序集合的 起始位置 (并不是分数)
# end 有序集合的 结束位置 (并不是分数)
# desc 排序 默认是按照分数的 从小到大来排序
# withscores 是否携带分数 默认是不携带的
# score_cast_func 对分数进行转换的函数
print(r.zrange('z_num',start=0,end=2))

# zrem(name, values) 删除 name 对应的有序集合中 值是 values 的成员
r.zrem('z_num',['num1'])

# zscore(name, value) 获取到 value 对应的分数
print(r.zscore('z_num',"num1"))
