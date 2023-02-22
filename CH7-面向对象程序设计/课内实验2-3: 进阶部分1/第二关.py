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

     
    #        请在此处添加代码            #
    #根据测试用例的，重载某些方法，实现定制类#
     # *************begin************#
    def __add__(self, oth):
        tmp1 = self._numerator * oth._denominator + self._denominator * oth._numerator
        tmp2 = self._denominator * oth._denominator
        return Fraction(tmp1, tmp2)


    def __sub__(self, oth):
        tmp1 = self._numerator * oth._denominator - self._denominator * oth._numerator
        tmp2 = self._denominator * oth._denominator
        return Fraction(tmp1, tmp2)


    def __repr__(self):
        return str(self._numerator) + '/' + str(self._denominator)

     # **************end*************#

        
        
a = int(input())
b = int(input())
frac1 = Fraction(a,b)
c = int(input())
d = int(input())
frac2 = Fraction(c,d)
resultSUB = frac1-frac2
print(resultSUB)
resultADD = frac1+frac2
print(resultADD)
