class BankEmployee():
 #    请在此处添加代码 设置插槽    #
 # *************begin************#
 
 # **************end*************#
    def __init__(self,name="",num="",salary=3000): 
        self.__name = name
        self.__num = num
        self.salary = salary
    def get_salary(self): #定义领工资方法get_salary()
        print("%s领到这个月工资%d"%(self.__name,self.salary))
    def set_name(self,name):
        self.__name = name
    
    def get_name(self):
        return self.__name
            
    def set_num(self,num):
        self.__num = num
 
    def get_num(self):
        return self.__num
 
#commission 提成
class BankManager(BankEmployee):
    def __init__(self,name="",num="",salary=3000,commission=0):
        self.__name = name
        self.__num = num
        self.salary = salary
        self.commission = commission
 
    def get_commission(self):
        print(self.__name+"领到这个月提成"+str(self.commission))
 
# 请在此处添加代码 完成BankTeller类的定义#
# ************* begin  ************#
    
# ************** end  *************#
        
def main():
    name = input()
    num = input()
    salary = int(input())
    commission = int(input())
    bankmanager = BankManager(name,num,salary,commission)
    bankmanager.get_commission()
    
if __name__=="__main__":
    main()
