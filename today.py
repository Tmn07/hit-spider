# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 19:45:39 2015
@author: Tmn07
"""

import urllib2
import random
import time
from bs4 import BeautifulSoup

def get_recommend_url(page_url):
    '''
    获取"推荐本文"对应的链接
    '''
    request = urllib2.Request(page_url)
    page = urllib2.urlopen(request)
    soup = BeautifulSoup(page, 'html.parser')
    iframe_url = soup.find_all('center')[1].iframe['src']   # 获取 iframe 链接
    recommend_url = 'http://today.hit.edu.cn' + iframe_url.replace('0.htm','1.htm')
    return recommend_url

def get_recommend_count(page_url):
    '''
    获取新闻推荐数
    '''
    request = urllib2.Request(page_url)
    page = urllib2.urlopen(request)
    soup = BeautifulSoup(page, 'html.parser')
    iframe_url = 'http://today.hit.edu.cn' + soup.find_all('center')[1].iframe['src']
    iframe_page = urllib2.urlopen(iframe_url)
    iframe_code = iframe_page.read()
    string_before = '<div class="topBox ">\t\r\n\t\t'
    string_after = '\t\r\n\t</div>'
    recommend_count = iframe_code[iframe_code.find(string_before) + len(string_before) : iframe_code.find(string_after)]
    return int(recommend_count)
    
def ip_generator():
    '''
    生成随机的IP地址
    '''
    a = random.randint(1,255)
    b = random.randint(0,255)
    c = random.randint(0,255)
    d = random.randint(0,255)
    ipAddress = "%d.%d.%d.%d" % (a,b,c,d)
    return ipAddress

def shua(page_url,k):
    user_agent = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36'  
    headers = { 'User-Agent' : user_agent }
    url = get_recommend_url(page_url)
    
    for i in range(k):

        ipAddress = ip_generator()
        print ipAddress
        headers["X-Forwarded-For"] = ipAddress
        
        time.sleep(1)
        
        request = urllib2.Request(url, "", headers)  
        try:    
            urllib2.urlopen(request)
        except urllib2.HTTPError,e:
            print e.code
        
        print i

page_url = "http://today.hit.edu.cn/news/2017/06-05/4762308160RL1.htm"   # 新闻页面的链接

print get_recommend_count(page_url)     # 刷票前推荐数
shua(page_url,3)
print get_recommend_count(page_url)     # 刷票后推荐数
