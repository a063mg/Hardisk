import urllib2
from bs4 import BeautifulSoup
import time

start = time.time()
proxy = urllib2.ProxyHandler({'http': '178.238.40.33:80'})
opener = urllib2.build_opener(proxy)
urllib2.install_opener(opener)

import datetime
from selenium import webdriver
import urllib
import json
import codecs
import telebot
import time, requests, json, os
from datetime import datetime
from bs4 import BeautifulSoup
from urllib import urlopen
from time import sleep
from selenium.webdriver.support.ui import Select

def dropdate():
	sep = ''
	day = datetime.now().strftime('%d')
	week = datetime.weekday(datetime.now())
	if week > 3:
		cur_week = 6-week+4
	elif week != 3:
		cur_week = 3-week
	if int(day)+cur_week<10:
		sep = '0'
	dropdate = datetime.now().strftime('%Y-%m-{}'.format(sep+str(int(day)+cur_week)))
	return dropdate

# items_name = u'AKIRA/Supreme Patches Hooded Sweatshirt'
# items_color = 'Lime'
# items_size = 'Large'
# items_name = u"Supreme\xae/Levi's\xae Snakeskin Trucker Jacket"
# items_color = 'Purple'
# items_size = 'Large'
items_name = u"Supreme\xae/Levi's\xae Snakeskin Overalls"
items_color = 'Light Blue'
items_size = 'Large'


customs_name = 'Alekseev'
customs_email = 'alekseev.artem700@gmail.com'
customs_tel = '+79057455125'
customs_address = 'Leontevcky pereulok d 2'
customs_city = 'Moscow'
customs_postcode = '495'
customs_number = '0000 0000 0000 0000'


pas = True
while pas:
	# if datetime.now().strftime('%Y-%m-%d') == dropdate():
	if datetime.now().strftime('%H:%M:%S') >= '12:36:00':
		start = time.time()	
		url = 'http://www.supremenewyork.com/shop/new'
		urlink = 'http://www.supremenewyork.com'
		checkout_link = 'https://www.supremenewyork.com/shop/cart/'

		content = urllib2.urlopen(url).read()
		soup = BeautifulSoup(content, 'html.parser')

		for div in soup.select("div.inner-article"):
			if div.select("div.sold_out_tag") == [] and pas:
				product_link = urlink+div.select("img")[0].parent.get('href')
				product_content = urllib2.urlopen(product_link).read()
				product_soup = BeautifulSoup(product_content, 'html.parser')
				color = product_soup.title.string.split('-')[1]
				for details in product_soup.find_all('img'):
					if "image" == details.get('itemprop') and pas:
						name = details.get('alt')
						photo = details.get('src')
						if name == items_name:
							for p in product_soup.find_all('p'):
								if p.get('itemprop') == 'model': 
									if str(p.text) == items_color:
										print(name,color)
    									print(time.time() - start)
    									driver = webdriver.Chrome('/Users/Artem/Desktop/Music/chromedriver')
    									driver.get(product_link)
    									button_element = driver.find_element_by_name('commit')
    									select = driver.find_element_by_name('size')
    									select = Select(select)
    									print(time.time() - start)
    									if items_size != 'None':
	    									try:
	    										select.select_by_visible_text(items_size)
	    										# driver.get(checkout_link)
	    									except:
	    										pas = False
	    										print('No size')
	    								if pas:
	    									button_element.click()
    										sleep(0.5)
    										driver.get('http://www.supremenewyork.com/shop/cart')
	    									sub = driver.find_elements_by_xpath("//a[@class='button checkout']")
	    									sub[0].click()
	    									elem = driver.find_elements_by_xpath("//input[@placeholder='full name']")
	    									elem[0].send_keys(customs_name)
	    									elem = driver.find_elements_by_xpath("//input[@placeholder='email']")
	    									elem[0].send_keys(customs_email)
	    									elem = driver.find_elements_by_xpath("//input[@placeholder='tel']")
	    									elem[0].send_keys(customs_tel)
	    									elem = driver.find_elements_by_xpath("//input[@placeholder='address']")
	    									elem[0].send_keys(customs_address)
	    									elem = driver.find_elements_by_xpath("//input[@placeholder='city']")
	    									elem[0].send_keys(customs_city)
	    									elem = driver.find_elements_by_xpath("//input[@placeholder='postcode']")
	    									elem[0].send_keys(customs_postcode)
	    									elem = driver.find_elements_by_xpath("//input[@placeholder='number']")
	    									elem[0].send_keys(customs_number)
	    									select = driver.find_elements_by_xpath("//select[@class='select optional']")
    										select = Select(select[0])
    										select.select_by_visible_text('RUSSIA')
    										select = driver.find_elements_by_xpath("//select[@class='select required']")
    										select = Select(select[0])
    										select.select_by_visible_text('PayPal')
    										pas = False
    										finish = time.time()
    										print(finish - start)
    										break;
print(1)