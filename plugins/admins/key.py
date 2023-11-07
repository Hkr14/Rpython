import asyncio
import json
import requests
import re
from pyrogram import Client, filters
from pyrogram.types import (
    Message,
    InlineKeyboardButton,
    InlineKeyboardMarkup
)
import random
import string
from datetime import datetime, timedelta
import mysql.connector
from db import cursor, db 
import datetime

def random_string(length):
    characters = string.digits + string.ascii_lowercase
    return ''.join(random.choice(characters) for _ in range(length))

async def generar_clave():
    clave_existe = True
    clave = ''

    while clave_existe:
        two = random_string(4)
        three = random_string(4)
        four = random_string(4)
        clave = f'AzunaChkBot-{two}{three}{four}'

        cursor = db.cursor()
        select_query = "SELECT * FROM keyuser WHERE clave = %s"
        select_data = (clave,)
        cursor.execute(select_query, select_data)
        result = cursor.fetchone()

        if not result:
            # La clave no existe en la base de datos, es única
            clave_existe = False

    return clave

@Client.on_message(filters.command('key', prefixes='/'))
async def generar_y_almacenar_clave(client: Client, message: Message):
    comando, *argumentos = message.text.split(' ', 1)
    # Ejecuta una consulta SQL para buscar al usuario por su User ID
    query = "SELECT * FROM admins WHERE user_id = %s"
    user_id = message.from_user.id
    cursor = db.cursor()
    cursor.execute(query, (user_id,))
    cursor.fetchall()  # Descarta los resultados no leídos
    if cursor.rowcount == 0:
        await message.reply_text("<i>❌ Lo siento, no tienes permiso para ejecutar este comando.</i>")
        return
    if not argumentos:
        # No se proporcionaron argumentos, mostrar formato de uso
        await message.reply('<i>❌ Formato incorrecto. Uso: /key [tipo_plan|dias|fecha_expiracion]</i>')
        return
    
    argumentos = argumentos[0]
    
    if '|' in argumentos:
        comando_plan, *opciones = argumentos.split('|')
        plantype = comando_plan.split()[-1] if len(comando_plan.split()) > 1 else 'Premium'
        dias = None
        fecha_expiracion = None
        
        for opcion in opciones:
            opcion = opcion.strip()
            if opcion.isdigit():
                dias = int(opcion)
            else:
                try:
                    fecha_expiracion = datetime.datetime.strptime(opcion, '%Y-%m-%d')
                except ValueError:
                    pass
        
        if dias is not None:
            # Si se proporciona el número de días, calcular la fecha de expiración sumando los días a la fecha actual
            fecha_actual = datetime.datetime.now()
            fecha_expiracion = fecha_actual + datetime.timedelta(days=dias)
    else:
        plantype = 'Premium'  # Valor predeterminado si no se especifica un plan
    
    clave_generada = await generar_clave()
    
    # Insertar la clave en la base de datos
    insert_query = "INSERT INTO keyuser (clave, status, planexpiry) VALUES (%s, %s, %s)"
    insert_data = (clave_generada, plantype, fecha_expiracion)
    cursor = db.cursor()
    cursor.execute(insert_query, insert_data)
    db.commit()
    
    await message.reply(f'<b>♻️ Key creada exitosamente</b>\n'
                        f'━━━━━━━━━━━━━━━━━━\n'
                        f'<i>⚜️ Key:</i> <code>{clave_generada}</code>\n'
                        f'<i>➤ Rango:</i> <code>{plantype}</code>\n'
                        f'<i>📛 Fecha De Expiración:</i> <code>{fecha_expiracion.strftime("%Y-%m-%d")}</code>\n'
                        f'━━━━━━━━━━━━━━━━━━')

# Definir y ejecutar el bucle de eventos

