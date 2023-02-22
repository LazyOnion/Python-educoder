def countlevel():
    '''
     
       :return:最小阶梯数
       '''
    #        请在此处添加代码       #
    # *************begin************#
    for x in range(100, 200):
        if x % 2 == 1 and x % 3 == 2 and x % 5 == 4 and x % 6 == 5 and x % 7 == 0:
            return x


    # **************end*************#
    
print(countlevel())
