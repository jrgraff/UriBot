# -*- coding: utf-8 -*-

import telepot
import time

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
        bot.sendMessage(chat_id, "isso foi apenas um teste", reply_to_message_id = msg_id)

TOKEN = sys.argv[1]  # get token from command-line

bot = telepot.Bot(TOKEN)
bot.message_loop(handle)

print('Verificando...')

while 1:
    time.sleep(10)
