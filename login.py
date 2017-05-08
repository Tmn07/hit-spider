# coding=utf-8
import re
import requests
from bs4 import BeautifulSoup

from config import *
from somersa import rsa

def write_down(data, filename='test.html'):
    fp = open(filename, 'w')
    fp.write(data)
    fp.close()
    print('write down ok')


def login(uid, pwd):
    # 前往认证登录页面
    url = "https://ids.hit.edu.cn/authserver/login"

    s = requests.Session()

    r = s.get(url, timeout=None)

    soup = BeautifulSoup(r.text, 'lxml')

    login_form = soup.find('form', id="casLoginForm")

    # print(login_form)

    # 获取登录所需要的在页面表单中的隐藏信息
    hidden_inputs = login_form.find_all('input', type='hidden')

    hidden_data = {}

    for i in hidden_inputs:
        hidden_data[i['name']] = i['value']

    # write_down(r.content)

    # 加入学号，密码
    hidden_data['username'] = uid
    hidden_data['password'] = pwd

    # 构造请求头
    header = {
        'Referer': 'https://ids.hit.edu.cn/authserver/login',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.82 Safari/537.36'
    }
    # header = {
    #     'Accept':'*/*',
    #     'Accept-Encoding':'gzip, deflate, sdch',
    #     'Accept-Language':'zh-CN,zh;q=0.8',
    #     'Connection':'keep-alive',
    #     'Host':'jwts.hit.edu.cn',
    #     'Cookie':'JSESSIONID=xkQLYT6Khvy59vfp1fyx3dXh1htt9v7h959sxLmhLYh0bcJxvGcn!-1677291570; clwz_blc_pst=16781484.23323; name=value',
    #     'Referer':'http//:jwts.hit.edu.cn/',
    #     'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
    # }
    # 发送登录信息
    r = s.post('https://ids.hit.edu.cn/authserver/login', headers=header, data=hidden_data)

    try:
        soup = BeautifulSoup(r.text, 'lxml')
        err = soup.find(id='msg')
        if err:
            print(err.text)
        else:
            print('login ok')
    except Exception, e:
        pass

    return s

def old_login(uid, pwd):
    f=open("test.html")
    data=f.read()
    n = eval(re.findall("KeyPair(.*?);", data)[0])[2]
    post_data = {}
    post_data['username'] =  rsa(uid, n)
    post_data['password'] = rsa(pwd, n)
    print post_data

def get_login_style():
    # 前往页面，查看教务处登录方式
    url = "http://jwts.hit.edu.cn/"
    data = {
        'Accept':'*/*',
        'Accept-Encoding':'gzip, deflate, sdch',
        'Accept-Language':'zh-CN,zh;q=0.8',
        'Connection':'keep-alive',
        'Host':'jwts.hit.edu.cn',
        'Referer':'http//:jwts.hit.edu.cn/',
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
    }
    r = requests.get(url,headers=data)
    soup = BeautifulSoup(r.text, 'lxml')

    login_url = soup.find('a', id='dl')['href']
    # http://jwts.hit.edu.cn/loginCAS
    if login_url == '/loginLdapQian':
        # 旧版教务处登录
        print "old"
        return 0
    else:
        # 新版统一认证登录？
        print "new"
        return 1


if __name__ == '__main__':
    # 第一个参数学号，第一个参数密码
    # s = login(username, password)

    # 前往其他网站，验证登录
    # test_url = "https://cms.hit.edu.cn/my/"
    # r = s.get(test_url, verify=False)

    # write_down(r.content)

    # print (get_login_style())
    old_login(username, password)
