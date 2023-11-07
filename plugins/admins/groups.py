import mysql.connector
import requests
import datetime
from pyrogram import Client, filters
from pyrogram.types import Message
from db import *
from unidecode import unidecode
# Handler para el comando /addgp
@Client.on_message(filters.command(["addgp"], ["/", "."]))
async def add_group_to_database(_, message: Message):
    # Verifica si el usuario tiene permiso para ejecutar el comando
    user_id = message.from_user.id
    query = "SELECT * FROM admins WHERE user_id = %s"
    cursor = db.cursor()
    cursor.execute(query, (user_id,))
    cursor.fetchall()  # Descarta los resultados no leídos
    if cursor.rowcount == 0:
        await message.reply_text("<i>❌ Lo siento, no tienes permiso para ejecutar este comando.</i>")
        return

    # Obtén el ID del grupo y los días de vencimiento del mensaje
    args = message.text.split("|")
    if len(args) != 2:
        await message.reply_text("<i>Formato incorrecto.</i> El comando /addgp debe ser seguido por el ID del grupo y los días de vencimiento separados por '|'. Ejemplo: /addgp -1001610482690|30")
        return

    group_id = args[0].strip().replace("/addgp ", "")  # Elimina el comando "/addgp" y conserva el ID del grupo con el signo "-"
    expiry_days = args[1].strip()

    # Verifica si el ID del grupo y los días de vencimiento son números enteros
    if not group_id.startswith("-") or not group_id[1:].isdigit() or not expiry_days.isdigit():
        await message.reply_text("El ID del grupo y/o los días de vencimiento no son válidos. Asegúrate de ingresar números y un ID de grupo válido con el signo '-'.")
        return

    group_id = int(group_id)
    expiry_days = int(expiry_days)
    url = f"https://api.telegram.org/bot5970810632:AAGU4ycTrW-HB977ZLndG-qwIBYIoI3WT-M/getChat?chat_id={group_id}"
    response = requests.get(url).json()

    if not response['ok'] or 'result' not in response or 'title' not in response['result']:
        # Error al obtener información del grupo
        await message.reply_text(f"No se pudo obtener información del grupo. Asegúrate de proporcionar un ID de grupo válido: {group_id}")
        return

    group_title = response['result']['title']
    group_username = response['result'].get('username')  # Obtiene el valor de 'username', o None si no existe
    if not group_username:
        group_username = unidecode(group_title)
  # Cambiar el formato a minúsculas si no existe 'username'

    # Verifica si el grupo ya está registrado como premium en la base de datos
    query = "SELECT * FROM `groups` WHERE id = %s"
    cursor.execute(query, (group_id,))
    if cursor.fetchone() is not None:
        await message.reply_text(f"<i>❌ oh no!!, El grupo \"{group_title}\" ya está registrado como premium y no puede volver a ser premium.</i>")
        return

    # Calcula la fecha de vencimiento
    expiry_date = (datetime.datetime.now() + datetime.timedelta(days=expiry_days)).date()

    # Inserta el nuevo grupo y la fecha de vencimiento en la tabla "groups"
    query = "INSERT INTO `groups` (id, name, fecha_vencimiento, status) VALUES (%s, %s, %s, 'premium')"
    cursor.execute(query, (group_id, group_username, expiry_date))
    db.commit()

    # Mueve al siguiente conjunto de resultados antes de cerrar el cursor
    cursor.nextset()
    

    # Enviar el mensaje de respuesta
    await message.reply_text(f"<i>El grupo \"{group_title}\" se ha registrado como premium con la fecha de vencimiento.</i>")
