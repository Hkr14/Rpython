from pyrogram import Client, filters
from db import *

@Client.on_message(filters.command(["deldb"], ["/", "."]))
async def process_command(client, message):
    # Extraer el ID de usuario proporcionado después del comando "/deldb"
    sender_id = message.from_user.id
    query = "SELECT * FROM admins WHERE user_id = %s"
    cursor = db.cursor()
    cursor.execute(query, (sender_id,))
    cursor.fetchall()  # Descartar los resultados no leídos
    if cursor.rowcount == 0:
        await message.reply_text("<i>❌ Lo siento, no tienes permiso para ejecutar este comando.</i>")
        return
    command_parts = message.text.split(" ")
    if len(command_parts) != 2 or not command_parts[1].isdigit():
        await message.reply_text("<i>❌ Formato incorrecto. Debes usar: /deldb ID</i>")
        return

    user_id = int(command_parts[1])

    # Eliminar al usuario de la base de datos
    delete_query = "DELETE FROM users WHERE user_id = %s"
    cursor.execute(delete_query, (user_id,))
    db.commit()

    # Enviar una respuesta al usuario
    await message.reply_text("El usuario con ID {} fue eliminado de la base de datos.".format(user_id))

# Definir y ejecutar el bucle de eventos
