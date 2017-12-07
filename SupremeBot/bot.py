# -*- coding: utf-8 -*-
# vim: set fileencoding=utf-8 

import datetime

import urllib
import json
import codecs
import telebot
import time, requests, json, os
from datetime import datetime
from bs4 import BeautifulSoup
from urllib import urlopen

reader = codecs.getreader("utf-8")

token = '375602165:AAH6-j-iLozcXPOZP90r_6tz_7m2Yu2Nf_Q'

bot = telebot.TeleBot(token)

print('Server started...')

url = 'http://www.supremenewyork.com/shop/all/'

site = 'http://www.supremenewyork.com/'

@bot.message_handler(commands=['start'])
def start(message):
	markup = telebot.types.ReplyKeyboardMarkup()
	markup.row('New items')
	# markup = telebot.types.InlineKeyboardMarkup()
	# btn_my_site = telebot.types.InlineKeyboardButton(text='Buy', callback_data="Item_name")
	# markup.add(btn_my_site)
	bot.send_message(message.chat.id, "Chose option:", reply_markup = markup)
@bot.callback_query_handler(func=lambda text:True)	
def reply(text):
	print(text)

@bot.message_handler(content_types=['text'])
def process(message):
	if message.text == "Back":
		markup = telebot.types.ReplyKeyboardMarkup()
		markup.row('New items')
		bot.send_message(message.chat.id, "Chose option:", reply_markup = markup)
	if message.text == "New items":

		markup = telebot.types.ReplyKeyboardMarkup()
		markup.row('Back')
		bot.send_message(message.chat.id, "All new items:", reply_markup=markup)
		
		url = 'http://www.supremenewyork.com/shop/new'
		urlink = 'http://www.supremenewyork.com'

		content = urlopen(url).read()
		soup = BeautifulSoup(content, 'html.parser')

		no_item = True

		for div in soup.find_all('div'):
			try:
			    link = div.get('class')
			    if link[0] == 'inner-article':
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
				    					print(name, color, currency, price, 'http:'+photo)
				    					bot.send_message(message.chat.id, name+" ("+color+")"+" - "+currency+": "+price)
						    			bot.send_photo(message.chat.id, 'http:'+photo)
			    			except:
			    				continue
		 	except:
		 		continue
		if no_item:
			bot.send_message(message.chat.id, "Sorry all items are sold out...")


bot.polling()

