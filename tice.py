import requests
from bs4 import BeautifulSoup

s = requests.Session()


baseurl = "http://210.46.72.143/"
url = "http://210.46.72.143/servlet/adminservlet"

headers = {
	'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
}

r = s.get(baseurl, headers=headers)

soup = BeautifulSoup(r.text,'lxml')
random = soup.find_all("input",attrs={"name":"random_form"})[0]['value']

data = {
	"displayName":'',
	"displayPasswd":'',
	"submit.x":'53',
	"submit.y":'13',
	"operType":'911',
	"random_form":random,
	'select':'2',
	'userName':'1140340101',
	'passwd':'xxxxxx'
}

r = s.post(url, headers=headers ,data=data)


def main(sid):
	sid = str(sid)
	print "sid:",sid
	# url1 = "http://210.46.72.143/student/studentInfo.jsp"
	# r = s.get(url1, data={"userName":sid,"passwd":sid})
	r = s.get("http://210.46.72.143/student/studentInfo.jsp?userName="+sid+"&passwd="+sid)
	soup = BeautifulSoup(r.text,'lxml')
	print "id:",
	print soup.find_all("td")[15].text[1:]


	r2 = s.get("http://210.46.72.143/student/queryHealthInfo.jsp")
	soup = BeautifulSoup(r2.text,'lxml')

	tice = soup.find_all("td")
	height = tice[16].text
	weight = tice[24].text

	print "height:", height
	print "weight:", weight


main(1140340101)
