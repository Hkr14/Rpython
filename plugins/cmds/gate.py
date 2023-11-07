from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from db import*



# Establece los detalles de la conexión
@Client.on_message(filters.command("gate"))
async def cmds_command2(client, message):
    # Editar el mensaje según el callback_data
    
    chat_id = message.chat.id
    
    # Obtiene el ID de usuario que generó el evento
    
    user_id = (
    message.from_user.id
)
       
    
    # Crea una conexión a la base de datos
    

    

    # Ejecuta una consulta SQL para buscar al usuario por su User ID
    query = f"SELECT username, status, expiration_date, creditos FROM users WHERE user_id='{user_id}'"
    cursor.execute(query)
    
    # Obtiene el resultado de la consulta
    result = cursor.fetchone()
    if result is None:
        await client.send_message(message.chat.id, "No estás registrado. Por favor, utiliza /register para registrarte.")
        return

    video_path = "https://i.ibb.co/PjpK2ZG/Racext-chk-1-1.png"
    # Verifica el resultado y almacena el valor en la variable "rank"
    if result:
        rank = result[1]
        expiration = result[2]
        creditos = result[3]
    else:
        rank = None

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
    await client.send_video(message.chat.id, video_path, caption=f"""
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
    
<b>[Aviso]:</b> Se Irán Agregando Nuevos Gates....""", reply_markup=keyboard,reply_to_message_id =message.id)

