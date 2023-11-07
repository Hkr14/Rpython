import json
import requests
from luhn import *
import time
import asyncio
import re
import colored 
from asyncio import sleep
from pyrogram import Client, filters
from pyrogram.types import (
    Message,
    InlineKeyboardButton,
    InlineKeyboardMarkup
) 

from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.types import (
    Message,
    InlineKeyboardButton,
    InlineKeyboardMarkup
)
from db import*


@Client.on_callback_query()
async def handle_buttons(client, callback_query):
   
    data = callback_query.data
    
    # Obtiene el mensaje y el chat
    
    
    chat_id = message.chat.id
    
    # Obtiene el ID de usuario que generó el evento
    
    user_id = callback_query.from_user.id
    

        # Crea una conexión a la base de datos
    

        # Ejecuta una consulta SQL para buscar al usuario por su User ID
    query = f"SELECT username, status, expiration_date, creditos FROM users WHERE user_id='{user_id}'"
    cursor.execute(query)

        # Obtiene el resultado de la consulta
    result = cursor.fetchone()
    if result is None:
        await client.send_message(message.chat.id, "No estás registrado. Por favor, utiliza /register para registrarte.")
        return

        # Verifica el resultado y almacena el valor en la variable "rank"
    if result:
            global rank
            rank = result[1]
            global expiration
            expiration = result[2]
            global creditos
            creditos = result[3]
    else:
            rank = None
        # Editar el mensaje según el callback_data
        
    global generating_cards
    if generating_cards:
        return

    generating_cards = True
    message = callback_query.message
    inputm = message.text.split(None, 1)[1]
    bincode = 6
    BIN = inputm[:bincode]
    req = requests.get(f"https://bins.antipublic.cc/bins/{BIN}").json()

    brand = req['brand']
    country = req['country']
    country_name = req['country_name']
    country_flag = req['country_flag']
    country_currencies = req['country_currencies']
    bank = req['bank']
    level = req['level']
    typea = req['type']
    input = re.findall(r'[0-9]+', message.text)

    if len(BIN) < 6:
        generating_cards = False
        return await message.edit_text("<b>⎚ Usar <code>/genmass 456789|rnd|rdn|rdn</code></b>")

    if not BIN:
        generating_cards = False
        return await message.edit_text("<b>⎚ Usar <code>/genmass 456789|rnd|rdn|rdn</code></b>")

    tiempoinicio = time.perf_counter()

    if len(input) == 1:
        cc = input[0]
        mes = 'x'
        ano = 'x'
        cvv = 'x'
    elif len(input) == 2:
        cc = input[0]
        mes = input[1]
        ano = 'x'
        cvv = 'x'
    elif len(input) == 3:
        cc = input[0]
        mes = input[1]
        ano = input[2]
        cvv = 'x'
    elif len(input) == 4:
        cc = input[0]
        mes = input[1]
        ano = input[2]
        cvv = input[3]
    else:
        cc = input[0]
        mes = input[1]
        ano = input[2]
        cvv = input[3]

    cc1, cc2, cc3, cc4, cc5, cc6, cc7, cc8, cc9, cc10, = cc_gen(cc, mes, ano, cvv)
    
    tiempofinal = time.perf_counter()
    