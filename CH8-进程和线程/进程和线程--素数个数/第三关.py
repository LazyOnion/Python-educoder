import threading
import sys
import time


def showfoo(n):
    '''
    
    :param n: 要输出foobarpython的次数
    :return: 无返回，可直接输出
    '''
    # 请在此处添加代码       #
# *************begin************#
    for i in range(n):
      lockfoo.acquire()
      print("foo",end="")
      lockbar.release()
# **************end*************#


def showbar(n):
    '''

      :param n: 要输出foobarpython的次数
      :return: 无返回，可直接输出
      '''
    # 请在此处添加代码       #
# *************begin************#
    for i in range(n):  
      lockbar.acquire()
      print("bar",end="")
      lockpython.release()
# **************end*************#

def showpython(n):
    '''

      :param n: 要输出foobarpython的次数
      :return: 无返回，可直接输出
      '''
     # 请在此处添加代码       #
# *************begin************#
    for i in range(n):
      lockpython.acquire()
      print("python",end="")
      lockfoo.release() 
# **************end*************#


if __name__ == '__main__':
    lockfoo = threading.Lock()  # 定义3个互斥锁
    lockbar = threading.Lock()
    lockpython =threading.Lock()
    n = int(input())
    t1 = threading.Thread(target=showfoo,args=[n])  # 定义3个线程
    t2 = threading.Thread(target=showbar,args=[n])
    t3 = threading.Thread(target=showpython,args=[n])
    lockpython.acquire()  # 先锁住foo,bar锁，保证先打印foo
    lockbar.acquire()


    t1.start()
    t2.start()
    t3.start()
