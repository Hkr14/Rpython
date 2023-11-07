import os
import asyncio
from configs import Config
from pyrogram import Client
from pyrogram.errors import RPCError, BadRequest
import logging
from termcolor import colored

async def main():
    bot = Client(
        "Sarcehkr",
        api_hash=Config.API_HASH,
        api_id=Config.API_ID,
        bot_token=Config.BOT_TOKEN,
        plugins=dict(root="plugins"),
    )

    @bot.on_callback_query()
    async def callback_privates(client, callback_query):
        reply_message = callback_query.message.reply_to_message
        if reply_message is not None and reply_message.from_user is not None:
            if reply_message.from_user.id != callback_query.from_user.id:
                await callback_query.answer("❗No tienes acceso ❗")
                return
            else:
                await callback_query.continue_propagation()
                return

        # Inserta aquí tu código específico para manejar las consultas de callback
        # ...

        

    try:
        await bot.start()

        # Mensaje de inicio con estilo y colores
        colored_text = colored("Hola Sarce, Soy RaceXtChkBot Estoy A Tus Ordenes 💋", "cyan")
        print(colored_text)

        # Mantener el bot en funcionamiento
        while True:
            await asyncio.sleep(60)  # Esperar 60 segundos antes de volver a verificar eventos

    except Exception as e:
        print(e)
    finally:
        await bot.stop()
    print('iniciado !')

if __name__ == "__main__":
    asyncio.run(main())
