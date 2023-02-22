from os import listdir
from os.path import join,isfile,isdir
def listDir(director):
    """
     遍历文件夹，如果是文件就直接输出当前文件绝对路径，
     如果是文件夹，就输出当前文件夹路径，
     然后接着遍历该子文件夹，直到指定文件夹被全部遍历完。

     :param director: 需遍历的路径
     :return:无返回值，直接输出
     """
    #        请在此处添加代码       #
    # *************begin************#
    dirs = listdir(director)
    for i in dirs:
        pat = join(director, i)
        if isfile(pat):
            print(pat)
        elif isdir(pat):
            print(pat)
            listDir(pat)
    # **************end*************#



