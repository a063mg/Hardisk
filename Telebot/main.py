import telebot

bot = telebot.TeleBot('375602165:AAH6-j-iLozcXPOZP90r_6tz_7m2Yu2Nf_Q')

update = bot.get_updates()

last_update = update[-1]

message = last_update.message

print(message.text)
# bot.send(chat_id, 'Hello yourself')

@bot.message_handler(content_type=['text'])
def handle_message(message):
	print('TESST')
	bot.send_message(message.chat.id, 'Hello Yourself')



bot.polling(none_stop=True, interval=0)