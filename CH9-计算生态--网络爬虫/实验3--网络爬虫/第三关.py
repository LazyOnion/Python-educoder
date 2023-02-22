import re

def Evidence(text):
    # text为给定字符串
    #   请在此添加实现代码   #
    # ********** Begin *********#
    print(re.match(r'^(\w*d*)@\w*.(com|cn)$',text))
    # ********** End **********#
