# -*- coding: utf-8 -*-
# @Time         : 2018/10/19 16:15
# @Author       : sodalife
# @File         : mysql_v2.py
# @Description  : 远程连接mysql 并执行更新操作

import pymysql.cursors

connect = pymysql.connect(host='222.199.193.65', user='root', password='duhan', port=3306, charset='utf8',
                          database='test')
cursor = connect.cursor()
# try:
#     cursor.execute('create table person(id primary key not null auto_increment int ,name varchar (20), age int )')
#     cursor.execute('insert into person(name,age) values(%s) ' % ('"qiye", 20',))
#     cursor.execute('insert into person(name,age) values (%s, %d)', ('qiye', 20))
#
#     # 使用 executemany 多个语句
#     cursor.executemany('insert into person(name,age) values (%s, %d)', [('marry', 20), ('jack', 20)])
#     connect.commit()
#     print('commit successfully.')
# except Exception as e:
#     print('fatel error.')
#     connect.rollback()
# finally:
#     print('close connection')
#     cursor.close()
#     connect.close()
try:
    cursor.execute('create table person(id int primary key not null auto_increment  ,name varchar (20), age int )')
    # cursor.execute('insert into person(name,age) values(%s) ' % '"qiye",20')
    # cursor.execute('insert into person(name ,age )values (%s, %d)' % ('qiye', 20))
    connect.commit()
    print('commit successfully.')
except Exception as e:
    print('fatel error.')
    connect.rollback()
finally:
    print('close connection')
    cursor.close()
    connect.close()
