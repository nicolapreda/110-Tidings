# -*- coding: utf-8 -*-

import telebot  # Connect with Telegram
from bs4 import BeautifulSoup   # Find elements in pages
from fake_useragent import UserAgent    # Fake header agent
import requests     # Inspect page
import time     # Sleep script
from GoogleNews import GoogleNews
import json 


token = json.loads(open("token.json").read()) # Get the token in "token.json"
bot = telebot.TeleBot(token['token']) # Load bot with token

@bot.message_handler(commands=['start']) #Welcome message
def main(message):
    bot.reply_to(message, "Benvenuto! Qui riceverai tutte le notizie riguardanti il Bonus Casa 110%")

    googlenews = GoogleNews(lang='it')
    googlenews.search('Bonus casa 110')
    data = googlenews.get_links()   # Get links of news
    
    while True:
        read_newslink = json.loads(open("news.json").read()) # Get the token in "token.json"

        for e in data:
            if e in read_newslink:
                pass    
            else:
                print("Nuova notizia trovata!\n")
                print(e)
                bot.reply_to(message, "Nuova notizia!\n" + str(e))
                json_name = 'news.json' 
                
                def WritetoJSONFile(path, json_name, data):  # Access JSON
                    filePathNameWExt = './' + json_name
                    with open(filePathNameWExt, 'w') as fp:
                        json.dump(data, fp)

                WritetoJSONFile('./',json_name, data)
        
        time.sleep(10)

print("Bot Online! 🚀")
bot.polling()