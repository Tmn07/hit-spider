
import requests
from bs4 import BeautifulSoup

def write(data, filename='test.html'):
    fp = open(filename, 'w')
    fp.write(data)
    fp.close()
    print('write down ok')


url = 'https://vpn.hit.edu.cn/dana-na/auth/url_default/login.cgi'

header = {
"Accept-Language":"zh-CN,zh;q=0.8",
'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/53.0.2785.143 Chrome/53.0.2785.143 Safari/537.36'
}
post_data = {
    "tz_offset":"480",
    "username":"1140340116",
    "password":"xxxxx",
    "realm":"本科生",
    "btnSubmit":"登陆"
}
s = requests.Session()

r = s.post(url, headers=header, data=post_data)
write(r.content,'vpn.html')

jwts_login_url = "https://vpn.hit.edu.cn/,DanaInfo=jwts+loginLdapQian"

r = s.get(jwts_login_url, headers=header)

import re
from somersa import rsa

n = eval(re.findall("KeyPair(.*?);", r.text)[0])[2]
post_data = {}
post_data['username'] =  rsa('1140340116', n)
post_data['password'] = rsa('qq963852741', n)
post_data['code'] = ""
print post_data
# ???
jwts_url = 'https://vpn.hit.edu.cn/,DanaInfo=jwts+loginLdap'
header = {
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding":"gzip, deflate, br",
    "Accept-Language":"zh-CN,zh;q=0.8",
    "Cache-Control":"max-age=0",
    "Connection":"keep-alive",
    "Content-Length":"281",
    "Content-Type":"application/x-www-form-urlencoded",
    "Host":"vpn.hit.edu.cn",
    "Origin":"https://vpn.hit.edu.cn",
    "Referer":"https://vpn.hit.edu.cn/,DanaInfo=jwts+loginLdapQian",
    "Upgrade-Insecure-Requests":"1",
    "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/53.0.2785.143 Chrome/53.0.2785.143 Safari/537.36"
}

r = s.post(jwts_url, headers=header, data=post_data)
write(r.content,"vpn-jwts.html")

# s.get("https://vpn.hit.edu.cn/xswhxx/,DanaInfo=jwts+showPhoto?xh=1140340116")

# write_down(r.content, 'photo.jpg', 'wb')


# try:
#     if len(r.headers['Set-Cookie']) > 20:
#         print('login ok')
#     else:
#         print('login fail')
#         exit()
# except Exception, e:
#     pass

# return s