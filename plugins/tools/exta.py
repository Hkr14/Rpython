from pyrogram import Client, filters
import re

# Define el filtro para capturar los mensajes que contienen el comando "/exta"
@Client.on_message(filters.command(["exta"], ["/", "."]))
# Obtener el texto después del comando
def extrapolate_advanced(client, message):
    # Obtener el texto después del comando
    text = message.text[len("/exta "):]

    # Verificar el formato del texto
    if '-' not in text:
        message.reply_text("Formato incorrecto. Debe ser: /exta 4115680117164577-4178490024082621")
        return

    # Extraer los dos números de tarjeta
    t1, t2 = text.split("-")

    # Realizar los cálculos según el método de extrapolación avanzada
    t1_group2_sum = int(t1[7]) + int(t1[8])
    t2_group2_sum = int(t2[7]) + int(t2[8])

    t1_result = int((t1_group2_sum / 2) * 5)
    t2_result = int((t2_group2_sum / 2) * 5)

    # Sumar los resultados de la extrapolación
    total_result = t1_result + t2_result

    # Combinar los resultados para formar el número de tarjeta extrapolado
    extrapolated_card = f"{t1[:7]} {total_result:03d}xx xxxx"

    # Responder con el número de tarjeta extrapolado
    message.reply_text(f"El resultado de la extrapolación avanzada es:\n{extrapolated_card}")


