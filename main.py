def write_down(data, filename='score.html'):
    fp = open(filename, 'w')
    fp.write(data)
    fp.close()
    print('write down ok')


import requests
from bs4 import BeautifulSoup
import os
import time


class hit_jwts(object):
    """ 程序主类
    """

    def __init__(self):
        """初始化函数
        """
        self.s = requests.Session()
        self.login()

    def login(self):
        url = 'http://jwts.hit.edu.cn/loginLdap'
        header = {
            'Host': 'jwts.hit.edu.cn',
            'Connection': 'keep-alive',
            'Content-Length': '40',
            'Cache-Control': 'max-age=0',
            'Origin': 'http//jwts.hit.edu.cn',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, \
            like Gecko) Ubuntu Chromium/51.0.2704.79 Chrome/51.0.2704.79 Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Referer': 'http//jwts.hit.edu.cn/loginLdapQian',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.8'
        }
        uid = input('输入你的学号')
        pwd = input('输入你的密码')
        post_data = {
            'usercode': uid,
            'password': pwd
        }
        r = self.s.post(url, headers=header, data=post_data)
        if r.status_code == 200:
            print('login ok')
        else:
            print('login fail')
            exit()

    def score(self):
        post_data = {
            'pageNo': 1,
            'pageSize': 250,
            'pageCount': 1
        }
        r = self.s.post('http://jwts.hit.edu.cn/cjcx/queryQmcj', data=post_data)
        if r.status_code == 200:
            print('get score ok')
            self.write_down(r.text, 'score.html')
        else:
            print('get score fail')
            exit()

    def write_down(self, data, filename, mode='w'):
        with open(filename, mode) as f:
            f.write(data)
        print(filename + 'write down ok')

    def getPhoto(self, uid):
        url = "http://jwts.hit.edu.cn/xswhxx/showPhoto?xh=" + str(uid)
        r = self.s.get(url)
        self.write_down(r.content, 'photo.jpg', 'wb')

    def qk(self):
        data = {
            'zy': '',
            'qz': '50',
            'pageXklb': 'tsk',
            'pageXnxq': '2016-20171',
            'pageKkxiaoqu': '',
            'pageKkyx': '',
            'pageKcmc': ''
        }
        url = "http://jwts.hit.edu.cn/xsxk/saveXsxk"
        # "2016-2017-1-GH43400100-001"
        term = '2016-2017-1'
        kc = ['GH41600700', 'GH42500100']
        cls = '001'
        for r in kc:
            data['rwh'] = term + '-' + r + '-' + cls
            print(data['rwh'])
            self.s.post(url, data=data)
            time.sleep(2)

    def run(self):
        c1.score()
        c1.getPhoto(1140340116)
        c1.qk()

if __name__ == '__main__':
    c1 = hit_jwts()
    c1.run()