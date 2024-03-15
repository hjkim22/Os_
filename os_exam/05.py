from multiprocessing import Process
import os

def func():
    print('test function')
    print('ProcessId :',os.getpid())
    print('ParentsProcessId :', os.getppid())

if __name__ == "__main__":
    print('05.py ProcessID:', os.getpid())
    child = Process(target=func).start()