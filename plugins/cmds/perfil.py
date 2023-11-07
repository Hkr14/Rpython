from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from db import *

@Client.on_message(filters.command("info"))
async def cmds_command2(client, message):
    # Comprueba si el mensaje es una respuesta a otro mensaje
    if message.reply_to_message:
        # Obtiene el mensaje al que se está respondiendo
        reply_msg = message.reply_to_message

        # Comprueba si el mensaje tiene un remitente
        if not reply_msg.from_user:
            await message.reply_text("❌ No se pudo obtener la información del usuario.")
            return

        # Obtiene el ID de usuario que generó el mensaje al que se respondió
        user_id = reply_msg.from_user.id

        # Ejecuta una consulta SQL para buscar al usuario por su User ID
        query = f"SELECT username, status, expiration_date, creditos FROM users WHERE user_id='{user_id}'"
        cursor.execute(query)

        # Obtiene el resultado de la consulta
        result = cursor.fetchone()
        if result is None:
            await message.reply_text("El usuario no está registrado.")
            return

        video_path = "https://i.ibb.co/PjpK2ZG/Racext-chk-1-1.png"
        # Verifica el resultado y almacena los valores
        rank, expiration, creditos = result[1], result[2], result[3]

        keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("back", callback_data="back"),
                ]
            ]
        )

        # Envía el perfil del usuario como respuesta al mensaje actual
        await client.send_video(
            message.chat.id,
            video_path,
            caption=f"""
<b>
⊗Information Del Perfil
━━━━━━━━━━━━━━━━━━
⊗ ID: <code>{user_id}</code>
⊗ Rango: <code>{rank}</code>
⊗ Fecha De Expiración: <code>{expiration}</code>
⊗ Créditos: <code>{creditos}</code>
━━━━━━━━━━━━━━━━━━""",
            reply_markup=keyboard,
            reply_to_message_id=message.id
        )
    else:
        # Si no es una respuesta, muestra el perfil del propio usuario
        user_id = message.from_user.id

        # Ejecuta una consulta SQL para buscar el propio perfil del usuario
        query = f"SELECT username, status, expiration_date, creditos FROM users WHERE user_id='{user_id}'"
        cursor.execute(query)

        # Obtiene el resultado de la consulta
        result = cursor.fetchone()
        if result is None:
            await message.reply_text("No estás registrado. Por favor, utiliza /register para registrarte.")
            return

        video_path = "https://i.ibb.co/PjpK2ZG/Racext-chk-1-1.png"
        # Verifica el resultado y almacena los valores
        rank, expiration, creditos = result[1], result[2], result[3]

        keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("back", callback_data="back"),
                ]
            ]
        )

        # Envía el perfil del propio usuario como respuesta al mensaje actual
        await client.send_video(
            message.chat.id,
            video_path,
            caption=f"""<b>

⊗Information Del Perfil
━━━━━━━━━━━━━━━━━━
⊗ ID: <code>{user_id}</code>
⊗ Rango: <code>{rank}</code>
⊗ Fecha De Expiración: <code>{expiration}</code>
⊗ Créditos: <code>{creditos}</code>
━━━━━━━━━━━━━━━━━━""",
            reply_markup=keyboard,
            reply_to_message_id=message.id
        )
