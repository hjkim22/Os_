import threading
import os

def func():
    print("TEST FUNCTION")
    print("ProcessId :", os.getpid())
    print("ThreadId :", threading.get_native_id())

if __name__ == "__main__":
    print('기존 프로세스 아이디 :', os.getpid())
    thread1 = threading.Thread(target=func)
    thread1.start()