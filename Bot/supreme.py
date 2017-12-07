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

token = '494624716:AAGUvKUBtW1tjzUKS9Q6N4Ehbw9epL8GgZo'

bot = telebot.TeleBot(token)

print('Server started...')

url = 'http://www.supremenewyork.com/shop/all/'

site = 'http://www.supremenewyork.com/'

def dropdate():
	sep = ''
	cur_week = 0
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


@bot.message_handler(commands=['start'])
def start(message):
	markup = telebot.types.ReplyKeyboardMarkup()
	markup.row('New avaliable items')
	markup.row('Droplist')
	# markup = telebot.types.InlineKeyboardMarkup()
	# btn_my_site = telebot.types.InlineKeyboardButton(text='Buy', callback_data="Item_name")
	# markup.add(btn_my_site)
	bot.send_message(message.chat.id, "Chose option:", reply_markup = markup)

@bot.callback_query_handler(func=lambda text:True)	
def reply(text):
	print(text.data)

@bot.message_handler(content_types=['text'])
def process(message):
	print(message.text)
	if message.text == "Back":
		markup = telebot.types.ReplyKeyboardMarkup()
		markup.row('New avaliable items')
		markup.row('Droplist')
		bot.send_message(message.chat.id, "Chose option:", reply_markup = markup)

	if message.text == "Button":
		markup = telebot.types.InlineKeyboardMarkup()
		btn_my_site = telebot.types.InlineKeyboardButton(text='Buy', callback_data="Item_name")
		markup.add(btn_my_site)
		bot.send_message(message.chat.id, "Click me", reply_markup = markup)

	if message.text == "Droplist":
		markup = telebot.types.ReplyKeyboardMarkup()
		markup.row('Back')
		bot.send_message(message.chat.id, "Items on droplist:", reply_markup=markup)

		url = "https://www.supremecommunity.com/season/fall-winter2017/droplist/2017-11-16/"
		urlink = "https://www.supremecommunity.com"

		content = urlopen(url).read()
		soup = BeautifulSoup(content, 'html.parser')

		no_item = True

		for img in soup.find_all('img'):
			photo = img.get('src')
			if photo[1] == 'u':
				name = img.get('alt')
				photo = urlink+photo
				markup = telebot.types.InlineKeyboardMarkup()
				btn_my_site = telebot.types.InlineKeyboardButton(text='Buy', callback_data=name)
				markup.add(btn_my_site)
				print(name,photo)
				bot.send_message(message.chat.id, name, reply_markup=markup)
				bot.send_photo(message.chat.id, photo)

	if message.text == "New avaliable items":

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

