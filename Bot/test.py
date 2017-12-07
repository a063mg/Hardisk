from selenium import webdriver
import time

import datetime

import urllib
import json
import codecs
import telebot
import time, requests, json, os
from datetime import datetime
from bs4 import BeautifulSoup
from urllib import urlopen

url = 'http://www.supremenewyork.com/shop/new/'
urlink = 'http://www.supremenewyork.com'

content = urlopen(url).read()
soup = BeautifulSoup(content, 'html.parser')

no_item = True

names = u'AKIRA/Supreme Yamagata Tee'

# url = "https://www.supremecommunity.com/season/fall-winter2017/droplist/2017-11-02/"
# urlink = "https://www.supremecommunity.com"

# content = urlopen(url).read()
# soup = BeautifulSoup(content, 'html.parser')

# no_item = True

# for img in soup.find_all('img'):
# 	photo = img.get('src')
# 	if photo[1] == 'u':
# 		name = img.get('alt')
# 		photo = urlink+photo
# 		print(name)

for div in soup.find_all('div', 'inner-article'):
	img = div.find_all('img')
	if div.find_all('div') == []:
		no_item = False
		product_link = urlink+img[0].parent.get('href')
		product_content = urlopen(product_link).read()
		product_soup = BeautifulSoup(product_content, 'html.parser')
		color = product_soup.title.string.split('-')[1]
		for span in product_soup.find_all('span'):
			try:
				if span.get('itemprop') == "price":
					price = span.getText()
					currency = span.get('data-currency')
			except:
				continue
		for details in product_soup.find_all('img'):
			try:
				if "image" == details.get('itemprop'):
						name = details.get('alt')
						photo = details.get('src')
						if name == names:
							print(product_link)
							driver = webdriver.Chrome('/Users/Artem/Desktop/Music/chromedriver')
							driver.get(product_link)

			except:
				continue

# for div in soup.find_all('div', 'inner-article'):
# 	img = div.find_all('img')
# 	if div.find_all('div') == []:
# 		no_item = False
# 		product_link = urlink+img[0].parent.get('href')
# 		product_content = urlopen(product_link).read()
# 		product_soup = BeautifulSoup(product_content, 'html.parser')
# 		color = product_soup.title.string.split('-')[1]
# 		for span in product_soup.find_all('span'):
# 			try:
# 				if span.get('itemprop') == "price":
# 					price = span.getText()
# 					currency = span.get('data-currency')
# 			except:
# 				continue
# 		for details in product_soup.find_all('img'):
# 			try:
# 				if "image" == details.get('itemprop'):
# 						name = details.get('alt')
# 						photo = details.get('src')
# 						print(name, color, currency, price, 'http:'+photo)
# 			except:
# 				continue

# driver = webdriver.Chrome('/Users/Artem/Desktop/Music/chromedriver')
# # Go to your page url
# driver.get('http://www.supremenewyork.com/shop/shirts/hhdt309r6/tlw9sx4n1')
# # Get button you are going to click by its id ( also you could us find_element_by_css_selector to get element by css selector)
# button_element = driver.find_element_by_name('commit')
# button_element.click()
# driver.get('http://www.supremenewyork.com/checkout')
