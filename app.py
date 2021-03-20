# -*- coding: utf-8 -*-

import telebot  # Connect with Telegram
import time     # Sleep script
from GoogleNews import GoogleNews   # Get Google News
import json     # Read JSON Files
from datetime import datetime   # Get current time


token = json.loads(open("token.json").read()) # Get the token in "token.json"
bot = telebot.TeleBot(token['token']) # Load bot with token

@bot.message_handler(commands=['start']) # Start command
def main(message):
    chatid = message.chat.id
    print("🆕 L'id utente: " + str(chatid) + " ha appena avviato il bot!")
    bot.reply_to(message, "Benvenuto nel bot Telegram dedicato al bonus Casa 110%! 🏠🎉\nQui riceverai tutti gli aggiornamenti in tempo reale sul Bonus. 📰\nUsa /help per maggiori informazioni sul bot. 🙋")
    

    while True:
        now = datetime.now()    
        current_time = now.strftime("%H:%M:%S")  # Get time  

        print("--- ⚠️ Controllo nuove notizie alle ore: " + current_time)  # Print new scan
            
        googlenews = GoogleNews(lang='it')
        googlenews.search('Bonus casa 110')
        pages_range = range(10)
        for n in pages_range:
            googlenews.get_page(n)
            
        data = googlenews.get_links()   # Get links of news
        print(data)            
        read_newslink = json.loads(open("news.json").read()) # Get the token in "token.json"

        for e in data:  # Scan "data" links array 
            if e in read_newslink:
                pass                    
            else:
                print("⚠️ 🏠Nuova notizia sul Superbonus Casa 110%!\n" + str(e))     # Send messages
                bot.send_message(chatid, "⚠️🏠Nuova notizia sul Superbonus Casa 110%!\n" + str(e))
                json_name = 'news.json' 
                    
                def WritetoJSONFile(path, json_name, data):  # Access JSON
                    filePathNameWExt = './' + json_name
                    with open(filePathNameWExt, 'w') as fp:
                        json.dump(data, fp)

                WritetoJSONFile('./',json_name, data)   # Update news.json
                    
        print("--- ⚠️ Finito controllo in data: " + current_time)    # Print scan refresh
        time.sleep(60)    


@bot.message_handler(commands=['help']) # Help command
def main(message):
    bot.reply_to(message, "❓️ Cosa può fare questo bot?\n➡️ Inoltra gli ultimi annunci e le ultime notizie riguardanti il Superbonus Casa 110%\n❓️ Come posso fermare l'invio delle notizie?\n➡️ Ti basta arrestare e bloccare il bot cliccando sul menù in alto a destra\n❓️ Chi è lo sviluppatore del bot?\n➡️ https://t.me/diskxo ")

print("Bot Online! 🚀🏠")
bot.polling()