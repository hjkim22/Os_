# day2_과제
# 내 파이썬 프로그램의 이름을 알아보기

import psutil

def find_running_process():
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            process_name = proc.info['name']
            exe_path = proc.exe()

            if '08.py' in exe_path:
                return process_name
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

process_name = find_running_process()

if process_name:
    print(f"현재 실행 중인 '08.py' 파일과 연결된 프로세스의 이름: {process_name}")
else:
    print("현재 실행 중인 '08.py' 파일과 연결된 프로세스를 찾을 수 없음.")