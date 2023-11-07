from pyrogram import Client, filters
from db import *

@Client.on_message(filters.command(["delkey"], ["/", "."]))
async def process_command(client, message):
    # Comprobar si el remitente del mensaje es un administrador
    sender_id = message.from_user.id
    query = "SELECT * FROM admins WHERE user_id = %s"
    cursor = db.cursor()
    cursor.execute(query, (sender_id,))
    cursor.fetchall()  # Descartar los resultados no leídos
    if cursor.rowcount == 0:
        await message.reply_text("<i>❌ Lo siento, no tienes permiso para ejecutar este comando.</i>")
        return

    # Extraer la clave del comando "/delkey"
    command_parts = message.text.split(" ")
    if len(command_parts) != 2:
        await message.reply_text("<i>❌ Formato incorrecto. Debes usar: /delkey clave</i>")
        return

    key_to_delete = command_parts[1]

    # Verificar si la clave existe en la base de datos
    query_key = "SELECT * FROM users WHERE `key` = %s"
    cursor.execute(query_key, (key_to_delete,))
    key_data = cursor.fetchone()
    if not key_data:
        await message.reply_text("<i>❌ La clave no existe en la base de datos.</i>")
        return

    # Actualizar el estado, los créditos y la fecha de expiración del usuario en la base de datos
    user_id = key_data[0]  # El ID del usuario está en la primera columna
    update_query = "UPDATE users SET status = 'free user', creditos = creditos - 20, `key` = NULL, expiration_date = NULL WHERE user_id = %s"
    cursor.execute(update_query, (user_id,))
    db.commit()

    # Enviar una respuesta al usuario
    await message.reply_text("Se borró la clave y se restaron 20 créditos al usuario con ID {}. La clave y la fecha de expiración se han establecido en NULL.".format(user_id))
