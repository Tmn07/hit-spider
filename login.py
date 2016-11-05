# coding=utf-8

import requests
from bs4 import BeautifulSoup

def write_down(data, filename='test.html'):
    fp = open(filename, 'w')
    fp.write(data)
    fp.close()
    print('write down ok')


def login(uid, pwd):
    # 前往认证登录页面
    url = "https://ids.hit.edu.cn/authserver/login"

    s = requests.Session()

    r = s.get(url)

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


def get_login_style():
    # 前往页面，查看教务处登录方式
    url = "http://jwts.hit.edu.cn/"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')

    login_url = soup.find('a', id='dl')['href']

    if login_url == '/loginLdapQian':
        # 旧版教务处登录
        return 0
    else:
        # 新版统一认证登录？
        return 1


if __name__ == '__main__':
    # 第一个参数学号，第一个参数密码
    s = login('xxx', 'xxx')

    # 前往其他网站，验证登录
    test_url = "https://cms.hit.edu.cn/my/"
    r = s.get(test_url)

    write_down(r.content)

    print (get_login_style())
