#!/usr/bin/env python

from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
from time import ctime
from BeautifulSoup import BeautifulSoup
import requests

secret = open('/root/.telegram-token', 'r').read().strip()

updater = Updater(token=secret)
dispatcher = updater.dispatcher

def fetch_tvdata(time='now'):
    URLbase = "http://www.tvspielfilm.de/tv-programm/rss/"
    if time != 'now':
        URLsuffix = 'heute2015.xml'
        timeprefix =''
    else:
        URLsuffix = 'jetzt.xml'
        timeprefix = 'seit '
    URL = URLbase + URLsuffix

    XML = requests.get(URL).text
    soup = BeautifulSoup(XML)

    whitelist = ["Das Erste", "ZDF", "RTL", "SAT.1", "ProSieben", "kabel eins", "RTL II", "VOX"]
    out = ''

    for item in soup.findAll('item'):
        data = item.find('title').text
        data = data.split("|")
        start = data[0].strip()
        sender = data[1].strip()
        name = data[2].strip()
        if sender in whitelist:
            data = u"{} - {} ({}{})\n".format(name, sender, timeprefix, start)
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
    bot.sendMessage(chat_id=update.message.chat_id, text=fetch_tvdata())

def tv_later(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text=fetch_tvdata('2015'))

updater.start_polling()

dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(MessageHandler(Filters.text, echo))
dispatcher.add_handler(CommandHandler('caps', caps, pass_args=True))
dispatcher.add_handler(CommandHandler('time', time))
dispatcher.add_handler(CommandHandler('tv', tv))
dispatcher.add_handler(CommandHandler('2015', tv_later))
