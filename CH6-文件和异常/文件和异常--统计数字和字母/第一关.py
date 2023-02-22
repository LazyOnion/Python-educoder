#统计大写字母出现的次数，并按照字母出现次数降序排序输出
def countchar(file):
# *************begin************#
    fp = open(file, mode='r')
    ch = fp.read()
    l = {}
    for i in ch:
        if i.isupper():
            if i in l:
                l[i] += 1
            else:
                l[i] = 1
    lista = sorted(l.items(), key=lambda e: e[1], reverse=True)
    for i,j in lista:
        print((i,j))


# **************end*************#  


file = input()
countchar(file)
