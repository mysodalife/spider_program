# -*- coding: utf-8 -*-
# @Time         : 2018/10/21 15:37
# @Author       : sodalife
# @File         : mongodb_v1.py
# @Description  : Python操作mongodb
import mongoengine as me

me.connection.disconnect()
# 这里测试一下指定一下数据库 账户名 密码 IP地址 端口号
# 需要在配置一下MongoDB的远程登录
me.connect('pythonSpider', host='222.199.193.65', port=27017, username='sodalife', password='duhan')


class python(me.DynamicDocument):
    def __init__(self, version: float, description: str):
        super(python, self).__init__()
        self.version = version
        self.description = description

    version = me.FloatField()
    description = me.StringField(max_length=25)


data = python(version=1.0, description='first commit')
data.value = "hello world"
data.save()
