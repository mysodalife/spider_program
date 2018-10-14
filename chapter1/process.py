from multiprocessing import Process
import os


def run_proc(name):
    print('Child process %s is running  pid: %s' % (name, os.getpid()))


if __name__ == '__main__':
    print("Parent process %s in running " % os.getpid())
    for i in range(5):
        process = Process(target=run_proc, args=(str(i),))
        print("Process will start")
        process.start()
    process.join()
    print("Process end.")

