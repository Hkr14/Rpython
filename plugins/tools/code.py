import aiohttp
import asyncio
import uuid
import random
from pyrogram import Client, filters
from pyrogram.types import Message
import os

# Configura tu token de bot aquí

# Lista de todos los temas disponibles
available_themes = [
    "3024-night", "a11y-dark", "blackboard", "base16-dark", "base16-light",
    "cobalt", "dracula", "duotone-dark", "duotone-light", "hopscotch",
    "lucario", "material", "monokai", "night-owl", "nord", "oceanic-next",
    "one-light", "one-dark", "panda-syntax", "paraiso-dark", "seti",
    "shades-of-purple", "solarized", "solarized-light", "synthwave-84",
    "twilight", "verminal", "yeti", "zenburn"
]
# Función para convertir el mensaje en una imagen de código y enviarla como respuesta
async def convert_to_code_image(client, message):
    if message.reply_to_message and message.reply_to_message.text:
        code = message.reply_to_message.text
        url = "https://carbonara.solopov.dev/api/cook"
        headers = {'Content-Type': 'application/json'}
        unique_id = str(uuid.uuid4())  # Genera un identificador único

        # Genera un color de fondo aleatorio en formato hexadecimal
        random_color = "#{:02x}{:02x}{:02x}".format(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        # Elige un tema aleatorio de la lista de temas disponibles
        random_theme = random.choice(available_themes)

        data = {
            'code': code,
            'backgroundColor': random_color,
            'theme': random_theme,  # Cambia el tema de la terminal
            'watermark': False,
            'name': f'carbon_{unique_id}.png'  # Nombre de archivo único
        }

        # Envía el mensaje "Cargando imagen..."
        loading_message = await message.reply_text("<b>Cargando imagen...</b>")

        async with aiohttp.ClientSession() as session:
            async with session.post(url, json=data) as response:
                if response.status == 200:
                    content = await response.read()
                    filename = f'carbon_{unique_id}.png'
                    with open(filename, 'wb') as f:
                        f.write(content)

                    # Envia la imagen generada como documento
                    sent_message = await message.reply_document(filename)

                    # Elimina el mensaje "Cargando imagen..."
                    await loading_message.delete()

                    # Elimina la imagen generada después de enviarla
                    os.remove(filename)

                    # Elimina fotos generadas previamente con el mismo nombre
                    async for media in client.search_messages(chat_id=message.chat.id, query=f'carbon_{unique_id}.png'):
                        if media.document and media.document.file_name == filename:
                            await client.delete_messages(chat_id=message.chat.id, message_ids=media.message_id)

                else:
                    await loading_message.edit_text("Error al convertir el mensaje en una imagen de código.")
    else:
        await message.reply_text("<b>Debe usarse sobre un texto.</b>\nEjemplo:\n<code>/code</code> (respondiendo a un mensaje que contenga el código)")

# Comando /code para convertir el mensaje en una imagen de código
@Client.on_message(filters.command('code') & (filters.reply | filters.text))
async def code_to_image(client, message: Message):
    await convert_to_code_image(client, message)

