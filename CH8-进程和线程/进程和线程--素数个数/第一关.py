import math
from multiprocessing import cpu_count
from multiprocessing import Pool


def isPrime(n):
    # 判断数字是否为素数
    #        请在此处添加代码       #
    # *************begin************#
    if n < 2 : return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True



def howMany(T):
    # 计算给定区间含有多少个素数
    #        请在此处添加代码       #
    # *************begin************#
    
    # **************end*************#
    sum = 0
    for k in T:
        if isPrime(k):
            sum += 1
    return sum



def separateNum(N, CPU_COUNT):
    # 对整个数字空间N进行分段CPU_COUNT
    #        请在此处添加代码       #
    # *************begin************#
    list = [[i for i in range(j, j+int(N/CPU_COUNT))]for j in range(0, N, int(N/CPU_COUNT))]
    x = N%CPU_COUNT
    if x != 0:
        for k in range(int(N/CPU_COUNT)*CPU_COUNT+1,N+1):
            list[CPU_COUNT-1].append(k)
    return list
    # **************end*************#
    
if __name__ == '__main__':
    N = int(input())
    # 多进程
    CPU_COUNT = cpu_count()  ##CPU内核数 本机为8
    pool = Pool(CPU_COUNT)
    sepList = separateNum(N, CPU_COUNT)
    result = []
    for i in range(CPU_COUNT):
        result.append(pool.apply_async(howMany, (sepList[i], )))
    pool.close()
    pool.join()
    # ans = 0
    list = [res.get() for res in result]
    print(sum(list), end = '')
