def is_prime(num):
    """
    判断一个数是不是素数
    :param num: 正整数
    :return: 是素数返回True，不是素数返回False
    """
    #        请在此处添加代码       #
    # *************begin************#
    i = 2
    while i * i < num :
        if num % i == 0:
            return False
        i = i + 1
    return True
    # **************end*************#
def is_palindrome(num):
    """
    判断一个数是不是回文数
    :param num: 正整数
    :return: 是回文数返回True，不是回文数返回False
    """
    #        请在此处添加代码       #
    # *************begin************#
    strNum = str(num)
    return strNum[::-1] == strNum
    # **************end*************#
def prime_palindrome(num):
    """
        判断一个数是不是回文素数
        :param num: 正整数
        :return: 是回文素数返回True，不是回文素数返回False
        """
    #        请在此处添加代码       #
    # *************begin************#
    return is_prime(num) and is_palindrome(num)
    # **************end*************#
