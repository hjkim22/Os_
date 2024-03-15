from multiprocessing import Process
import os
import time

def coke():
    print("CokeProcessId :", os.getpid())
    print("ParentsProcessId :", os.getppid())

def cider():
    print("ciderProcessId :", os.getpid())
    print("ParentsProcessId :", os.getppid())

def juice():
    print("JuiceProcessId :", os.getpid())
    print("ParentsProcessId :", os.getppid())

if __name__ == "__main__":
    print('07.py ProcessID:', os.getpid())
    child1 = Process(target=coke)
    child1.start()
    time.sleep(0.5)
    child2 = Process(target=cider)
    child2.start()
    time.sleep(0.5)
    child3 = Process(target=juice)
    child3.start()