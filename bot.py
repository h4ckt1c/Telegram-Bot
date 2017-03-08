#!/usr/bin/env python

from telegram import ChatAction
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
from time import ctime
from BeautifulSoup import BeautifulSoup
import requests

secret = open('/root/.telegram-token', 'r').read().strip()

updater = Updater(token=secret)
dispatcher = updater.dispatcher

def fetch_tvdata(bot, update, time='now'):
    bot.sendChatAction(chat_id=update.message.chat_id, action=ChatAction.TYPING)
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
    bot.sendMessage(chat_id=update.message.chat_id, text="Hi, I'm a bot. You can ask me what's running in TV ;)")

def tv(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text=fetch_tvdata(bot, update))

def tv_later(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text=fetch_tvdata(bot, update, '2015'))

def helpme(bot, update):
    helptext = """Available commands:
`/help` prints this text
`/start` used to start this bot and prints welcome message
`/tv` prints current tv program
`/2015` prints tv program for today 20:15
"""
    bot.sendMessage(chat_id=update.message.chat_id, text=helptext, parse_mode='Markdown')

dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('tv', tv))
dispatcher.add_handler(CommandHandler('2015', tv_later))
dispatcher.add_handler(CommandHandler('help', helpme))

updater.start_polling()
updater.idle()
