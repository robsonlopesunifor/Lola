
#!/usr/bin/python3
#coding: utf-8
import telepot, time
from core.menu import Menu
from datetime import date, timedelta

caminho = []

def principal(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)    
    chat_id = msg['chat']['id']
    mensagem = msg['text']
    resposta = Menu().chat(content_type, mensagem)
    if resposta:
        bot.sendMessage(chat_id,resposta)


bot = telepot.Bot('6293729431:AAGMg3IvVrP7FC4grj5kwXhlwzUZUQ1f8zI')
bot.message_loop(principal)

while 1:
    time.sleep(5)