# -*- coding: utf-8 -*-
# @Time         : 2018/10/14 13:34
# @Author       : sodalife
# @File         : ControlScheduler.py
# @Description  : 分布式爬虫的主节点控制调度器
from multiprocessing import Queue
from .URLManager import URLManager
from multiprocessing import Process
from .DataOutput import DataOutput
from multiprocessing.managers import BaseManager
import time

'''
url_queue: 管理进程 URL 传递给 爬虫节点
result_q: 爬虫节点将结果传递给 主节点
conn_q: 数据管理进程给 URL管理进程
store_q: 数据管理进程 将数据传递给 数据存储进程
'''


class NodeManager(object):

    def start_manager(self, url_q, result_q):
        BaseManager.register('get_task_queue', callable=lambda: url_q)
        BaseManager.register('get_result_queue', callable=lambda: result_q)
        manager = BaseManager(address=('', 8001), authkey='baike')
        return manager

    def url_manager_proc(self, url_q: Queue, conn_q: Queue, root_url: str):
        url_manager = URLManager()
        url_manager.add_new_url(root_url)
        while True:
            new_url = url_manager.get_new_url()
            url_q.put(new_url)
            print('old_url is ', url_manager.old_url_size())
            if len(url_manager.old_url_size() > 2000):
                url_q.put('end')
                print('控制节点发起结束')
                url_manager.save_progress('new_urls.txt', data=url_manager.new_urls)
                url_manager.save_progress('old_urls.txt', data=url_manager.old_urls)
                return
            # 从 conn_q 取得新的 URL
            try:
                if not conn_q.empty():
                    new_urls = conn_q.get()
                    url_manager.add_new_urls(new_urls)
            except BaseException as e:
                time.sleep(0.5)

    def result_reslove_proc(self, result_q: Queue, store_q: Queue, conn_q: Queue):
        while True:
            try:
                if not result_q.empty():
                    content = result_q.get(True)
                    if content['new_urls'] == 'end':
                        print('结果分析进程，然后结束')
                        store_q.put('end')
                        return
                    conn_q.put(content['new_urls'])
                    store_q.put(content['data'])
                else:
                    time.sleep(0.1)
            except BaseException as e:
                time.sleep(0.1)

    def store_proc(self, store_q: Queue):
        output = DataOutput()
        while True:
            if not store_q.empty():
                data = store_q.get()
                if data == 'end':
                    print('存储进程接受到通知, 结束')
                    output.output_end(output.filepath)
                    return
                output.store_data(data=data)
            else:
                time.sleep(0.1)


if __name__ == '__main__':
    url_q = Queue()
    result_q = Queue()
    conn_q = Queue()
    store_q = Queue()
    mainnode = NodeManager()
    manager = mainnode.start_manager(url_q=url_q, result_q=result_q)
    url_manager_proc = Process(target=mainnode.url_manager_proc, args=(
    url_q, conn_q, 'https://baike.baidu.com/item/%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB/5162711?fr=aladdin'))
    result_reslove_proc = Process(target=mainnode.result_reslove_proc, args=(result_q, store_q, conn_q))
    store_proc = Process(target=mainnode.result_reslove_proc, args=(store_q,))
    url_manager_proc.start()
    result_reslove_proc.start()
    store_proc.start()
    manager.get_server().server_forever()
