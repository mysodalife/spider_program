from multiprocessing import Process, Queue
import os
import time, random


def put_proc(q, urls):
    print("Child putting process %s started. " % (os.getpid(),))
    for url in urls:
        q.put(url)
        print('Putting %s to queue.' % (url,))
        time.sleep(random.random() * 3)


def get_proc(q):
    print("Child reading process %s started." % (os.getpid(),))
    while True:
        url = q.get(True)
        print("Getting from queue is %s " % (url,))


if __name__ == '__main__':
    print("Parent process is started %s " % (os.getpid()))
    queue = Queue()
    process_writer1 = Process(target=put_proc, args=(queue, ['url1', 'url2', 'url3', 'url4']))
    process_writer2 = Process(target=put_proc, args=(queue, ['url5', 'url6', 'url7', 'url8']))
    process_reader3 = Process(target=get_proc, args=(queue,))
    process_writer1.start()
    process_writer2.start()
    process_reader3.start()
    process_writer1.join()
    process_writer2.join()
    process_reader3.terminate() # 手动结束读进程
