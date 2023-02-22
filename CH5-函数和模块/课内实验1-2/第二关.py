from random import randrange, randint, sample
import random
def display(balls):
    """
    按照题目所要求格式输出列表中的双色球号码

    :param balls:双色球号码列表，如[9,12,16,20,30,33 3]
    :print:输出格式为09 12 16 20 30 33 | 03
    :return: 无返回值

    """
    #        请在此处添加代码       #
    # *************begin************#
    j = 0
    for i in balls:
        j = j + 1
        if j == 7:
            print("|", end=" ")
            if i < 10:
                i = "0" + str(i)
            print(i, end=' ')
            continue
        if i < 10:
            i = "0" + str(i)
            print(i, end=" ")
            continue
        else:
            print(i, end=" ")

    # **************end*************#


def random_select():
    """
    随机选择一组号码
    :return: 返回随机选择的这一组号码，如[9,12,16,20,30,33 3]
    """
    #        请在此处添加代码       #
    # *************begin************#
    tmp = [x for x in range(1, 34)]
    red = sample(tmp, 6)
    red.sort()
    tmp = [x for x in range(1, 17)]
    blue = sample(tmp, 1)
    return red + blue
        

    # **************end*************#

#n为注数
def main(n):

    for _ in range(n):
        display(random_select())
        if _ < n-1:
            print('') 
        
random.seed(3)
n = int(input())
if __name__ == '__main__':
    main(n)


