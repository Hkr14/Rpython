from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import mysql.connector
from db import *
import asyncio
import re
import colored 
from asyncio import sleep
from gengen import *
# Define the filter for the /cmds command
@Client.on_message(filters.command(["cmds","start"], ["/", "."]))
async def cmds_command(client, message):
    # Send a video with a caption
    
    user_id = message.from_user.id


        # Ejecuta una consulta SQL para buscar al usuario por su User ID
    query = f"SELECT username, status, expiration_date, creditos FROM users WHERE user_id='{user_id}'"
    cursor.execute(query)

        # Obtiene el resultado de la consulta
    result = cursor.fetchone()
    if result is None:
        await client.send_message(message.chat.id, "No estás registrado. Por favor, utiliza /register para registrarte.")
        return
    video_path = "https://i.ibb.co/PjpK2ZG/Racext-chk-1-1.png"
    caption = """
<b><a href="tg://resolve?domain=RaceXtChkBot">RaceXtBot • [🤖]</a>\n\n¡Hola! Soy RaceXtChkBot Estoy A Tus Ordenes ¿Quieres Conocer Mis funciones? Primero Debes Registrarte Con /register\n\nPodras Utilizar Mis Gstes Y herramientas Gratis Solo En El Grupo Oficial Muchas Gracias.
OWNER: <b><a href="tg://resolve?domain=Sarcehkr">SarceDev[Owner]</a></b>
</b>"""

    # Create the buttons
    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("⊗ tools", callback_data="tools"),
                InlineKeyboardButton("⊗ Gateways", callback_data="gates"),
            ],
            [
                InlineKeyboardButton("⊗ Staff", callback_data="adm"),
            ]
        ]
    )

    # Send the message with the video, caption, and buttons
    await client.send_photo(message.chat.id, video_path, caption=caption, reply_markup=keyboard,reply_to_message_id =message.id)
# Establece los detalles de la conexión

