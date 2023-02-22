#使用深度优先遍历目录
import os


def listDirDepthFirst(path):
    """
    深度遍历算法遍历目录

    :param director: 需遍历的路径
    :return:无返回值，直接输出
    """
# *************begin************#
    al = os.listdir(path)
    for i in al:
        if os.path.isfile(os.path.join(path, i)):
            print(os.path.join(path, i))
        if os.path.isdir(os.path.join(path, i)):
            print(os.path.join(path, i))
            listDirDepthFirst(os.path.join(path, i))

# **************end*************#  


#遍历当前目录下的test目录
listDirDepthFirst('./test')
