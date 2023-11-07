from pyrogram import Client, filters
from deep_translator import GoogleTranslator
from langdetect import detect

# Función asincrónica para traducir un mensaje a un idioma específico
async def translate_message_to_language(text, dest_language):
    source_language = detect(text)
    try:
        translated_text = await GoogleTranslator(source=source_language, target=dest_language).translate_async(text)
        return translated_text
    except Exception as e:
        print(f"Error en la traducción: {e}")
        return None

# Obtener el código de idioma de dos letras a partir del nombre del idioma
def get_language_code(language_name):
    # Puedes personalizar esta función para obtener los códigos de idioma que necesites
    # Por ejemplo, si tienes un diccionario propio con códigos de idioma.
    # Aquí, simplemente retornamos el nombre del idioma tal cual.
    return language_name

# Obtener el nombre del idioma a partir del código de dos letras
def get_language_name(language_code):
    # Puedes personalizar esta función para obtener los nombres de idioma que necesites
    # Por ejemplo, si tienes un diccionario propio con nombres de idioma.
    # Aquí, simplemente retornamos el código de idioma tal cual.
    return language_code

# Manejador del comando /trad
@Client.on_message(filters.command(["trad"], ["/", "."]))
async def translate_message(client, message):
    # Si se responde a un mensaje, utilizamos el texto del mensaje respondido
    if message.reply_to_message and message.reply_to_message.text:
        text_to_translate = message.reply_to_message.text
    else:
        # Si no se responde a un mensaje, tomamos el texto del comando después de /trad
        text_to_translate = " ".join(message.command[1:])

    if not text_to_translate:
        await message.reply_text("Por favor, incluye un mensaje para traducir.")
        return

    # Verificamos si el mensaje está en español
    if detect(text_to_translate) == 'es':
        await message.reply_text("Lo siento, el mensaje ya está en español, no puedo traducirlo.")
        return

    # Si se proporciona un idioma después del comando, utilizamos ese idioma para la traducción.
    # Por ejemplo: /trad en Hola
    if len(message.command) >= 3:
        dest_language = get_language_code(message.command[1])
        text_to_translate = " ".join(message.command[2:])
    else:
        dest_language = "es"  # Idioma predeterminado si no se proporciona un idioma específico.

    translated_text = await translate_message_to_language(text_to_translate, dest_language)

    if translated_text is None:
        await message.reply_text("Ocurrió un error durante la traducción.")
        return

    source_language = detect(text_to_translate)
    source_language_name = get_language_name(source_language)
    dest_language_name = get_language_name(dest_language)

    response_text = f"""
    Traducción ({source_language_name} ➜ {dest_language_name}): 
{translated_text}"""
    await message.reply_text(response_text)


