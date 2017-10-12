# -*- coding: utf-8 -*-

import sys
import telepot
import time, datetime
from urinotas import getNotas

now = datetime.datetime.now()

pasta = pasta
senha = senha
meu_id = asdasd

def verificaNota():
    try:
        if notasOld == getNotas(pasta, senha):
	    return "False"
        return "True"
    except:
        return "Verifique o codigo pois aconteceu algum erro"

def handle(msg):
    command = msg['text']
    msg_id = msg['message_id']
    chat_id = msg['chat']['id']

    if command == '/start':
        bot.sendMessage(chat_id, "Não sei como você me achou mas eu só funciono para meu criador. Me desculpe", reply_to_message_id = msg_id)

TOKEN = sys.argv[1]  # get token from command-line

bot = telepot.Bot(TOKEN)
bot.message_loop(handle)
notasOld = getNotas(pasta, senha)

print('Verificando...')

while 1:
    if 8 <= now.hour <= 22:
    	time.sleep(25)
    	bot.sendMessage(seu_id, verificaNota())
