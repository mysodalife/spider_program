# -*- coding: utf-8 -*-
# @Time         : 2018/10/12 21:22
# @Author       : sodalife
# @File         : Email.py
# @Description  : 构造邮件和发送邮件

# 构造邮件: email
# 发送邮件: smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import parseaddr, formataddr
import smtplib

# def _format_addr(s):
#     name, addr = parseaddr(s)
#     return formataddr((Header(name, 'utf-8').encode(), addr))
#
#
# from_addr = '17611259722@163.com'
# password = 'duhan404997294'
# to_addr = '404997294@qq.com'
# smtp_server = 'smtp.163.com'
# msg = MIMEText('python 爬虫出现异常, 错误状态吗： HTTP 404', 'plain', 'utf-8')  # 构造邮件消息
# msg['From'] = _format_addr('一号爬虫 <%s>' % from_addr)  # 发件人
# msg['To'] = _format_addr('管理员 <%s>' % to_addr)  # 收件人
# msg['Subject'] = Header('一号爬虫状态', 'utf-8').encode()  # 邮件主题
#
# # 发送邮件
# server = smtplib.SMTP(smtp_server, 25)  # 构造服务器
# server.login(from_addr, password)  # 登陆
# server.sendmail(from_addr, [to_addr], msg.as_string())


# 利用Python 内置的邮件模块来发送状态
from email.mime.text import MIMEText
from email.header import Header
from email.utils import parseaddr, formataddr
import smtplib


def _format_addr(s):
    name, addr = parseaddr(s)  # 一个是发件人的名字 邮件地址
    return formataddr((Header(name, 'utf-8').encode(), addr))


from_address = '17611259722@163.com'
password = 'duhan404997294'
to_address = '404997294@qq.com'
smtp_server = 'smtp.163.com'
# 这里设置成了纯文本的形式 如果是html 就把第二个改成 html即可
mime_text = MIMEText('spider run error HTTP Status:404', 'plain', 'utf-8')
mime_text['From'] = _format_addr('Node One <%s> ' % from_address)  # 设置发件人
mime_text['To'] = _format_addr('Admin One <%s>' % to_address)  # 设置收件人
mime_text['Subject'] = Header('Status report', 'utf-8')

# smtplib 来发送邮件
server = smtplib.SMTP(smtp_server, 25)  # 设置服务器地址和端口号
server.login(from_address, password=password)
server.sendmail(from_address, [to_address], mime_text.as_string())
