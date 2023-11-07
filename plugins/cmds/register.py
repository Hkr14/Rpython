import mysql.connector
from pyrogram import Client, filters
from db import *

@Client.on_message(filters.command(["register", ".register", "registrar", "register@RaceXtChk"]))
async def register_command(client, message):
    # Verifica si el usuario ya está registrado en la base de datos
    user_id = message.from_user.id
    cursor = db.cursor()
    username = message.from_user.username
    query = f"SELECT * FROM users WHERE user_id = '{user_id}'"
    cursor.execute(query)
    result =  cursor.fetchone()

    if result:
        # El usuario ya está registrado
        await client.send_message(
            chat_id=message.chat.id,
            text="<i>❌Ya estás registrado.</i>"
        )
    else:
        # Registra al usuario como free user en la base de datos
        insert_query = f"INSERT INTO users (user_id, username, status, expiration_date, creditos, warns) VALUES ('{user_id}', '{username}', 'free user', NULL, 0, NULL)"
        cursor.execute(insert_query)
        db.commit()
        await client.send_message(
            chat_id=message.chat.id,
            text="<i>¡Te has registrado correctamente!</i>"
        )
