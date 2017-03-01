# coding=utf-8
import requests
from bs4 import BeautifulSoup
from login import *
import time
import MySQLdb



class hit_jwts(object):
    """ 程序主类
    """

    def __init__(self, uid, pwd):
        """初始化函数
        """
        url = "http://jwts.hit.edu.cn/loginLdap"

        # 不能100%确定....
        ltype = get_login_style()

        if ltype == 0:
            s = self.login(uid, pwd)
        else:
            s = login(uid, pwd)
            test_url = "http://jwts.hit.edu.cn/loginCAS"
            s.get(test_url)
            print("test ok")
        self.s = s

    def login(self, uid, pwd):
        s = requests.Session()
        url = 'http://jwts.hit.edu.cn/loginLdap'
        header = {
            'Host': 'jwts.hit.edu.cn',
            'Origin': 'http//jwts.hit.edu.cn',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/51.0.2704.79 Chrome/51.0.2704.79 Safari/537.36',
            'Referer': 'http//jwts.hit.edu.cn/loginLdapQian'
        }
        post_data = {
            'usercode': uid,
            'password': pwd
        }
        r = s.post(url, headers=header, data=post_data)

        try:
            if len(r.headers['Set-Cookie']) > 20:
                print('login ok')
            else:
                print('login fail')
                exit()
        except Exception, e:
            pass

        return s

    def write_down(self, data, filename, mode='w'):
        with open(filename, mode) as f:
            f.write(data)
        print(filename + ' write down ok')

    def score(self):
        # post_data = {
        #     'pageNo': 1,
        #     'pageSize': 250,
        #     'pageCount': 1
        # }
        post_data = {
            'pageXnxq': "2015-20161",
        }
        r = self.s.post('http://jwts.hit.edu.cn/cjcx/queryQmcj', data=post_data)
        # r = self.s.post('http://jwts.hit.edu.cn/cjcx/queryQmcj', headers=header, data=post_data)
        if r.status_code == 200:
            print('get score ok')
            self.write_down(r.content, 'score.html')
        else:
            print('get score fail')
            exit()

    def getPhoto(self, uid):
        url = "http://jwts.hit.edu.cn/xswhxx/showPhoto?xh=" + str(uid)
        r = self.s.get(url)
        self.write_down(r.content, 'photo.jpg', 'wb')

    def xuanke(self,cid,lb,qz=""):
        url = "http://jwts.hit.edu.cn/xsxk/saveXsxk"
        data = {
            'rwh' : cid,
            'pageXklb':'xx',
            'qz': qz,
        }
        r = self.s.post(url,data)
        return r

    def cjxxview(self):
        filep = open("cjxx.txt","w")
        # 6666636
        start_id = 6669600
        baseurl = "http://jwts.hit.edu.cn/cjcx/queryCjxxView?id="
        f = 0
        while f<30:
            url = baseurl+str(start_id)
            r = self.s.get(url)
            if r.headers.get('Content-Length',0) == "1842":
                # 2472
                print start_id,"null"
                f+=1
                start_id += 1
                time.sleep(2)
                filep.write(str(start_id)+"\tnull\n")
                continue
            soup = BeautifulSoup(r.content,"lxml")
            data = soup.find_all('td')
            print start_id,data[0],data[3],data[7]
            filep.write(str(start_id)+str(data[0])+str(data[3])+str(data[7])+"\n")
            start_id += 1
            time.sleep(2)


    def gay(self):
        db = MySQLdb.connect("127.0.0.1","root","root","jwts")

        # 使用cursor()方法获取操作游标 
        cursor = db.cursor()

        # 6666620  6666794
        # 6666294  6670647
        start_id = 6670634
        # baseurl = "http://jwts.hit.edu.cn/cjcx/queryCjxxView?rwh=2016-2017-1-13GN12000300-017&id="

        baseurl = "https://vpn.hit.edu.cn/cjcx/,DanaInfo=jwts.hit.edu.cn+queryCjxxView?rwh=2016-2017-1-13GN12000300-017&id=667063"
        f = 0
        # i = 0
        while f<30:
            url = baseurl+str(start_id)
            r = self.s.get(url)
            # 13GN12000300
            if r.headers.get('Content-Length',0) == "2472":
                # 2472
                print start_id,"null"
                f+=1
                start_id += 1
                time.sleep(0.5)
                # filep.write(str(start_id)+"\tnull\n")
                continue
            soup = BeautifulSoup(r.content,"lxml")
            data = soup.find_all('td')
            # print data[2]
            if data[2].string=="13GN12000300":
                try:
                    sql = "INSERT INTO `jwts`.`gay` (`id`, `rwh`, `score`, `item1`, `item2`, `item3`) VALUES('%d', '%s', '%f', '%f', '%f', '%f');" % (start_id , data[0].string[-3:], float(data[7].string),float(data[9].string),float(data[11].string),float(data[13].string))
                    # print float(data[7].string)
                except Exception, e:
                    # raise e
                    if data[7].string == u"缓考":
                        status = 1
                    else:
                        status = 2
                    sql = "INSERT INTO `jwts`.`gay` (`id`, `rwh`, `status`) VALUES('%d', '%s', '%d');" % (start_id , data[0].string[-3:], status)
                print sql
                cursor.execute(sql)

            print start_id,data[0],data[3],data[7]
            # filep.write(str(start_id)+str(data[0])+str(data[3])+str(data[7])+"\n")
            start_id += 1
            # i+=1
            time.sleep(0.5)

        db.close()

    def tuike(self,cid="",lb=""):
        url = "http://jwts.hit.edu.cn/xsxk/saveXstk"
        header = {
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding':'gzip, deflate',
            'Accept-Language':'zh-CN,zh;q=0.8',
            'Cache-Control':'max-age=0',
            'Connection':'keep-alive',
            'Content-Length':'102',
            'Content-Type':'application/x-www-form-urlencoded',
            'Host':'jwts.hit.edu.cn',
            'Origin':'http://jwts.hit.edu.cn',
            'Referer':'http://jwts.hit.edu.cn/xsxk/queryYxkc',
            'Upgrade-Insecure-Requests':'1',
            'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.82 Safari/537.36'
        }
        data = {
            'rwh' : cid,
            'pageXklb' : lb,
            'pageXnxq':'2016-20172',
            'pageNj': '',
            'pageYxdm': '',
            'pageZydm': '',
            'pageKcmc': '',
        }
        r = self.s.post(url,headers=header, data=data)
        return r


if __name__ == '__main__':
    # 第一个参数学号，第二个参数密码
    c = hit_jwts('xxx', 'xxx')
    # c.cjxxview()
    c.gay()

    # c.score()
    # c.getPhoto('1140340116')

    # c.xuanke("2016-2017-2-13SE28001200-001","xx")
    # c.xuanke("2016-2017-1-GO00300400-001","qxrx")
    # c.tuike("2016-2017-1-GO00300400-001","qxrx")
