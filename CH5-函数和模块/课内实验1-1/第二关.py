def Change(num):
    """
    :阿拉伯数值与中文数值之间的转换
    :param num: 阿拉伯数值的金额
    :return: 转换后的中文大写格式金额
    """
    #        请在此处添加代码       #
    # *************begin************#
    ch = ["零","壹","贰","叁","肆","伍","陆","柒","扒","玖"]
    bit = ["分","角","元","拾","佰","仟"]
    num = num * 1000
    tmp = int(num) // 10
    idx = 0
    res = ""
    while tmp > 0 :
        res = res + bit[idx] + ch[tmp % 10]
        tmp = tmp // 10
        idx = idx + 1
    return res[::-1]
