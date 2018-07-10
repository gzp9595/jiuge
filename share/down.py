from urllib.request import urlopen
from bs4 import BeautifulSoup

def down(ss, cnt):
	for i in ss:
		try:
			tmp = i.find('img')['lowsrc']
			g = open("{0}.jpg".format(cnt),"wb")
			cnt += 1
			g.write(urlopen(tmp).read())
			g.close()
		except Exception as e:
			print(e)

html = urlopen("http://www.quanjing.com/category/12700332/1.html")
s = BeautifulSoup(html,"lxml")
ss = s.find_all('li')
down(ss, 0)