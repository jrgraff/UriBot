#!/usr/bin/python3
#-*- coding: utf-8 -*-

import sys
import telepot
import time, datetime

from random import randint
from urinotas import getNotas

pasta = sua_pasta
senha = sua_senha
meu_id = id_do_seu_grupo

def verificaNota():
    try:
        for key in notasOld.keys():
            if notasOld[key] != getNotas(pasta, senha)[key]:
                return "Notas de %s lançadas" % key
        return "False"
    except:
        return "ETA PORRA DEU ERRO AQUI VÉI!!"

def handle(msg):
    command = msg['text']
    msg_id = msg['message_id']
    chat_id = msg['chat']['id']

    if command == '/start':
        bot.sendMessage(chat_id, "Hi, It's %s" % time.ctime(), reply_to_message_id = msg_id)

TOKEN = sys.argv[1]  # get token from command-line

bot = telepot.Bot(TOKEN)
bot.message_loop(handle)

#log para controle
notasOld = getNotas(pasta, senha)
print(notasOld.keys())

while 1:
    time.sleep(randint(1500, 4000))
    now = datetime.datetime.now()
    if 8 <= now.hour <= 22:
        status = verificaNota()
        bot.sendMessage(meu_id, status)
        #log para controle
        print("Verificado as: %s - %s" % (time.ctime(), status)) 
