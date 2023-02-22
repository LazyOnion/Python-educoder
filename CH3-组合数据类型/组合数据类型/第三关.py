def is_leap_year(year):
    """
    判断指定的年份是不是闰年

    :param year: 年份
    :return: 闰年返回True平年返回False
    """
    #        请在此处添加代码       #
    # *************begin************#
    return year%4==0 and year%100 != 0 or year%400==0 

    # **************end*************#


def which_day(year, month, date):
    """
    计算传入的日期是这一年的第几天

    :param year: 年
    :param month: 月
    :param date: 日
    :return: 第几天
    """
 #        请在此处添加代码       #
    # *************begin************#
    Day=[31,28,31,30,31,30,31,31,30,31,30,31]
    Day_leap=[31,29,31,30,31,30,31,31,30,31,30,31]
    total=0
    if(is_leap_year(year)):
        for i in range(month-1):
            total+=Day_leap[i]
        return total+date
    else:
        for i in range(month-1):
            total+=Day[i]
        return total+date


    # **************end*************#
