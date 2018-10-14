import os
from multiprocessing import Pool
import time
import random


def run_proc(name):
    print("Child process %s is running, pid is %s" % (name, os.getpid()))
    time.sleep(random.random() * 3)
    print("Child process %s ended, pid is %s" % (name, os.getpid()))


if __name__ == '__main__':
    print("Parent process %s is running " % (os.getpid(),))
    p = Pool(3)
    for i in range(56):
        p.apply_async(run_proc, args=(str(i),))
    print("Waiting for all the subprocess done.")
    p.close() # 在join之前执行 代表不能添加新的进程了
    p.join()
    print("All the process done.")
