import mysql.connector
import requests
import datetime
from pyrogram import Client, filters
from pyrogram.types import Message
from db import *
import os
from os.path import isfile



@Client.on_message(filters.command(["binbanned"], ["/", "."]))
async def bin_banned_command(_, message: Message):
    user_id = message.from_user.id
    query = "SELECT * FROM admins WHERE user_id = %s"
    cursor.execute(query, (user_id,))
    cursor.fetchall()  # Descarta los resultados no leídos
    if cursor.rowcount == 0:
        await message.reply_text("<i>❌ Lo siento, no tienes permiso para ejecutar este comando.</i>")
        return
    
    # Verificar si se proporcionaron bins
    if len(message.command) < 2:
        await message.reply_text("Debes proporcionar uno o más bins de 6 dígitos.")
        return

    bins = message.command[1:]

    banned_file = "bin_banned.txt"

    with open(banned_file, "a+") as file:
        file.seek(0)  # Colocar el puntero al inicio del archivo
        banned_bins = file.read().splitlines()

        with open(banned_file, "a") as file:
            for bin_code in bins:
                # Verificar la longitud del bin
                if len(bin_code) != 6 or not bin_code.isdigit():
                    await message.reply_text(f"El bin '{bin_code}' no es válido. Los bins deben tener 6 dígitos numéricos.")
                    continue

                # Verificar si el bin ya está en la lista
                if bin_code in banned_bins:
                    await message.reply_text(f"El bin '{bin_code}' ya está en la lista de bins prohibidos.")
                    continue

                # Agregar el bin a la lista
                file.write(bin_code + "\n")

    await message.reply_text("Bins añadidos a la lista de bins prohibidos.")
