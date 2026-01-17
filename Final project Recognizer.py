import os
from googletrans import Translator
import telebot
from dotenv import load_dotenv
load_dotenv()
bot=telebot.TeleBot(os.getenv("TG_API_TOKEN"))

tr=Translator()

@bot.message_handler(commands=['start'])
def s(m):
    bot.reply_to(m,"Привет! Пришли текст на русском — я переведу на английский.")

@bot.message_handler(func=lambda m: m.text and not m.text.startswith('/'))
def h(m):
    bot.reply_to(m, tr.translate(m.text, src='ru', dest='en').text)

bot.polling()
