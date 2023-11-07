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





# Establece los detalles de la conexion

generating_cards = False
@Client.on_message(filters.command(["gen"], ["/", "."]))
async def genmass(client, message):
        
            username = message.from_user.username

            user_id = (
    message.from_user.id
)
     
    
       
            # Crea un cursor para ejecutar consultas
            


        
            
            # Ejecuta una consulta SQL para buscar al usuario por su User ID
            query = f"SELECT status FROM users WHERE user_id='{user_id}'"
            cursor.execute(query)
             
        # Obtiene el resultado de la consulta
            result = cursor.fetchone()
            if result is None:
             await message.reply_text("No estás registrado. Por favor, utiliza /register para registrarte.")
             return
            # Verifica el resultado y almacena el valor en la variable "rank"
        
            rank = result[0]
        
            
            input = re.findall(r'[0-9]+',message.text)
            BIN = message.text[len("/bin"): 11]
            if len(BIN) <6:
                return await message.reply("<b>⎚ Usar <code>/gen 456789|rnd|rdn|rdn</code></b>")
            if not BIN:
                return await message.reply("<b>⎚ Usar <code>/gen 456789|rnd|rdn|rdn</code></b>")
                apibincito = 6
                BIN = inputm[:apibinsito]
        
        
            tiempoinicio = time.perf_counter()

            if len(input) == 1:
                cc = input[0]
                mes = 'x'
                ano = 'x'
                cvv = 'x'
            elif len(input) ==2:
                cc = input[0]
                mes = input[1]
                ano = 'x'
                cvv = 'x'
            elif len(input) ==3:
                cc = input[0]
                mes = input[1]
                ano = input[2]
                cvv = 'x'
            elif len(input) ==4:
                cc = input[0]
                mes = input[1]
                ano = input[2]
                cvv = input[3]
            else:
                cc = input[0]
                mes = input[1]
                ano = input[2]
                cvv = input[3]

            cc1,cc2,cc3,cc4,cc5,cc6,cc7,cc8,cc9,cc10, = cc_gen(cc,mes,ano,cvv)

            tiempofinal = time.perf_counter()
            await message.reply_text(f"""<b>
⎚ Gen Ccs  [ 🥀 ]
━━
<code>{cc1}</code>
<code>{cc2}</code>
<code>{cc3}</code>
<code>{cc4}</code>
<code>{cc5}</code>
<code>{cc6}</code>
<code>{cc7}</code>
<code>{cc8}</code>
<code>{cc9}</code>
<code>{cc10}</code>
━━━ 
<b><i>Take</i></b> : <code>{tiempofinal - tiempoinicio:0.2} seconds</code>
━━━━━━━━━━━━━━━━━━━━━━
⎚ Create <b><a href="tg://resolve?domain=Sarcehkr">SarceDev[Owner]</a></b>
            </b>"""

        )
        else:
            return await message.reply(f'<b>⎚ Registrese <code>/register</code></b>')
        
        buttons = [
            [
                InlineKeyboardButton("Regen", callback_data="callback_data_1"),
            ],

        ]

        keyboard = InlineKeyboardMarkup(buttons)

        def luhn_verification(num):
            num = [int(d) for d in str(num)]
            check_digit = num.pop()
            num.reverse()
            total = 0
            for i,digit in enumerate(num):
                if i % 2 == 0:
                    digit = digit * 2
                if digit > 9:
                    digit = digit - 9
                total += digit
            total = total * 9
            return (total % 10) == check_digit



        def cc_genmass(cc,mes='x',ano='x',cvv='x'):
            ccs = []
            while len(ccs) < 10:
                card = str(cc)
                digits = '04567896789'
                list_digits = list(digits)
                random.shuffle(list_digits)
                string_digits = ''.join(list_digits)
                card = card + string_digits
                if card[0] == '3':
                    card = card[0:15]
                else:
                    card = card[0:16]

                if mes == 'x':
                    mes_genmass = random.randint(1,12)
                    if len(str(mes_genmass)) == 1:
                        mes_genmass = '0' + str(mes_genmass)
                else:
                    mes_genmass = mes

                if ano == 'x':
                    ano_genmass = random.randint(2023,2031)
                else:
                    ano_genmass = ano
                    if len(str(ano_genmass)) == 2:
                        ano_genmass = '20' + str(ano_genmass)

                if cvv == 'x':
                    if card[0] == '3':
                        cvv_genmass = random.randint(1000,9999)
                    else:
                        cvv_genmass = random.randint(100,999)
                else:
                    cvv_genmass = cvv

                x = str(card) + '|' + str(mes_genmass) + '|' + str(ano_genmass) + '|' + str(cvv_genmass)    
                a = luhn_verification(card)
                if a:
                    ccs.append(x)
                else:
                    continue

            return ccs
