# Telegram Bot

This is my first bot for telegram written in python. It's origin purpose is to fetch tv-data, e.G. what's running now, or at 20:15.

## Usage

This bot is listening on Telegram and can be found via *@h4ckt1c_tvbot*

## Files

`bot.py` is a "service-ready" python script.

`telegram-bot` can be copied to /etc/init.d to control the bot (start/stop)

## Commands

The folling commands are available:

* `/help` prints this text
* `/time` prints current time and date
* `/start` used to start this bot and prints welcome message
* `/caps {patter}` prints _{pattern}_ UPPERCASE
* `/tv` prints current tv program
* `/2015` prints tv program for today 20:15

## External Data

The commands `/tv` and `/2015` parses data from [TV-Spielfilm](http://www.tvspielfilm.de/tv-programm/rss/) and prints it out.
