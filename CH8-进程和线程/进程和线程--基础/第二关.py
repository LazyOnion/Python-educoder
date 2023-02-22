import concurrent.futures
import math

def is_prime(m):
    """
    判断一个数m是不是素数
    :param m: 正整数
    """
    #        请在此处添加代码       #
    # *************begin************#
    if m < 2:
        return False
    if m in (2, 3):
        return True
    if not m & 1:
        return False
    for i in range(3, int(m ** 0.5) + 1, 2):
        if m % i == 0:
            return False

    return True
    # **************end*************#  

def main(n):
    """
    判断0~n之间素数的个数
    :param m: 正整数
    """    
    #        请在此处添加代码       #
    # *************begin************#

    with concurrent.futures.ProcessPoolExecutor() as executor:
        print(sum(executor.map(is_prime,range(n))))
    # **************end*************#
    
if __name__ == '__main__':
    n = int(input())
    main(n)
