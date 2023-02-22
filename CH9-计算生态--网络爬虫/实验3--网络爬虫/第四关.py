#!/usr/bin/env python
#coding=utf-8

import requests
from bs4 import BeautifulSoup

def Evidence(date):
    #    date为给定日期
    #   请在此添加实现代码   #
    # ********** Begin *********#
    response = requests.get("https://www.guet.edu.cn/jy/zhaopin.jsp?a165823t=70&a165823p=4&a165823c=50&urltype=tree.TreeTempUrl&wbtreeid=1003")
    soup = BeautifulSoup(response.text, 'lxml')
    titles = soup.find_all("li",class_=None)
    for title in titles:
        post = title.find("a")
        if post:
            a = post.getText().replace('\n','').replace('\r','').replace('\t','')
            day=a[-10:]
            if day==date:
                if a[:-10] != "第八周用人单位进校招聘一览表（10月23日-10月30日）":
                    print(a[:-10])
    # ********** End **********#
