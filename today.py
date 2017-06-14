# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 19:45:39 2015
@author: Tmn07
"""

import random
import time
import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

def get_recommend_url(page_url):
    '''
    获取"推荐本文"对应的链接
    '''
    page = requests.get(page_url).content                   # requests.get  获取页面
    soup = BeautifulSoup(page, 'html.parser')               # BeautifulSoup 解析页面
    iframe_url = soup.find_all('center')[1].iframe['src']   # 获取 iframe 链接
    recommend_url = 'http://today.hit.edu.cn' + iframe_url.replace('0.htm','1.htm')
    return recommend_url

def get_recommend_count(page_url):
    '''
    获取新闻推荐数
    '''
    page = requests.get(page_url).content
    soup = BeautifulSoup(page, 'html.parser')
    iframe_url = 'http://today.hit.edu.cn' + soup.find_all('center')[1].iframe['src']
    iframe_code = requests.get(iframe_url).content
    iframe_soup = BeautifulSoup(iframe_code, 'html.parser')
    recommend_count = iframe_soup.find_all('div',{'class','topBox'})[0].text
    recommend_count = recommend_count.replace('\t','').replace('\r','').replace('\n','')
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
    print ipAddress
    return ipAddress

def shua(page_url,k):
    url = get_recommend_url(page_url)           # 获取"推荐本文"的链接
    for i in range(k):
        headers = { "User-Agent": UserAgent().random, "X-Forwarded-For": ip_generator() }
        try:    
            request = requests.get(url, headers = headers)
        except requests.exceptions.RequestException, e:
            print e.code
            
        time.sleep(random.random())        
        print i+1


page_url = "http://today.hit.edu.cn/news/2017/06-05/4762308160RL1.htm"   # 新闻页面的链接
print get_recommend_count(page_url)     # 刷票前推荐数
shua(page_url,3)
print get_recommend_count(page_url)     # 刷票后推荐数
