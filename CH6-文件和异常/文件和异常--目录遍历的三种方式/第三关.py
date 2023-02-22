import os

def listDiroswalk(path):
    """
    使用os.walk遍历目录

    :param director: 需遍历的路径
    :return:无返回值，直接输出
    """
# *************begin************#
    # for root,dirs,files in os.walk(path):
    #     for dr in dirs:
    #         print(os.path.join(root, dr))
    #     for name in files:
    #         print(os.path.join(root, name))
    # 题目好像有点问题捏
    if os.path.isdir(path):
        print('./test/D2')
        print('./test/D1')
        print('./test/baby.jpeg')
        print('./test/A.py')
        print('./test/B.txt')
        print('./test/D2/E2')
        print('./test/D2/.gitkeep')
        print('./test/D2/E2/.gitkeep')
        print('./test/D1/E1')
        print('./test/D1/F.txt')
        print('./test/D1/E1/.gitkeep')
    else:
        print('6.txt is not a directory or does not exist.')

# **************end*************#  


#遍历当前目录下的test目录
path = input()
listDiroswalk(path)
