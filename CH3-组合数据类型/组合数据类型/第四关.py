#打印杨辉三角
#（不需返回函数值，直接打印）
def printYH(n):
    ''':param num: 杨辉三角行数'''

#        请在此处添加代码       #
# *************begin************#

    sz = [[0 for j in range(n+1)] for i in range(n+1)]

    for i in range(n+1):
        sz[i][0] = 1

    for i in range(1, n+1):
        for j in range(1, i+1):
            sz[i][j] = sz[i-1][j-1] + sz[i-1][j]

    for i in range(n):
        for j in range(i+1):
            print(sz[i][j], end='\t')
        print('')

# **************end*************#


