def write_down(data,filename='score.html'):
	fp = open(filename,'w')
	fp.write(data)
	fp.close()
	print('write down ok')

import requests
from bs4 import BeautifulSoup
import os

s = requests.Session()

url = 'http://jwts.hit.edu.cn/loginLdap'

header = {
	'Host': 'jwts.hit.edu.cn',
	'Connection': 'keep-alive',
	'Content-Length': '40',
	'Cache-Control': 'max-age=0',
	'Origin': 'http//jwts.hit.edu.cn',
	'Upgrade-Insecure-Requests': '1',
	'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/51.0.2704.79 Chrome/51.0.2704.79 Safari/537.36',
	'Content-Type': 'application/x-www-form-urlencoded',
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
	'Referer': 'http//jwts.hit.edu.cn/loginLdapQian',
	'Accept-Encoding': 'gzip, deflate',
	'Accept-Language': 'zh-CN,zh;q=0.8'
}
# uid = input('输入你的学号')
# pwd = input('输入你的密码')

post_data = {
	'usercode': '1140340116',
	'password': 'qq963852741'
}

r = s.post(url, headers=header ,data=post_data)

if r.status_code == 200:
	print ('login ok')
else:
	print('login fail')
	exit()


# post_data ={
# 	'pageNo' : 1,
# 	'pageSize' : 250,
# 	'pageCount':1
# }
# r = s.post('http://jwts.hit.edu.cn/cjcx/queryQmcj',data=post_data)

# if r.status_code == 200:
# 	print ('get score ok')
# else:
# 	print('get score fail')
# 	exit()

# write_down(r.text)


# main_soup = BeautifulSoup(r.text, 'lxml')
# form = main_soup.find(class_="bot_line")
# all_data = form.find_all('tr')
for c in range(1,3):

	img_url = "http://jwts.hit.edu.cn/xswhxx/showPhoto?xh=1152310" + str(c)

	ddir = './pic/gm15'+str(c)
	os.mkdir(ddir)
# if not os.path.exists(ddir):
    # 1522101


	for i in range(1,20):
		if i < 10:
			flag = '0'
		else:
			flag = ''
		r = s.get(img_url+flag+str(i))
		with open(ddir+'/pic'+str(i)+'.jpg','wb') as f:
			f.write(r.content)
		print('class '+str(c)+' num '+str(i)+'download  over')


	