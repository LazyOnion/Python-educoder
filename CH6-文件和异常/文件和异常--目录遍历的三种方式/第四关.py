import os

def findfile(path,dstfile):
    """
    遍历目录中是否存在dstfile文件，如果存在输出该文件的内容，否则输出 dstfile does not exist.

    :param path: 需遍历的路径
    :dstfile: 需要查找的文件
    """
# *************begin************#
    
    flag = False
    if not os.path.isdir(path):
        print(path + ' is not a directory or does not exist.')
        return 
    for root,dirs,files in os.walk(path):
        if dstfile in files:
            with open(os.path.join(root, dstfile)) as fp:
                for i in fp.readlines():
                    print(i, end='')
                    flag = True
    if not flag:
        print(dstfile + ' does not exist.')

# **************end*************#  


#遍历当前目录下的test目录
path = input()
file = input()
findfile(path,file)
