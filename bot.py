#########################################################
from ast import If
from config import bot
import config
from time import sleep
import re
#########################################################

# Función respuesta al comando help

@bot.message_handler(commands=['help'])
def on_fallback(message):
    bot.send_chat_action(message.chat.id, 'typing')
    sleep(1)
    
    response = (
        "Estos son los comandos y órdenes disponibles:\n"
        "\n"
        "*/start* - Inicia la interacción con el bot\n"
        "*/help* - Muestra este mensaje de ayuda\n"
        "*sumar {valor1} y {valor2}* - Calcula la suma de dos valores\n"
        "*restar {valor1} y {valor2}* - Calcula la resta de dos valores\n"
        "*multiplicar {valor1} y {valor2}* - Calcula la multiplicación de dos valores\n"
        "*dividir {valor1} y {valor2}* - Calcula la división de dos valores\n"
        )
    
    bot.send_message(
        message.chat.id,
        response,
        parse_mode="Markdown")

#########################################################

#Función para resolver comando /start
@bot.message_handler(commands=['start'])
def on_command_start(message):
    bot.send_chat_action(message.chat.id, 'typing')
    sleep(1)
    bot.send_message(
        message.chat.id,
        "Hola, soy un \U0001F916, ¿cómo estás?",
        parse_mode="Markdown")
#########################################################

# Función para Sumar
@bot.message_handler(regexp=r"^sumar ([+-]?([0-9]*[.])?[0-9]+) y ([+-]?([0-9]*[.])?[0-9]+)$")
def on_add(message):
    bot.send_chat_action(message.chat.id, 'typing')
    sleep(1)
    
    parts = re.match(
        r"^sumar ([+-]?([0-9]*[.])?[0-9]+) y ([+-]?([0-9]*[.])?[0-9]+)$",
        message.text,
        flags=re.IGNORECASE)
    
    # print (parts.groups())
    oper1 = float(parts[1])
    oper2 = float(parts[3])
    
    result = oper1 + oper2
    
    bot.reply_to(
        message,
        f"\U0001F913 Resultado: {result}")
#########################################################

# Función para Restar
@bot.message_handler(regexp=r"^restar ([+-]?([0-9]*[.])?[0-9]+) y ([+-]?([0-9]*[.])?[0-9]+)$")
def on_subtract(message):
    bot.send_chat_action(message.chat.id, 'typing')
    sleep(1)
    
    parts = re.match(
        r"^restar ([+-]?([0-9]*[.])?[0-9]+) y ([+-]?([0-9]*[.])?[0-9]+)$",
        message.text,
        flags=re.IGNORECASE)
    
    # print (parts.groups())
    oper1 = float(parts[1])
    oper2 = float(parts[3])
    
    result = oper1 - oper2
    
    bot.reply_to(
        message,
        f"\U0001F913 Resultado: {result}")
#########################################################

# Función para Multiplicar 
@bot.message_handler(regexp=r"^multiplicar ([+-]?([0-9]*[.])?[0-9]+) y ([+-]?([0-9]*[.])?[0-9]+)$")
def on_multiply(message):
    bot.send_chat_action(message.chat.id, 'typing')
    sleep(1)
    
    parts = re.match(
        r"^multiplicar ([+-]?([0-9]*[.])?[0-9]+) y ([+-]?([0-9]*[.])?[0-9]+)$",
        message.text,
        flags=re.IGNORECASE)
    
    # print (parts.groups())
    oper1 = float(parts[1])
    oper2 = float(parts[3])
    
    result = oper1 * oper2
    
    bot.reply_to(
        message,
        f"\U0001F913 Resultado: {result}")

#########################################################

#Función para dividir
@bot.message_handler(regexp=r"^dividir ([+-]?([0-9]*[.])?[0-9]+) y ([+-]?([0-9]*[.])?[0-9]+)$")
def on_divide(message):
    bot.send_chat_action(message.chat.id, 'typing')
    sleep(1)
    
    parts = re.match(
        r"^dividir ([+-]?([0-9]*[.])?[0-9]+) y ([+-]?([0-9]*[.])?[0-9]+)$",
        message.text,
        flags=re.IGNORECASE)
    
    # print (parts.groups())
    oper1 = float(parts[1])
    oper2 = float(parts[3])
    
    if oper2==0:
        bot.reply_to(
            message,
            f"\U0001F628 Lo sentimos, no se puede dividir entre cero.")
        
    result = oper1 / oper2
    
    bot.reply_to(
        message,
        f"\U0001F913 Resultado: {result}")

#########################################################

# Función respuesta por defecto

@bot.message_handler(func=lambda message: True)
def on_fallback(message):
    bot.send_chat_action(message.chat.id, 'typing')
    sleep(1)
    
    bot.reply_to(
        message,
        "\U0001F648 Ups, no entendí lo que me dijiste.")

#########################################################

if __name__ == '__main__':
    bot.polling(timeout=20)
#########################################################