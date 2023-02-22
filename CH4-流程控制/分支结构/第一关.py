"""
英制单位英寸和公制单位厘米互换
"""
def cmin(value,unit):
    ''':param value:长度，
        :param unit:单位'''

    #        请在此处添加代码       #
    # *************begin************#
    if unit == "cm" or unit == "厘米":
        print("{:.2f}英寸".format(value / 2.54))
    elif unit == "in" or unit == "英寸":
        print("{:.2f}厘米".format(value * 2.54))
    else:
        print("请输入有效的单位")

    # **************end*************#
  

value = input()
value = int(value)
unit = input()
cmin(value,unit)