# Handle the button responses
@Client.on_callback_query()
async def handle_buttons(client, callback_query):
   

    
 #  Obtiene el callback_data del botón presionado
    
    data = callback_query.data
    
    # Obtiene el mensaje y el chat
    message = callback_query.message
    
    chat_id = message.chat.id
    
    # Obtiene el ID de usuario que generó el evento
    
    user_id = callback_query.from_user.id
    
    db = mysql.connector.connect(
        host="185.214.132.8",
        user="u943517844_racextpy",
        password="Cesar0728.",
        database="u943517844_racextpy"
    )
    cursor = db.cursor()

        # Crea una conexión a la base de datos
    

        # Ejecuta una consulta SQL para buscar al usuario por su User ID
    query = f"SELECT username, status, expiration_date, creditos FROM users WHERE user_id='{user_id}'"
    cursor.execute(query)

        # Obtiene el resultado de la consulta
    result = cursor.fetchone()
    if result is None:
        await client.send_message(message.chat.id, "No estás registrado. Por favor, utiliza /register para registrarte.")
        return

        # Verifica el resultado y almacena el valor en la variable "rank"
    if result:
            global rank
            rank = result[1]
            global expiration
            expiration = result[2]
            global creditos
            creditos = result[3]
    else:
            rank = None
        # Editar el mensaje según el callback_data
        
    if data == "tools":
            keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("back", callback_data="back"),
              
                InlineKeyboardButton("close", callback_data="cerrar"),
                 InlineKeyboardButton("→", callback_data="siguiente"),
            ],

            
                
            
        ]
    )

            # Editar el mensaje para el botón "tools"
            await client.edit_message_caption(chat_id, message.id, caption="""
<b>Herramientas</b>
                                              
⎚ Bin - <code>FREE</code>
⎚ Usar <code>/bin 456789</code>
━━━━━━━━━
⎚ Gen Ccs - <code>OFF</code>
⎚ Usar <code>/gen 456789|rnd|rdn|rdn</code>
━━━━━━━━━
⎚ Gen Mass Ccs <code>FREE</code>
⎚ Usar <code>/genmass 456789|rnd|rnd|rnd</code>
━━━━━━━━━
⎚ Tu informacion - <code>FREE</code>
⎚ Usar <code>/info </code>
━━━━━━━━━
⎚ Info Del bot user - <code>FREE</code>
⎚ Usar <code>/me</code>
━━━━━━━━━""",reply_markup=keyboard)
    if data == "siguiente":
            keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("back", callback_data="tools"),
              
                InlineKeyboardButton("close", callback_data="cerrar"),
                 
            ],

            
                
            
        ]
    )

            # Editar el mensaje para el botón "tools"
            await client.edit_message_caption(chat_id, message.id, caption="""
<b>HERRAMIENTAS</b>
                                              
━━━━━━━━━
⎚ Rand - <code>FREE</code>
⎚ Usar <code>/rand </code> 
━━━━━━━━━
⎚ Rand Pais - <code>FREE</code>
⎚ Usar <code>/rdn ar</code>
━━━━━━━━━
⎚ Zip code Postal - <code>FREE</code>
⎚ Usar <code>/zip 10020</code>
━━━━━━━━━
⎚ Extra - <code>FREE</code>
⎚ usar <code>/exta 4115680117164577-4178490024082621</code>""",reply_markup=keyboard)
    elif data == "cerrar":
             keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("⊗ Open Back", callback_data="back"),
                
            ],
            
                
            
        ]
    )
            # Editar el mensaje para el botón "tools"
             await client.edit_message_caption(chat_id, message.id, caption="""
""",reply_markup=keyboard)
   
   
    elif data == "principio":
             keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("⊗ tools", callback_data="tools"),
                InlineKeyboardButton("⊗ Gateways", callback_data="gates"),
            ],
            [
                InlineKeyboardButton("⊗ Staff", callback_data="adm"),
            ]
        ]
    )

            # Editar el mensaje para el botón "tools"
             await client.edit_message_caption(chat_id, message.id, caption="""
<b>Hola Mi nombre es RaceXtChk, presiona los botones a continuación para saber más sobre mí</b>""",reply_markup=keyboard)
 
    elif data == "back":
             keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("⊗ tools", callback_data="tools"),
                InlineKeyboardButton("⊗ Gateways", callback_data="gates"),
            ],
            [
                InlineKeyboardButton("⊗ Staff", callback_data="adm"),
            ]
        ]
    )

            # Editar el mensaje para el botón "tools"
             await client.edit_message_caption(chat_id, message.id, caption="""
<b>Hola Mi nombre es RaceXtChk,presiona los botones a continuación para saber más sobre mí</b>""",reply_markup=keyboard)
 
 
    elif data == "gates":
            keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("auth", callback_data="auth"),
                InlineKeyboardButton("charged", callback_data="charged"),
            ],
            [
                InlineKeyboardButton("back", callback_data="back"),
            ]
        ]
    )
            # Editar el mensaje para el botón "gates"
            await client.edit_message_caption(chat_id, message.id, caption="""
━━━━[𝙍𝙖𝙘𝙚𝙓𝙩𝘾𝙝𝙠𝘽𝙤𝙩]━━━━

※𝙂𝙖𝙩𝙚𝙬𝙖𝙮𝙨 𝘼𝙪𝙩𝙝
※𝘼𝙘𝙩𝙞𝙫𝙤𝙨             [3]
※𝘼𝙥𝙖𝙜𝙖𝙙𝙤𝙨        [2]

※𝙂𝙖𝙩𝙚𝙬𝙖𝙮𝙨 𝘾𝙝𝙖𝙧𝙜𝙚𝙙
※𝘼𝙘𝙩𝙞𝙫𝙤𝙨             [4]
※𝘼𝙥𝙖𝙜𝙖𝙙𝙤𝙨        [3]

※𝙂𝙖𝙩𝙚𝙬𝙖𝙮𝙨 𝙈𝙖𝙨𝙨
※𝘼𝙘𝙩𝙞𝙫𝙤𝙨             [0]
※𝘼𝙥𝙖𝙜𝙖𝙙𝙤𝙨        [1]
    
<b>[Aviso]:</b> Se Irán Agregando Nuevos Gates....""",reply_markup=keyboard)
    elif data == "back1":
        keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("auth", callback_data="auth"),
                InlineKeyboardButton("charged", callback_data="charged"),
            ],
            [
                InlineKeyboardButton("back", callback_data="back"),
            ]
        ]
    )
            # Editar el mensaje para el botón "gates"
        await client.edit_message_caption(chat_id, message.id, caption="""
━━━━[𝙍𝙖𝙘𝙚𝙓𝙩𝘾𝙝𝙠𝘽𝙤𝙩]━━━━

※𝙂𝙖𝙩𝙚𝙬𝙖𝙮𝙨 𝘼𝙪𝙩𝙝
※𝘼𝙘𝙩𝙞𝙫𝙤𝙨             [3]
※𝘼𝙥𝙖𝙜𝙖𝙙𝙤𝙨        [2]

※𝙂𝙖𝙩𝙚𝙬𝙖𝙮𝙨 𝘾𝙝𝙖𝙧𝙜𝙚𝙙
※𝘼𝙘𝙩𝙞𝙫𝙤𝙨             [4]
※𝘼𝙥𝙖𝙜𝙖𝙙𝙤𝙨        [3]

※𝙂𝙖𝙩𝙚𝙬𝙖𝙮𝙨 𝙈𝙖𝙨𝙨
※𝘼𝙘𝙩𝙞𝙫𝙤𝙨             [0]
※𝘼𝙥𝙖𝙜𝙖𝙙𝙤𝙨        [1]
    
<b>[Aviso]:</b> Se Irán Agregando Nuevos Gates....""",reply_markup=keyboard)
       
    elif data == "auth":
            keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("back", callback_data="back1"),
                InlineKeyboardButton("close", callback_data="cerrar"),
            ],
            [
                InlineKeyboardButton("home", callback_data="principio"),
            ]
        ]
    )
            # Editar el mensaje para el botón "gates"
            await client.edit_message_caption(chat_id, message.id, caption="""
╔━━「𝙂𝙖𝙩𝙚𝙬𝙖𝙮𝙨 𝘼𝙪𝙩𝙝」━━╗

𝙂𝙖𝙩𝙚𝙬𝙖𝙮 - ↯  Denver [Premium]
𝙁𝙤𝙧𝙢𝙖𝙩𝙤 - ↯  /rp cc|mm|yy|cvv
𝙋𝙖𝙨𝙖𝙧𝙚𝙡𝙖 - ↯  Stripe Auth
𝙎𝙩𝙖𝙩𝙪𝙨 - ↯  Activo✅
- - - - - - - - - - - - - -
𝙂𝙖𝙩𝙚𝙬𝙖𝙮 - ↯  Medellin [Premium]
𝙁𝙤𝙧𝙢𝙖𝙩𝙤 - ↯  /md cc|mm|yy|cvv
𝙋𝙖𝙨𝙖𝙧𝙚𝙡𝙖 - ↯ Stripe Auth
𝙎𝙩𝙖𝙩𝙪𝙨 - ↯  Activo✅
- - - - - - - - - - - - - -
𝙂𝙖𝙩𝙚𝙬𝙖𝙮 - ↯  Auth [Premium]
𝙁𝙤𝙧𝙢𝙖𝙩𝙤 - ↯  /auth cc|mm|yy|cvv
𝙋𝙖𝙨𝙖𝙧𝙚𝙡𝙖 - ↯  Stripe Auth
𝙎𝙩𝙖𝙩𝙪𝙨 - ↯  Activo✅
- - - - - - - - - - - - - -
𝙂𝙖𝙩𝙚𝙬𝙖𝙮 - ↯  Italia [Premium]
𝙁𝙤𝙧𝙢𝙖𝙩𝙤 - ↯  /bra cc|mm|yy|cvv
𝙋𝙖𝙨𝙖𝙧𝙚𝙡𝙖 - ↯  Braintree Auth
𝙎𝙩𝙖𝙩𝙪𝙨 - ↯  Actualizacion⚠️
- - - - - - - - - - - - - -
𝙂𝙖𝙩𝙚𝙬𝙖𝙮 - ↯  Brasil [Free]
𝙁𝙤𝙧𝙢𝙖𝙩𝙤 - ↯  /bs cc|mm|yy|cvv
𝙋𝙖𝙨𝙖𝙧𝙚𝙡𝙖 - ↯  Stripe Auth
𝙎𝙩𝙖𝙩𝙪𝙨 - ↯  Actualizacion⚠️
- - - - - - - - - - - - -""",reply_markup=keyboard)
    elif data == "charged":
                keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("back", callback_data="back1"),
                InlineKeyboardButton("close", callback_data="cerrar"),
            ],
            [
                InlineKeyboardButton("home", callback_data="principio"),
            ]
        ]
    )
            # Editar el mensaje para el botón "gates"
                await client.edit_message_caption(chat_id, message.id, caption="""
━━「𝙂𝙖𝙩𝙚𝙬𝙖𝙮 𝘾𝙝𝙖𝙧𝙜𝙚𝙙」━━

𝙂𝙖𝙩𝙚𝙬𝙖𝙮 - ↯ Rusia [Premium]
𝙁𝙤𝙧𝙢𝙖𝙩𝙤 - ↯  /rt cc|mm|yy|cvv
𝙋𝙖𝙨𝙖𝙧𝙚𝙡𝙖 - ↯  Stripe Charged
𝙎𝙩𝙖𝙩𝙪𝙨 - ↯  Activo✅

𝙂𝙖𝙩𝙚𝙬𝙖𝙮 - ↯ Bogota [Premium]
𝙁𝙤𝙧𝙢𝙖𝙩𝙤 - ↯  /bg cc|mm|yy|cvv
𝙋𝙖𝙨𝙖𝙧𝙚𝙡𝙖 - ↯ Stripe Charged
𝙎𝙩𝙖𝙩𝙪𝙨 - ↯  Activo✅

𝙂𝙖𝙩𝙚𝙬𝙖𝙮 - ↯  Roma [Premium]
𝙁𝙤𝙧𝙢𝙖𝙩𝙤 - ↯  /bo cc|mm|yy|cvv
𝙋𝙖𝙨𝙖𝙧𝙚𝙡𝙖 - ↯  Braintree
𝙎𝙩𝙖𝙩𝙪𝙨 - ↯  ACTIVO✅

𝙂𝙖𝙩𝙚𝙬𝙖𝙮 - ↯ Francia [Premium]
𝙁𝙤𝙧𝙢𝙖𝙩𝙤 - ↯  /ac cc|mm|yy|cvv
𝙋𝙖𝙨𝙖𝙧𝙚𝙡𝙖 - ↯  Braintree
𝙎𝙩𝙖𝙩𝙪𝙨 - ↯  OFF❌

𝙂𝙖𝙩𝙚𝙬𝙖𝙮 - ↯ Manchester [Premium]
𝙁𝙤𝙧𝙢𝙖𝙩𝙤 - ↯  /stp cc|mm|yy|cvv
𝙋𝙖𝙨𝙖𝙧𝙚𝙡𝙖 - ↯  Stripe Charged
𝙎𝙩𝙖𝙩𝙪𝙨 - ↯  Activo✅

𝙂𝙖𝙩𝙚𝙬𝙖𝙮 - ↯ Arabia [Premium]
𝙁𝙤𝙧𝙢𝙖𝙩𝙤 - ↯  /sh cc|mm|yy|cvv
𝙋𝙖𝙨𝙖𝙧𝙚𝙡𝙖 - ↯  Shopify
𝙎𝙩𝙖𝙩𝙪𝙨 - ↯  OFF❌


𝙂𝙖𝙩𝙚𝙬𝙖𝙮 - ↯ Paypal [Premium]
𝙁𝙤𝙧𝙢𝙖𝙩𝙤 - ↯  /pp cc|mm|yy|cvv
𝙋𝙖𝙨𝙖𝙧𝙚𝙡𝙖 - ↯  Paypal
𝙎𝙩𝙖𝙩𝙪𝙨 - ↯  Activo✅""",reply_markup=keyboard)
    elif data == "adm":
            keyboard = InlineKeyboardMarkup(
        [
       
            [
                InlineKeyboardButton("Grupo Oficial", url="https://t.me/RaceXtChkOficial"),
            ]
        ]
    )
            # Editar el mensaje para el botón "me"
            await client.edit_message_caption(chat_id, message.id, caption=f"""<b>
👤ADMINISTRACION RACEXTBOT
━━━━━━━━━━━━━━━━━━
⊗ OWNER: <b><a href="tg://resolve?domain=Sarcehkr">SarceDev[Owner]</a></b>
⊗ ADMIN: <b><a href="tg://resolve?domain=ChorizoConQueso">Alecarrera186</a></b>
⊗ ADMIN: <b><a href="tg://resolve?domain=axelguzman06">Axel</a></b>
⊗ ADMIN: <b><a href="tg://resolve?domain=ImCharmeleon">ImCharmeleon</a></b>
⊗ ADMIN: <b><a href="tg://resolve?domain=Blar351">Lal</a></b>
━━━━━━━━━━━━━━━━━━""",reply_markup=keyboard)
     
    
  
                
