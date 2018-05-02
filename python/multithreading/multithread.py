import threading


#0~10000까지 더한걸 받을꺼임 ; 500500
#파이썬의 전역변수
g_result = 0
lock = threading.Lock()

def thread_main(*args):
    global g_result
    global lock
    result = 0

    for arg in args:
        g_result += arg
    lock.release()

n = 1000000
offset = n // 4

li = [ e for e in range(n + 1)]

threads = []

for i in range(4):
    th = threading.Thread(target = thread_main, args = li[offset * i + 1 : offset *(i + 1) + 1])

    th.start()
    threads.append(th)

for th in threads:
    th.join()

print("g_result : {}".format(g_result))
