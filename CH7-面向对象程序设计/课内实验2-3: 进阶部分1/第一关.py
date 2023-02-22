class Fraction:
    def __init__(self,numerator = 0, denominator = 1):
        if denominator == 0:
            raise ZeroDivisionError("denominator cannot be zero")
        if numerator == 0:
            self._numerator = 0
            self._denomoinator = 1
        else:
            if(numerator<0 and denominator>0)or(numerator>0 and denominator<0):
                flag = -1
            else:
                flag = 1
            a = abs(numerator)
            b = abs(denominator)
            while a%b != 0:
                tempA = a
                tempB = b
                a = tempB
                b = tempA % tempB
            self._numerator = abs(numerator)//b*flag
            self._denominator = abs(denominator)//b
        

    def __eq__(self, others):
        if self._numerator == others._numerator and self._denominator == others._denominator:
            return True
        else:
            return False
        

    def __lt__(self, others):
        if self._numerator / self._denominator < others._numerator / others._denominator:
            return True 
        else:
            return False 
        
        
     
    #        请在此处添加代码            #
    #根据测试用例的，重载某些方法，实现定制类#
     # *************begin************#

     # **************end*************#

        
        
a = int(input())
b = int(input())
frac1 = Fraction(a,b)
c = int(input())
d = int(input())
frac2 = Fraction(c,d)
print(frac1<frac2)
print(frac1==frac2)
