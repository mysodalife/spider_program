from multiprocessing import Pipe,Process
import os
import time
import random


def send_proc(pipe,content):
    pass 


def recv_proc(pipe):
    pass

if __name__ == '__main__':
    print("Parent process is %s started." % (os.getpid(),))
    pipe = Pipe()
    send_process = Process(target = send_proc, args=())