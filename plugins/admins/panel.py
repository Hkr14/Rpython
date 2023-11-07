from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import mysql.connector
import random
from db import*
# Define the filter for the /panel command
@Client.on_message(filters.command(["panel"], ["/", ".", ","]))
async def panel_command(client, message):
    user_id = message.from_user.id
    
    # Crea un cursor para ejecutar consultas
    

    # Ejecuta una consulta SQL para buscar al usuario por su User ID
    query = "SELECT * FROM admins WHERE user_id = %s"
    cursor.execute(query, (user_id,))
    cursor.fetchall()  # Descarta los resultados no leídos
    if cursor.rowcount == 0:
        await message.reply_text("<i>❌ Lo siento, no tienes permiso para ejecutar este comando.</i>")
        return

    # Send a random video with a caption
    video_urls = [
        "https://tenor.com/es-MX/view/bunny-gif-22123827",
        "https://tenor.com/es-MX/view/bunny-gif-22123827",
        "https://tenor.com/es-MX/view/bunny-gif-22123827"
    ]

    # Obtener la lista de videos ya enviados
    sent_videos = getattr(client, "sent_videos", [])

    # Verificar si se han enviado todos los videos disponibles
    if len(sent_videos) == len(video_urls):
        # Se han enviado todos los videos, restablecer la lista de sent_videos
        sent_videos = []

    # Seleccionar un video aleatorio que no se haya enviado anteriormente
    video_path = None
    while not video_path:
        random_video = random.choice(video_urls)
        if random_video not in sent_videos:
            video_path = random_video

    # Agregar el video a la lista de sent_videos
    sent_videos.append(video_path)

    # Actualizar la lista de sent_videos en el cliente
    setattr(client, "sent_videos", sent_videos)

    caption = """
<b>Bienvenido admin, Estos Son Los Comandos Nuestros</b>
<i>

/addgp + id y días del plan

/key tipo_plan|días

/ban id|razon

/unapremium id

/deldb

/unban
</i>"""

    # Create the buttons
    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("📿 Perfil", callback_data="me"),
            ]
        ]
    )

    # Send the video with the caption and buttons
    await client.send_video(message.chat.id, video_path, caption=caption, reply_markup=keyboard)
