# coding=utf-8
import requests

s = requests.Session()

url = 'http://192.168.52.11/cgi-bin/srun_portal'

header = {
    'Host': '192.168.52.11',
    'Origin': 'http://192.168.52.11',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/51.0.2704.79 Chrome/51.0.2704.79 Safari/537.36',
    'Referer': 'http://192.168.52.11/srun_portal_pc.php?url=&ac_id=1',
}

# usernama里@sam前填学号，password填密码
post_data = {
    'action': 'login',
    'username': 'xxx@sam',
    'password': 'xxx',
    'ac_id': '1',
    'type': '1',
    'wbaredirect': '',
    'mac': '',
    'user_ip': '',
    'vrf_id': '0'
}

r = s.post(url, headers=header, data=post_data)

print(r.text)

# input()