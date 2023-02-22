class BankEmployee():
 #        请在此处添加代码         #
 # *************begin************#
    def __init__(self, name, num, salary=3000):
        self.name = name
        self.num = num
        self.salary = salary


    def get_salary(self):
        print(self.name + "领到这个月工资" + str(self.salary))

 # **************end*************#

def main():
    name = input()
    num = input()
    bankemployee = BankEmployee(name,num)
    bankemployee.get_salary()

if __name__=="__main__":
    main()
