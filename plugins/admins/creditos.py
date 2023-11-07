from pyrogram import Client, filters
from db import *

@Client.on_message(filters.command(["creditos"], ["/", "."]))
async def process_command(client, message):
    # Extraer el ID de usuario y la cantidad de créditos proporcionados después del comando "/creditos"
    # Comprobar si el remitente del mensaje es un administrador
    sender_id = message.from_user.id
    query = "SELECT * FROM admins WHERE user_id = %s"
    cursor = db.cursor()
    cursor.execute(query, (sender_id,))
    await cursor.fetchall()  # Descartar los resultados no leídos
    if cursor.rowcount == 0:
        await message.reply_text("<i>❌ Lo siento, no tienes permiso para ejecutar este comando.</i>")
        return
    command_parts = message.text.split(" ")
    if len(command_parts) != 2:
        await message.reply_text("<i>❌ Formato incorrecto. Debes usar: /creditos ID|cantidad</i>")
        return

    user_id, creditos_str = command_parts[1].split("|")
    if not user_id.isdigit() or not creditos_str.isdigit():
        await message.reply_text("<i>❌ Formato incorrecto. Debes usar: /creditos ID|cantidad</i>")
        return

    user_id = int(user_id)
    creditos = int(creditos_str)

    # Actualizar la cantidad de créditos del usuario en la base de datos
    update_query = "UPDATE users SET creditos = %s WHERE user_id = %s"
    cursor.execute(update_query, (creditos, user_id))
    db.commit()

    # Enviar una respuesta al usuario
    await message.reply_text("Se actualizaron los créditos del usuario con ID {} a {}.".format(user_id, creditos))
