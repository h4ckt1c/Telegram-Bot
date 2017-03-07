#!/usr/bin/env python

from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
from time import ctime
from BeautifulSoup import BeautifulSoup
import requests
from secret import secret

print secret

updater = Updater(token=secret)
dispatcher = updater.dispatcher

def tv_2015(sender):
    URL = ""

def tv_now():
    URL = "http://www.tvspielfilm.de/tv-programm/rss/jetzt.xml"
    XML = requests.get(URL).text

    whitelist = ["Das Erste", "ZDF", "RTL", "SAT.1", "ProSieben", "kabel eins", "RTL II", "VOX"]

    soup = BeautifulSoup(XML)

    out = ""

    for item in soup.findAll('item'):
        data = item.find('title').text
        data = data.split("|")
        start = data[0].strip()
        sender = data[1].strip()
        name = data[2].strip()
        if sender in whitelist:
            data = u"{} - {} (seit {})\n".format(name, sender, start)
            out += data

    return out

def start(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")

def echo(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text=update.message.text)

def caps(bot, update, args):
    text_caps = ''.join(args).upper()
    bot.sendMessage(chat_id=update.message.chat_id, text=text_caps)

def time(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text=ctime())

def tv(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text=tv_now())

updater.start_polling()

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(echo_handler)

caps_handler = CommandHandler('caps', caps, pass_args=True)
dispatcher.add_handler(caps_handler)

time_handler = CommandHandler('time', time)
dispatcher.add_handler(time_handler)

tv_handler = CommandHandler('tv', tv)
dispatcher.add_handler(tv_handler)
