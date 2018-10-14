# -*- coding: utf-8 -*-
# @Time         : 2018/9/21 19:32
# @Author       : sodalife
# @File         : UDP_Server.py
# @Description  : UDP_Server
import socket

# step1: create the socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# step2: bind the ip address
s.bind(('127.0.0.1', 9999))
print('Bind UDP on 9999')
while True:
    data, addr = s.recvfrom(1024)
    print("Receive from %s : %s" % (addr, data))
    s.sendto(b'Hello, %s' % (data,), addr)
