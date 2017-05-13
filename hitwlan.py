# coding=utf-8
import requests
from bs4 import BeautifulSoup
from config import *

s = requests.Session()

url = 'http://192.168.52.11/srun_portal_pc.php?ac_id=1&'

header = {
    'Host': '192.168.52.11',
    'Origin': 'http://192.168.52.11',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/51.0.2704.79 Chrome/51.0.2704.79 Safari/537.36',
    'Referer': 'http://192.168.52.11/srun_portal_pc.php?url=&ac_id=1',
}

# usernama里@sam前填学号，password填密码
post_data = {
    'action': 'login',
    'username': netuid,
    'password': netpwd,
    'ac_id': '1',
    'user_ip':'',
	'nas_ip':'',
	'user_mac':'',
	'url':'',
	'save_me':'1'
}

r = s.post(url, headers=header, data=post_data)
try:
	soup = BeautifulSoup(r.text,"lxml")
	fs = soup.find("fieldset")
	print fs.find("p").text
except Exception, e:
	print "login ok"


# print(r.text)

# input()
