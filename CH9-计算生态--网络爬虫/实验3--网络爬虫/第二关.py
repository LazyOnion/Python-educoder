import requests

def Evidence(url):
    # url为给定url地址，当给定url请求正确时输出状态码，请求失败输出错误信息
    #   请在此添加实现代码   #
    # ********** Begin *********#
    try:
        r = requests.get(url)
        print("Status: " + str(r.status_code))
    except:
        print("url请求失败")
    # ********** End **********#
