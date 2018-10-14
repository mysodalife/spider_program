# -*- coding: utf-8 -*-
# @Time         : 2018/9/22 8:06
# @Author       : sodalife
# @File         : TCP_Server.py
# @Description  : TCP server
import socket
import threading
import time


def deal_client(sock: socket, addr):
    print("Accept new connection from %s" % (addr,))
    sock.send(b'Hello I am Server')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        print('---> %s' % (data.decode('utf-8')))
        sock.send(("Loop_Msg %s ! " % (data.decode('utf-8'))).encode('utf-8'))
    sock.close()
    print("Connection from %s closed" % addr)


if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('127.0.0.1', 9999))
    s.listen(5)
    print("Waiting for connection")
    while True:
        sock, addr = s.accept()
        t = threading.Thread(target=deal_client, args=(sock, addr))
        t.start()
