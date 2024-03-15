from multiprocessing import Process
import os
import time

def func():
    print('test function')
    print('ProcessId :',os.getpid())
    print('ParentsProcessId :', os.getppid())

if __name__ == "__main__":
    print('06.py ProcessID:', os.getpid())
    child1 = Process(target=func)
    child1.start()
    time.sleep(0.5)
    child2 = Process(target=func)
    child2.start()
    time.sleep(0.5)
    child3 = Process(target=func)
    child3.start()