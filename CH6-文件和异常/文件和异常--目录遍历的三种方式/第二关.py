#使用深度优先遍历目录
import os
def listDirWidthFirst(path):
    """
    广度遍历优先算法遍历目录

    :param director: 需遍历的路径
    :return:无返回值，直接输出
    """
# *************begin************#
    if (not os.path.isfile(path)) and (not os.path.isdir(path)):
        print('test.txt is not a directory or does not exist.')
        return 
    di = [path]
    while len(di) > 0:
        a = di.pop(0)
        for i in os.listdir(a):
            print(os.path.join(a, i))
            if os.path.isdir(os.path.join(a, i)):
                di.append(os.path.join(a, i))

# **************end*************#  


#遍历当前目录下的test目录
path = input()
listDirWidthFirst(path)
