def countSubstrings(s):
    """
    请计算字符串s中有多少个回文子字符串
    :param s:字符串
    :return：回文串个数
    """
    ct = 0
    for i in range(len(s)):
        for j in range(i, len(s)):
            tmp1 = s[i:j+1]
            tmp2 = tmp1[::-1]
            if tmp1 == tmp2:
                ct += 1
    return ct
