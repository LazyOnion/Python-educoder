import threading
import math
ans = 0
lock = threading.Lock()


import threading
import math
ans = 0
lock = threading.Lock()


def isPrime(n):
    # 判断数字是否为素数
   
    global ans
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
   



def howMany(T):
    # 计算给定区间含有多少个素数
   

    sum = 0
    for i in range(T[0], T[1] + 1):
        if isPrime(i):
            sum += 1
    lock.acquire()
    try:
        global ans
        ans += sum
    finally:
        lock.release()
   




def seprateNum(N, CPU_COUNT):
    # 对整个数字空间N进行分段CPU_COUNT
    list = [[i * (N // CPU_COUNT) + 1, (i + 1) * (N // CPU_COUNT)] for i in range(0, CPU_COUNT)]
    list[0][0] = 1
    if list[CPU_COUNT - 1][1] < N:
        list[CPU_COUNT - 1][1] = N
    return list

if __name__ == '__main__':
    N = int(input())
    threadNum = 32
 #        请在此处添加代码       #
    # *************begin************#
    t = []
    sepList = seprateNum(N, threadNum)
    for i in range(0, threadNum):
        t.append(threading.Thread(target = howMany, args = (sepList[i], )))
        t[i].start()
    for i in range(0, threadNum):
        t[i].join()
    print(N - 1 - ans, end = '')
    # **************end*************#
