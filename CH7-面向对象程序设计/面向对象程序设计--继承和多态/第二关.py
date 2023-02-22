class BankEmployee():
    def __init__(self,name="",num="",salary=2000): 
        self.__name = name
        self.__num = num
        self.salary = salary
    def get_salary(self): #定义领工资方法get_salary()
        print("%s领到这个月工资%d"%(self.__name,self.salary))
    # 请在此处添加代码对name和num设置set/get方法 #
     # *************   begin   ************#

    def set_num(self, num):
        self.__num=num
        if self.__num[0] == 's':
            return 
        print("工号以s开头")

    def set_name(self, name):
        self.__name=name
    
    def get_name(self):
        return self.__name
    
    def get_num(self):
        if self.__num[0] == 's':
            return self.__num 
        print("工号以s开头")
        
    
    
     # **************  end   *************#

  
class BankTeller(BankEmployee):
 #        请在此处添加代码         #
 # *************begin************#
    def __init__(self):
        super(BankTeller, self).__init__()

 # **************end*************#
        
def main():
    bankteller = BankTeller()
    name = input()
    num = input()
    bankteller.set_name(name)
    bankteller.set_num(num)
    bankteller.get_salary()
    print(bankteller.get_name(),bankteller.get_num())
    
if __name__=="__main__":
    main()
