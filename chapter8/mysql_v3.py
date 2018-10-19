# -*- coding: utf-8 -*-
# @Time         : 2018/10/19 17:21
# @Author       : sodalife
# @File         : mysql_v3.py
# @Description  : 连接远程的mysql 更新和删除数据
import pymysql.cursors

connect = pymysql.connect(host='222.199.193.65', user='root', password='duhan', port=3306, database='test',
                          charset='utf8')

cursor = connect.cursor()
try:
    cursor.execute('update person set name=%s where age=%s', ('cyan', 20))
    connect.commit()
    print('commit successfully.')
except Exception as e:
    print('fatel error.')
    connect.rollback()
finally:
    print('connect failed.')
    cursor.close()
    connect.close()
