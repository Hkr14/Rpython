from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import mysql.connector
import asyncio
import random

# Conexión a la base de datos
from db import *
# Función para obtener los IDs de los usuarios desde la base de datos
# Función para obtener los IDs de los usuarios desde la base de datos
async def obtener_ids_usuarios():
    query = "SELECT user_id FROM users"
    cursor.execute(query)
    resultados = cursor.fetchall()
    ids_usuarios = [str(row[0]) for row in resultados]
    return ids_usuarios

# Lista de URLs de imágenes disponibles
imagen_urls = [
    "https://telegra.ph/file/b162c4cb02fc4eb22cab6.jpg",
    "https://telegra.ph/file/b4905d24fd9fc05ef7be1.jpg",
    "https://telegra.ph/file/37321258f56d8ac29fd54.jpg"
]

# Crea el objeto del cliente de Pyrogram


# Comando para enviar mensajes a todos los usuarios
@Client.on_message(filters.command("mensaje", prefixes="/"))
async def enviar_mensaje_privado(client, message):
    # Obtiene el ID del remitente del mensaje
    remitente_id = message.from_user.id

    # Lee los IDs permitidos desde el archivo 'owner.txt'
    with open('owner.txt', 'r') as file:
        ids_permitidos = file.read().splitlines()

    # Verifica si el ID del remitente está permitido
    if str(remitente_id) not in ids_permitidos:
        mensaje_no_permiso = "Lo siento, no tienes permisos para hacer esto."
        await client.send_message(message.chat.id, mensaje_no_permiso)
        return

    # Obtiene el mensaje personalizado después del comando
    mensaje_personalizado = message.text.split(maxsplit=1)[1]

    # Envía un mensaje de confirmación al remitente
    mensaje_confirmacion = "El mensaje se está enviando a todos los usuarios."
    await client.send_message(message.chat.id, mensaje_confirmacion)

    # Obtiene los IDs de los usuarios desde la base de datos
    ids_usuarios = await obtener_ids_usuarios()

    # Envía el mensaje personalizado y la imagen a todos los usuarios en paralelo
    tasks = []
    for user_id in ids_usuarios:
        try:
            # Selecciona una imagen aleatoria de la lista de imagen_urls
            imagen_url = random.choice(imagen_urls)
            keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("Grupo Oficial", url="https://t.me/RaceXtChk"),
                InlineKeyboardButton("Owner", url="https://t.me/Sarcehkr"),
            ],
        
        ]
    )
            # Envía la imagen junto con el mensaje personalizado como leyenda
            task = client.send_photo(user_id, imagen_url, caption=f"<b>{mensaje_personalizado}</b>",reply_markup=keyboard)
            tasks.append(task)
        except Exception as e:
            error_msg = f"Error al enviar mensaje a {user_id}: {str(e)}"
            await client.send_message(message.chat.id, error_msg)

    # Espera a que se completen todas las tareas de envío de mensajes
    await asyncio.gather(*tasks)

    # Muestra un mensaje cuando se ha enviado el mensaje a todos los usuarios
    mensaje_enviado = "El mensaje se ha enviado a todos los usuarios."
    await client.send_message(message.chat.id, mensaje_enviado)
