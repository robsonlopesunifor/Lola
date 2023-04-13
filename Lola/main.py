import sys
import time

from random import randrange
from typing import List

import telepot

from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardButton
from telepot.namedtuple import InlineKeyboardMarkup

sys.path.append("/app")
from Lola.configs import settings
from Lola.services.bocuse.service import BocuseService

caminho: List[str] = []


VERSION = settings.PROJECT_VERSION
BANCO = {}


def banco_dados(dados):
    chave = str(randrange(1000, 9999))
    BANCO[chave] = dados
    return chave


def menu(chat_id):
    categorias = BocuseService().menu()
    list_keyboard = []
    for categoria in categorias:
        cardapio_name = categoria["name"]
        data = {"chat_id": chat_id, "etapa": "cardapio", "cardapio": cardapio_name}
        chave = banco_dados(data)
        keyboar_button = InlineKeyboardButton(text=cardapio_name, callback_data=chave)
        list_keyboard.append(keyboar_button)
    keyboard = InlineKeyboardMarkup(inline_keyboard=[list_keyboard])
    bot.sendMessage(chat_id, "___________ Menu ___________", reply_markup=keyboard)


def cardapio(dados):
    cardapio = dados["cardapio"]
    receitas = BocuseService().cardapio(cardapio)
    chat_id = dados["chat_id"]
    keyboard = []
    for receita in receitas:
        receita_name = receita["name"]
        receita_id = receita["id"]
        data = {"chat_id": chat_id, "etapa": "receita", "receita_id": receita_id}
        chave = banco_dados(data)
        keyboar_button = InlineKeyboardButton(text=receita_name, callback_data=chave)
        keyboard.append([keyboar_button])
    keyboard = InlineKeyboardMarkup(inline_keyboard=keyboard)
    bot.sendMessage(
        chat_id,
        f"___________ Receitas de {cardapio} ___________",
        reply_markup=keyboard,
    )


def receita(dados):
    chat_id = dados["chat_id"]
    receita_id = dados["receita_id"]
    text_informacoes = BocuseService().informacoes(receita_id)
    texto_ingredientes = BocuseService().ingredientes(receita_id)
    texto_equipamentos = BocuseService().equipamentos(receita_id)
    texto_preparos = BocuseService().preparos(receita_id)
    bot.sendMessage(chat_id, text_informacoes)
    bot.sendMessage(chat_id, texto_ingredientes)
    bot.sendMessage(chat_id, texto_equipamentos)
    bot.sendMessage(chat_id, texto_preparos)


def callback_function(msg):
    query_id, from_id, query_data = telepot.glance(msg, flavor="callback_query")
    callback_data = BANCO[query_data]
    if callback_data["etapa"] == "cardapio":
        cardapio(callback_data)
    elif callback_data["etapa"] == "receita":
        receita(callback_data)
    # bot.answerCallbackQuery(query_id, text=query_data)
    # bot.sendMessage(callback_data["chat_id"], callback_data["cardapio"])


def principal(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    palavra_chave = msg["text"]
    if palavra_chave.upper() == "OI":
        menu(chat_id)


bot = telepot.Bot("6293729431:AAGMg3IvVrP7FC4grj5kwXhlwzUZUQ1f8zI")

MessageLoop(
    bot, {"chat": principal, "callback_query": callback_function}
).run_as_thread()


while 1:
    time.sleep(5)
