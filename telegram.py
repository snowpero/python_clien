#-*- coding: utf-8 -*-
import telepot
import json
import urllib2
import requests
import time
import datetime
from pprint import pprint

TOKEN = '241289057:AAFENoDsltc9A3fw_B82Is6k_rt_6F0koRw'
CHAT_ID = '31846052'
BASE_URL = 'https://api.telegram.org/bot' + TOKEN + '/'
PARAM = '?chat_id=' + CHAT_ID + '&text='

bot = telepot.Bot(TOKEN)

def handle(msg):
    pprint(msg)
    chat_msg = msg['text'].encode('utf-8')
    now_date = datetime.datetime.now()
    bot.sendMessage(CHAT_ID, chat_msg + '\n - I am Bot!\nDate : ' + str(now_date))

def initBot():    
    print bot.getMe()    
    print bot.getUpdates()

    bot.message_loop(handle)
    print 'Listening ...........'

    # Keep the program running.
    while 1:
        time.sleep(10)