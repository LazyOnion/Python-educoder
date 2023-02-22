def triangle(n):
    '''
       根据row值，打印三个三角形
       :row:三角形行数
       :return: 无返回值
       '''
    #        请在此处添加代码       #
    # *************begin************#
    for i in range(n):
        print("*" * (i + 1))
    for i in range(n):
        print(" " * (n - i - 1), end="")
        print("*" * (i + 1))
    for i in range(n):
        print(" " * (n - i - 1), end="")
        print("*" * ((i + 1) * 2 - 1))

    

    # **************end*************#
    
row = int(input())
triangle(row)
