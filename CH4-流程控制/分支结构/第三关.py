'''《幸运的基督徒》
有15个基督徒和15个非基督徒在海上遇险，
为了能让一部分人活下来不得不将其中15个人扔到海里面去，
有个人想了个办法就是大家围成一个圈，由某个人开始从1报数，
报到9的人就扔到海里面，他后面的人接着从1开始报数，
报到9的人继续扔到海里面，直到扔掉15个人。由于上帝的保佑，
15个基督徒都幸免于难，问这些人最开始是怎么站的，哪些位置是基督徒哪些位置是非基督徒。
'''

def main():
    #        请在此处添加代码       #
    # *************begin************#
    isDead = [False for i in range(30)]
    cnt = 0
    idx = 0
    node = 0
    while cnt < 15:
        while isDead[idx]:
            idx = idx + 1
            if idx >= 30:
                idx = 0
        node = node + 1
        if node % 9 == 0:
            isDead[idx] = True
            cnt = cnt + 1
        idx = idx + 1
        if idx >= 30:
            idx = 0

    for p in isDead:
        if p :
            print(0,end='')
        else:
            print(1,end='')



 # **************end*************#

   

if __name__ == '__main__':
    main()
