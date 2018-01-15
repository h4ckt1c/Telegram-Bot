# Telegram Bot

This is my first bot for telegram written in python. It's origin purpose is to fetch tv-data, e.G. what's running now, or at 20:15.

## Usage

This bot is listening on Telegram and can be found via *@h4ckt1c_tvbot*

## Files

`bot.py` is a "service-ready" python script.

`telegram-bot` can be copied to /etc/init.d to control the bot (start/stop)

OR when using systemd:

`telegram-bot.service` can be copied to /etc/systemd/system to enable/disable/start/stop the bot via `systemctl`

For more informations, see install section.

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

## Installing

If you're using systemd, copy `telegram-bot.service` to `/etc/systemd/system/` and do your changes. After it, perform a `systemctl daemon-reload && systemctl start telegram-bot`.

If you're using sysvinit, copy telegram-bot to `/etc/init.d/` and do your changes. After it, perform a `update-rc.d telegram-bot defaults && update-rc.d telegram-bot enable && service telegram-bot start`.
