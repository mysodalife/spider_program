# -*- coding: utf-8 -*-
# @Time         : 2018/9/17 20:10
# @Author       : sodalife
# @File         : thread_async.py
# @Description  : 线程同步
import threading

myLock = threading.RLock()
num = 0


class myThread(threading.Thread):

    def __init__(self, name):
        super(myThread, self).__init__(name=name)

    def run(self):
        global num  # 这个是共用的变量
        while True:
            myLock.acquire()
            print("%s Locked, number is %s " % (threading.current_thread().name, num))
            if num >= 4:
                myLock.release()
                print('%s released, number is %s' % (threading.current_thread().name, num))
                break
            num = num + 1
            print('%s released number is %s' % (threading.current_thread().name, num))
            myLock.release()


if __name__ == '__main__':
    t1 = myThread('thread1')
    t2 = myThread('thread2')
    t1.start()
    t2.start()
