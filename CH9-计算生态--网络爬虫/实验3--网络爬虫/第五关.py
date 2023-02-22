# -*- coding: utf-8 -*-
import requests
import sys
from queue import Queue
import threading
from bs4 import BeautifulSoup as bs
import re
import base64
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, compress',
    'Accept-Language': 'en-us;q=0.5,en;q=0.3',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'
    }


class BaiduSpider(threading.Thread):
    """docstring for ClassName"""
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self._queue = queue

    def run(self):
        while not self._queue.empty():
            url = self._queue.get()
            try:
                self.spider(url)
            except Exception as e:
                print(e)
                pass

    def spider(self, url):
        r = requests.get(url=url, headers=headers, timeout=3)
        soup = bs(r.content, 'lxml')
        urls = soup.find_all(name='li')
        for url in urls:
            if url.string == None and url.a != None:
                if url.a.font.string == '2022年10月21日' or url.a.font.string == '2022年10月23日':
                    url = 'https://www.guet.edu.cn/jy/'+url.a['href']
                    r_get_url = requests.get(url=url, headers=headers, timeout=3)
                    if r_get_url.status_code == 200:
                        soup = bs(r_get_url.content, 'lxml')
                        get_urls = soup.find_all(name='div', attrs={'class': 'title'})
                        for get_url in get_urls:
                            if get_url.string != None:
                                print(r_get_url.url)
                                print(get_url.string)
                                
                                
def Evidence(keyword):
    queue = Queue()
    # md5加密关键字
    base64_encrypt = base64.b64encode(keyword.encode('utf-8'))
    keyword = str(base64_encrypt, 'utf-8')
    for i in range(1, 97):
        queue.put('https://www.guet.edu.cn/jy/search.jsp?wbtreeid=1001&_lucenesearchtype=1&searchScope=0&lucenenewssearchkeyword=%s&currentnum=%s'%(keyword, str(i)))
    threads = []
    thread_code = 5
    for i in range(thread_code):
        threads.append(BaiduSpider(queue))
    for t in threads:
        t.start()
    for t in threads:
        t.join()
