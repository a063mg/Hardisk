import config
import json
import requests

token = '375602165:AAH6-j-iLozcXPOZP90r_6tz_7m2Yu2Nf_Q'

api = 'https://api.telegram.org/bot{}/{}'

def getRequest(url):
	request = requests.get(url)
	return request.json()

def sendMessage(chat_id, message):
	method = 'sendMessage'
	params = method+'?chat_id={}&text={}'.format(chat_id, message)
	print(api.format(token, params))
	result = requests.get(api.format(token, params))

req = getRequest(api.format(token,'getUpdates'))

last_request = req['result'][-1]
update_id = last_request['update_id']

last_update_id = update_id

while True:
	req = getRequest(api.format(token,'getUpdates'))

	last_request = req['result'][-1]
	update_id = last_request['update_id']

	if update_id != last_update_id:
		print(update_id, last_update_id)
		message = last_request['message']
	
		text_message = str(message['text'])
		chat_id = message['chat']['id']

		sendMessage(chat_id, text_message)
		

	last_update_id = update_id