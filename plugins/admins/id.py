from pyrogram import Client, filters



# Comando /ID
@Client.on_message(filters.command("id"))
async def get_id(client, message):
    user_id = message.from_user.id
    chat_id = message.chat.id

    # Verificar si el mensaje es una respuesta a otro mensaje
    if message.reply_to_message:
        replied_user_id = message.reply_to_message.from_user.id
        replied_chat_id = message.reply_to_message.chat.id
        await message.reply_text(
            f"👤 ID del usuario: <code>{replied_user_id}</code>\n"
            f"📌 ID del chat: <code>{chat_id}</code></code>"
        )
    else:
        await message.reply_text(
            f"👤 Tu ID: <code>{user_id}</code>\n"
            f"📌 ID del chat: <code>{chat_id}</code>"
        )


