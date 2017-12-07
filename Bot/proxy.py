import urllib2
from bs4 import BeautifulSoup
import time
from selenium import webdriver

start = time.time()
proxy = urllib2.ProxyHandler({'http': '178.238.40.33:80'})
opener = urllib2.build_opener(proxy)
urllib2.install_opener(opener)

url = 'http://www.supremenewyork.com/shop/all/'
site = 'http://www.supremenewyork.com/'
content = urllib2.urlopen(url).read()

soup = BeautifulSoup(content, 'html.parser')

for div in soup.select("div.inner-article"):
	if div.select("div.sold_out_tag") == []:
		product_content = urllib2.urlopen(site+div.select("img")[0].parent.get('href')).read()
		product_soup = BeautifulSoup(product_content, 'html.parser')
		color = product_soup.title.string.split('-')[1]
		for details in product_soup.find_all('img'):
			if "image" == details.get('itemprop'):
				name = details.get('alt')
				photo = details.get('src')
				print(name,color)
				if name == u'Hooded Suede Work Jacket':
					driver = webdriver.Chrome('/Users/Artem/Desktop/Music/chromedriver')
					driver.get(site+div.select("img")[0].parent.get('href'))



finish = time.time()
time1 = finish - start
print(time1)