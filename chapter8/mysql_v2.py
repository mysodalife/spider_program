# -*- coding: utf-8 -*-
# @Time         : 2018/10/19 16:15
# @Author       : sodalife
# @File         : mysql_v2.py
# @Description  : 远程连接mysql 并执行更新操作

import pymysql.cursors

connect = pymysql.connect(host='222.199.193.65', user='root', password='duhan', port=3306, charset='utf8',
                          database='test')
cursor = connect.cursor()  # 建立游标
try:
    cursor.execute('create table person(id int primary key not null auto_increment  ,name varchar (20), age int )')
    cursor.execute('insert into person(name ,age) values (%s)' % ('"qiye",20'))
    cursor.execute('insert into person(name ,age) values (%s, %s)', ('sodalife', 21))
    cursor.executemany('insert into person(name ,age) values (%s, %s)', [('duhan', 45), ('cyan', 18)])
    connect.commit()
    print('commit successfully.')
except Exception as e:
    print('fatel error.')
    connect.rollback()
finally:
    print('close connection')
    cursor.close()
    connect.close()
