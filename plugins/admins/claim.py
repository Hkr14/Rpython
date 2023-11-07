import json
import requests
import asyncio
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

# Resto del código ...

# Comando /claim para reclamar una clave
@Client.on_message(filters.command('claim', prefixes='/'))
async def reclamar_clave(client: Client, message: Message):
    user_id = message.from_user.id
    comando, *argumentos = message.text.split(' ', 1)

    if not argumentos:
        await message.reply('<i>❌ Formato incorrecto. Uso: /claim clave</i>')
        return

    argumentos = argumentos[0]

    comando, key = message.text.split(' ', 1)
    key = key.strip()

    # Verificar si el usuario ha alcanzado el límite de intentos fallidos

    select_query = "SELECT * FROM users WHERE user_id = %s"
    select_data = (user_id,)
    cursor.execute(select_query, select_data)
    user_data = cursor.fetchone()

    if user_data:
        warns = user_data[5]  # Obtener el número de warns del usuario
        print(warns)
        if warns is None:
            warns = 0  # Valor predeterminado de warns

        # Resto del código ...

        if int(warns) >= 4:
            # El usuario ha alcanzado el límite de warns, baneado temporalmente
            await message.reply('<b>❌ Estás temporalmente baneado. No puedes usar este comando en las próximas 12 horas.</b>')
            return

        # Verificar si la clave existe y está disponible en la tabla keyuser
        select_query = "SELECT * FROM keyuser WHERE `clave` = %s AND `status` = 'Premium'"
        select_data = (key,)
        cursor.execute(select_query, select_data)
        result = cursor.fetchone()

        if result:
            # La clave es válida y está disponible
            key_data = result  # Datos de la clave obtenidos de la tabla keyuser
            expiration_date = key_data[3]  # Obtener la fecha de vencimiento de la clave
            plan_expiry = key_data[3]  # Obtener el planexpiry de la clave

            # Convertir la fecha de vencimiento a formato legible
            expiration_date = expiration_date.strftime('%Y-%m-%d')

            # Resto del código ...

            await message.reply('<b>✅ Clave reclamada exitosamente. Se han sumado 20 créditos a tu cuenta.</b>')
        else:
            # La clave no es válida
            warns += 1  # Incrementar el número de warns del usuario

            if int(warns) >= 4:
                # El usuario ha alcanzado el límite de warns, baneado temporalmente
                update_query = "UPDATE users SET `warns` = %s, `status` = 'Banned', `ban_expiration` = %s WHERE user_id = %s"
                ban_expiration = datetime.now() + timedelta(hours=12)  # Establecer el tiempo de expiración del ban
                update_data = (warns, ban_expiration, user_id)
                cursor.execute(update_query, update_data)
                db.commit()

                await message.reply('<b>❌ Estás temporalmente baneado. No puedes usar este comando en las próximas 12 horas.</b>')
            else:
                # Resto del código ...

                await message.reply('<b>❌ La clave no es válida.</b>')
    else:
        return


