def invert(score):
    '''
    百分制成绩转换为等级制成绩
    :param score:百分制分数
    :return: 等级（A，B，C，D，E）
    '''
    #        请在此处添加代码       #
    # *************begin************#
    if score >= 90 and score <= 100:
        return "A"
    elif score >= 80:
        return "B"
    elif score >=70:
        return "C"
    elif score >=60:
        return "D"
    else:
        return "E"

    # **************end*************#
    
score = float(input())
grad = invert(score)
print(grad)
