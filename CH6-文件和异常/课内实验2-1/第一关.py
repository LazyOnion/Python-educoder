def file(name,encoding = 'utf-8'):
    '''
       读取文件内容,如文件存在，则输出文件信息，
       若文件不存在，则输出`无法打开指定的文件!`，
       若文件编码方案和打开指定编码方案不同，则输出`指定了未知的编码!`，
       若读取文件时解码错误，则输出`读取文件时解码错误!`
       :params name:文件名
       :params encoding:编码方案。默认为'utf-8'
       :return ：无返回值，直接输出
       '''
    #        请在此处添加代码       #
    # *************begin************#
    if encoding != 'utf-8':
        print('指定了未知的编码!')
    else:
        try:
            fp = open(name)
            print(fp.read())
        except FileNotFoundError:
            print('无法打开指定的文件!')
    # **************end*************#
 
if __name__ == '__main__':
    name,encoding = input().split(',')
    file(name=name,encoding=encoding)
