import json
import requests
import time
import asyncio
import re
import colored
from asyncio import sleep
from pyrogram import Client, filters
from pyrogram.types import (
    Message,
    InlineKeyboardButton,
    InlineKeyboardMarkup
)
import mysql.connector
from db import *


@Client.on_message(filters.command("admin"))
async def process_admin_command(client, message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    message_id = message.id
    
    if user_id != 1924666696:
        return
    # Verificar si el mensaje contiene el comando y un ID válido
    if not message.text.startswith('/admin'):
        return  # no es un comando /admin, salir sin hacer nada
    
    parts = message.text.split(' ')
    if len(parts) < 2:
        await client.send_message(chat_id, "El formato es: /admin [ID]", reply_to_message_id=message_id)
        return  # el comando /admin está incompleto, salir sin hacer nada
    
    user_id = parts[1].strip()
    # Verificar si el ID del usuario es un número válido
    if not user_id.isnumeric():
        await client.send_message(chat_id, "El ID de usuario debe ser un número", reply_to_message_id=message_id)
        return



    # Conexión a la base de datos
   

    if not db.is_connected():
        await client.send_message(chat_id, "No se pudo conectar a la base de datos", reply_to_message_id=message_id)
        return

    # Crea un cursor para ejecutar consultas
    

    # Ejecuta una consulta SQL para buscar al usuario por su User ID en la tabla admins
    query = f"SELECT username FROM admins WHERE user_id='{user_id}'"
    cursor.execute(query)

    # Obtiene el resultado de la consulta
    result = cursor.fetchone()

    # Si el usuario existe en la tabla admins, muestra un mensaje de confirmación
    if result:
        username = result[0]
        await client.send_message(chat_id, f"El usuario @{username} ya es un admin", reply_to_message_id=message_id)
    else:
        try:
            api_url = f"https://api.telegram.org/bot5970810632:AAGU4ycTrW-HB977ZLndG-qwIBYIoI3WT-M/getChat?chat_id={user_id}"
            api_response = requests.get(api_url).json()
            
            if not api_response["ok"]:
                await client.send_message(chat_id, "No se pudo obtener información del usuario", reply_to_message_id=message_id)
                return
            username = api_response["result"]["username"]
        except Exception as e:
            await client.send_message(chat_id, f"No se pudo obtener el nombre de usuario del ID {user_id}", reply_to_message_id=message_id)
            print(e)
            return

        # Insertar el usuario en la tabla admins
        query = f"INSERT INTO admins (user_id, username) VALUES ('{user_id}', '{username}')"
        cursor.execute(query)
        db.commit()
        await client.send_message(chat_id, f"El usuario @{username} ahora es un admin", reply_to_message_id=message_id)

    
   
