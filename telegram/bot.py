# -*- coding: utf-8 -*-
# vim: set fileencoding=utf-8 

import datetime

import urllib
import config
import json
import codecs
import telebot

reader = codecs.getreader("utf-8")

token = '375602165:AAH6-j-iLozcXPOZP90r_6tz_7m2Yu2Nf_Q'

bot = telebot.TeleBot(token)

print('Server started...')

action = ''

@bot.message_handler(commands=['start'])
def start(message):
	msg = bot.send_message(message.chat.id, 'Привет, я бот Центрального банка, выбери опцию:')
	markup = telebot.types.ReplyKeyboardMarkup()
	markup.row('Курс валют')
	markup.row('График валют')
	bot.send_message(message.chat.id, "Выберете опцию", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def process(message):
	rate_lst = {'USD': 'R01235', 'EUR': 'R01239'}

	global action

	date = datetime.datetime.now().strftime('%Y.%m.%d')
	new_date = date[0:5]+str(int(date[5:7])-1)+date[7:len(date)]

	date_rate = datetime.datetime.now().strftime('%d.%m.%Y')

	print('From: '+str(message.from_user.first_name)+' '+str(message.from_user.last_name)+': "'+message.text+'" [ '+date_rate+' ]')

	doc = urllib.urlopen('https://www.cbr.ru/currency_base/daily.aspx?date_req=05.10.2017').read()
	usd = '\xd0\x94\xd0\xbe\xd0\xbb\xd0\xbb\xd0\xb0\xd1\x80 \xd0\xa1\xd0\xa8\xd0\x90'
	buf = doc.find(usd)
	usd = doc[buf+len(usd)+11:buf+len(usd)+18]
	eur = '\xd0\x95\xd0\xb2\xd1\x80\xd0\xbe'
	buf = doc.find(eur)
	eur = doc[buf+len(eur)+11:buf+len(eur)+18]

	rate = {'USD': usd, 'EUR': eur}
	emoji = {'USD': u'\U0001F4B5', 'EUR': u'\U0001F4B6'}

	if  message.text == u'График валют':
		action = 'grafic'
		markup = telebot.types.ReplyKeyboardMarkup()
		markup.row('Назад')
		markup.row('USD', 'EUR')
		bot.send_message(message.chat.id, "Выберете валюту", reply_markup=markup)
	elif message.text == u'Курс валют':
		action = 'rate'
		bot.send_message(message.chat.id, 'Курс валют на дату - '+date+':')
		mes = emoji['USD']+str('USD')+' - '+str(rate['USD'])
		bot.send_message(message.chat.id, mes)
		mes = emoji['EUR']+str('EUR')+' - '+str(rate['EUR'])
		bot.send_message(message.chat.id, mes)
		markup = telebot.types.ReplyKeyboardMarkup()
		markup.row('Назад')
		bot.send_message(message.chat.id, "Пожалуйста...", reply_markup=markup)
	elif message.text == u'Назад':
		markup = telebot.types.ReplyKeyboardMarkup()
		markup.row('Курс валют', 'График валют')
		bot.send_message(message.chat.id, "Выберите опцию", reply_markup=markup)
	elif action == 'grafic':
		if message.text in list(rate_lst.keys()):
			mes = str('График ')+str(message.text)+' на дату - '+date+':'
			bot.send_message(message.chat.id, mes)
			bot.send_photo(message.chat.id, 'https://www.cbr.ru/currency_base/GrafGen.aspx?date_req1={}&date_req2={}&VAL_NM_RQ={}'.format(new_date,date,rate_lst[message.text]))
	elif action == 'rate':
		if message.text in list(rate.keys()):
			a = str(message.text)
			b = 'Курс'
			mes = emoji[message.text]+str(message.text)+': '+str(rate[message.text])
			bot.send_message(message.chat.id, mes)
	else:
		markup = telebot.types.ReplyKeyboardMarkup()
		markup.row('Курс валют')
		markup.row('График валют')
		bot.send_message(message.chat.id, "Извените, я вас не понимаю... Выберете опцию:", reply_markup=markup)

bot.polling()

