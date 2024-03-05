# import threading
# import time

# def daemon_thread():
#     print("데몬 스레드 시작")
#     time.sleep(2)
#     print("데몬 스레드 종료")  # 메인 스레드가 먼저 종료되면 이 메시지는 출력되지 않습니다.

# def non_daemon_thread():
#     print("일반 스레드 시작")
#     print("일반 스레드 종료")

# daemon = threading.Thread(name='daemon_thread', target=daemon_thread)
# daemon.setDaemon(True)  # 데몬 스레드로 설정

# non_daemon = threading.Thread(name='non_daemon_thread', target=non_daemon_thread)

# daemon.start()
# non_daemon.start()




import threading
import time

def first():
    print(11)
    time.sleep(0.1)
    print(22)
    time.sleep(0.1)
    print(33)
    time.sleep(0.1)
    
def second():
    print(1111)
    time.sleep(0.1)
    print(2222)
    time.sleep(0.1)
    print(3333)
    time.sleep(0.1)
    
def loop():
    for i in range(1,10):
        print(f"반복문:{i}")
        time.sleep(0.1)
        
        
f = threading.Thread(target=first)
s = threading.Thread(target=second)
l = threading.Thread(target=loop)

l.daemon = True 

l.start() 
f.start()
s.start()        

