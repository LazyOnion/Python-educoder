#根据main函数以及输出设计person函数的参数以及函数的功能
# *************begin************#
def person(name,**kw):
    print("name"+" "+name)
    for i in kw:
        if(kw[i]):
            print(i+" "+kw[i])
# **************end*************#  
def main():
    person('Alice',city='GL')
    person('Bob',gender='M',job='Teacher')
if __name__=='__main__':
    main()
