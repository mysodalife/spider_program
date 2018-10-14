# -*- coding: utf-8 -*-
# @Time         : 2018/9/17 19:26
# @Author       : sodalife
# @File         : thread2.py
# @Description  : 继承 Threading中的类来实现线程
import time
import threading
import random


# 继承 threading.Thread 来实现线程类
class myThread(threading.Thread):
    def __init__(self, name, urls):
        super(myThread, self).__init__(name=name)
        self.urls = urls

    def run(self):
        print("Current %s is running" % (threading.current_thread().name,))
        for url in self.urls:
            print(' %s ------> %s' % (threading.current_thread().name, url))
            time.sleep(random.random())
        print(' %s running ended' % (threading.current_thread().name,))


print(' %s is running.' % (threading.current_thread().name,))
t1 = myThread(name='thread_1', urls=['Url_1', 'Url_2', 'Url_3'])
t2 = myThread(name='thread_2', urls=['Url_4', 'Url_5', 'Url_6'])
t1.start()
t2.start()
t1.join()
t2.join()
print('%s is running ' % threading.current_thread().name)
