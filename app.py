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

@bot.message_handler(commands=['start']) # Start command
def main(message):
    chatid = message.chat.id
    print("🆕 L'id utente: " + str(chatid) + " ha appena avviato il bot!")
    bot.reply_to(message, "Benvenuto nel bot Telegram dedicato al bonus Casa 110%! 🏠🎉\nQui riceverai tutti gli aggiornamenti in tempo reale sul Bonus. 📰\nUsa /help per maggiori informazioni sul bot. 🙋")

    googlenews = GoogleNews(lang='it')
    googlenews.search('Bonus casa 110')
    pages_range = range(10)
    for n in pages_range:
        googlenews.get_page(n)
    
    data = googlenews.get_links()   # Get links of news
    
    while True:
        read_newslink = json.loads(open("news.json").read()) # Get the token in "token.json"

        for e in data:
            if e in read_newslink:
                pass    
            else:
                print("⚠️🏠Nuova notizia sul Superbonus Casa 110%!\n" + str(e))
                bot.send_message(chatid, "⚠️🏠Nuova notizia sul Superbonus Casa 110%!\n" + str(e))
                json_name = 'news.json' 
                
                def WritetoJSONFile(path, json_name, data):  # Access JSON
                    filePathNameWExt = './' + json_name
                    with open(filePathNameWExt, 'w') as fp:
                        json.dump(data, fp)

                WritetoJSONFile('./',json_name, data)
        
        time.sleep(60)


@bot.message_handler(commands=['help']) # Help command
def main(message):
    bot.reply_to(message, "❓️ Cosa può fare questo bot?\n➡️ Inoltra gli ultimi annunci e le ultime notizie riguardanti il Superbonus Casa 110%\n❓️ Come posso fermare l'invio delle notizie?\n➡️ Ti basta arrestare e bloccare il bot cliccando sul menù in alto a destra\n❓️ Chi è lo sviluppatore del bot?\n➡️ https://t.me/diskxo ")

print("Bot Online! 🚀🏠")
bot.polling()