# -*- coding: utf-8 -*-
# @Time         : 2018/9/20 21:00
# @Author       : sodalife
# @File         : taskManager.py
# @Description  : Windows 下的服务进程
import queue
from multiprocessing.managers import BaseManager
from multiprocessing import freeze_support

task_number = 10

# create the task queue
task_queue = queue.Queue(task_number)
result_queue = queue.Queue(task_number)


def get_task():
    return task_queue


def get_result():
    return result_queue


class QueueManager(BaseManager):
    pass


def win_run():
    # register the task queue and result queue
    QueueManager.register('get_task_queue', callable=get_task)
    QueueManager.register('get_result_queue', callable=get_result)
    manager = QueueManager(address=('127.0.0.1', 8001), authkey='qiye'.encode('utf-8'))
    manager.start()
    try:
        task = manager.get_task_queue()
        result = manager.get_result_queue()
        for img_url in ['Image_url' + str(i) for i in range(10)]:
            print(f"Put task {img_url}")
            task.put(f"put task {img_url}")
        print('try to get result')
        for i in range(10):
            print(f"result is %s" % (result.get()))
    except:
        print("Manager error.")
    finally:
        manager.shutdown()


if __name__ == '__main__':
    freeze_support()
    win_run()
