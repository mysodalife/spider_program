# -*- coding: utf-8 -*-
# @Time         : 2018/9/17 19:00
# @Author       : sodalife
# @File         : thread.py
# @Description  : 测试新的线程
import time
import random
import threading


def run_proc(urls):
    print('Current %s is running ' % (threading.current_thread().name,))
    for url in urls:
        print(' %s -----------> %s' % (threading.current_thread().name, url))
        time.sleep(random.random())
    print('%s ended.' % (threading.current_thread().name,))


print('%s is running....' % (threading.current_thread().name,))
t1 = threading.Thread(target=run_proc, name='Thread_1', args=(['Url_1', 'Url_2', 'Url_3'],))
t2 = threading.Thread(target=run_proc, name='Thread_2', args=(['Url_4', 'Url_5', 'Url_6'],))
t1.start()
t2.start()
t1.join()
t2.join()
print('%s ended.' % (threading.current_thread().name,))
