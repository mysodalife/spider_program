# -*- coding: utf-8 -*-
# @Time         : 2018/10/27 15:05
# @Author       : sodalife
# @File         : cookie_login
# @Description  : 使用 cookie 来登录
# 这个文件 我们可以使用 cookie来登录
import pickle  # 将对象序列化
import requests


# 保留 cookie 下次登陆的时候再使用
# 这里用到 session 在连续访问网页 处理登录跳转时很方便
def save_session(session: requests.Session):
    '''
    将session写入到文件中去
    :param session: 会话
    :return:
    '''
    with open('session.txt', 'wb') as f:
        pickle.dump(session.headers, f)
        # 将 session.cookies 获取到 并保存到整个 txt文件中
        pickle.dump(session.cookies.get_dict(), f)
        # 将session 写入到文件中


def load_session():
    '''
    从文件中加载对象 然后返回
    :return:
    '''
    with open('session.txt', 'rb') as f:
        headers = pickle.load(f)
        cookie = pickle.load(f)
        return headers, cookie
