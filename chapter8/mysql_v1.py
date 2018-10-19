# -*- coding: utf-8 -*-
# @Time         : 2018/10/19 16:02
# @Author       : sodalife
# @File         : mysql.py
# @Description  : 远程连接mysql 执行查询sql语句

'''
连接远程主机的上的 Mysql（版本8.0）
远程主机IP地址：222.199.193.65
attention： 这里在执行 sql 语句时一定要执行
'''
import pymysql.cursors

connect = pymysql.connect(host='222.199.193.65', user='root', password='duhan', database='test', port=3306,
                          charset='utf8')
cursor = connect.cursor()
cursor.execute('select * from student')
result = cursor.fetchall()
print(result)
cursor.close()
connect.close()