# -*- coding: utf-8 -*-

import sys
import telepot
import time
from urinotas import getNotas

def handle(msg):
    try:
        command = msg['text']
    except:
        command = "<ARQUIVO>"
    msg_id = msg['message_id']
    chat_id = msg['chat']['id']
    from_id = msg['from']['id']
    
    command = command.split(' ')

    if command[0] == '/notas':
        try:
            notas = getNotas(command[1], command[2])
            for nota in notas.keys():
                resultado =  nota + '\n' + notas[nota]
            bot.sendMessage(chat_id, resultado, reply_to_message_id = msg_id)
        except:
            bot.sendMessage(chat_id, "Digite como o exemplo '/notas <pasta> <senha>'", reply_to_message_id = msg_id)

TOKEN = sys.argv[1]  # get token from command-line

bot = telepot.Bot(TOKEN)
bot.message_loop(handle)

print('Verificando...')

while 1:
    time.sleep(10)
