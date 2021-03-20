<p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="https://i.imgur.com/Y1CGZ3g.png" alt="Bot logo"></a>
</p>

<h3 align="center">110 Tidings | Telegram bot</h3>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![GitHub Issues](https://img.shields.io/github/issues/diskxo/110-Tidings.svg)](https://github.com/diskxo/The-Documentation-Compendium/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/diskxo/110-Tidings.svg)](https://github.com/diskxo/110-Tidings/pulls)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

---

<p align="center"> 🤖 Bot Telegram realizzato in Python, con la funzione di inoltrare in chat gli ultimi annunci e le ultime notizie riguardanti il Superbonus Casa 110% attualmente presente in Italia.
    <br> 
</p>

## 📝 Table of Contents

- [About](#about)
- [How it works](#working)
- [Usage](#usage)
- [Getting Started](#getting_started)
- [Built Using](#built_using)
- [Authors](#authors)

## 🧐 About <a name = "about"></a>

🤖 Bot Telegram realizzato in Python, con la funzione di inoltrare in chat gli ultimi annunci e le ultime notizie riguardanti il Superbonus Casa 110% attualmente presente in Italia.<br>


## 💭 How it works <a name = "working"></a>

Questo script esegue ogni x secondi lo scraping delle pagine "news" di Google riguardanti il bonus 110% Case, e confronta i link trovati con quelli presenti nel file "news.json", cosi da capire se si tratta di una notizia inviata in precedenza oppure di un nuovo aggiornamento da inviare alla chat Telegram.

L'intero bot è scritto in Python 3.6

## 🎈 Usage <a name = "usage"></a>

Per utilizzare il bot su Telegram, recati al link:
http://t.me/bonus110_bot , 
e avvialo con il comando /start . 
Da quel momento riceverai una notifica ad ogni aggiornamento.
Altri comandi disponibili sono:

/help = Fornisce informazioni sul funzionamento del bot

### Prerequisites

E' necessario installare Python e Pipin locale per poter avviare il bot tramite console.

Le seguenti librerie sono richieste per il corretto funzionamento dello script:

```console
diskxo@main:~$ sudo pip install pyTelegramBotAPI==0.3.0 GoogleNews
```

### Installing


Utilizzando questo comando (avendo installato Git su Pc locale)
```
diskxo@main:~$ git clone https://github.com/diskxo/110-Tidings
```
Potrai avere una copia locale del bot.
Ti basterà infine creare un file chiamato "token.json"
e inserire il token del tuo bot di Telegram per completare l'installazione

```
diskxo@main:~/110-tidings $ touch token.json
```


## 🚀 Deploying your own bot <a name = "deployment"></a>

Per lanciare il bot ti basterà spostarti sulla repository clonata e lanciare il comando:
```console
diskxo@main:~/110-tidings $ python app.py
```

## ⛏️ Built Using <a name = "built_using"></a>

- [Python](https://www.python.org/) - Linguaggio di programmazione utilizzato
- [VSCode](https://code.visualstudio.com/) - Text Editor utilizzato
- [Telegram-Bot](https://github.com/python-telegram-bot/python-telegram-bot) - Libreria per comunicare con il bot di Telegram
- [GoogleNews](https://pypi.org/project/GoogleNews/) - Libreria per scraping delle notizie su Google
## ✍️ Authors <a name = "authors"></a>

- [@diskxo](https://github.com/diskxo) - Idea & Realizzazione

