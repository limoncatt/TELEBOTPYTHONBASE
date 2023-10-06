import telebot
import random

API_TOKEN = 'YOURTOKEN'

bot = telebot.TeleBot(API_TOKEN)

whatmedointoday = [ "BACK-END" , "FRONT-END" ]

@bot.message_handler(commands=['start'])
def startmess(message):
    bot.send_message(message.chat.id, "Hello, i'm a base bot for testing.")

@bot.message_handler(commands=['help'])
def starthelp(message):
    bot.send_message(message.chat.id, "Send /test to check what are you doing today")

@bot.message_handler(commands=['test'])
def startrandom(message):
    bot.send_message(message.chat.id, random.choice(whatmedointoday))

bot.polling(none_stop=True)