# -*- coding: utf-8 -*-
# @Time         : 2018/9/20 20:35
# @Author       : sodalife
# @File         : taskWorker.py
# @Description  : 分布式进程当中的工作者进程
import time
from multiprocessing.managers import BaseManager


class QueueManager(BaseManager):
    pass


# register the queue
QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

Server_address = '127.0.0.1'
print(f"Connecting to the server {Server_address}")
manager = QueueManager(address=(Server_address, 8001), authkey='qiye'.encode('utf-8'))

manager.connect()

task = manager.get_task_queue()
result = manager.get_result_queue()
while not task.empty():
    image_url = task.get(True, timeout=10)
    print(f"run task download {image_url}....")
    time.sleep(1)
    result.put(f"{image_url} -----> success")

print('Worker exit.')
