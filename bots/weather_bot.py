import telebot
import logging

from config import TOKEN
from get_weather import get_weather
from weather_btns import *

bot = telebot.TeleBot(TOKEN)
telebot.logger.setLevel(logging.DEBUG)


@bot.message_handler(commands=['help', 'start'])
def hello(msg):
    message = bot.send_message(msg.chat.id, "Hello i'am weather bot press the button to find out the weather",
                     reply_markup=btns)
    bot.register_next_step_handler(message, choice_city)


def choice_city(msg):
    message = bot.send_message(msg.chat.id, 'Выберите город', reply_markup=cityes)
    bot.register_next_step_handler(message, show_weather)


@bot.callback_query_handler(func=lambda call: True)
def show_weather(msg):
    if msg.data == 'bishkek':
        city = 'bishkek'
    elif msg.data == 'kara-balta':
        city ='kara-balta'
    elif msg.data == 'kant':
        city = 'kant'
    elif msg.data == 'sokuluk':
        city = 'sokuluk'

    weather = get_weather(city)
    temp = weather['temp']
    feels_like = weather['feels_like']
    sunrise = weather['sunrise']
    sunset = weather['sunset']
    wind = weather['wind']

    message = f"Здравствуйте.\n" \
              f"Температура {temp} °C.\n" \
              f"Ощущается как {feels_like} °C.\n" \
              f"Восход солнца в {sunrise}, заход в {sunset}.\n" \
              f"Скорость ветра {wind}м/c."

    message = bot.send_message(msg.message.chat.id, message)
    bot.register_next_step_handler(message, choice_city)
    bot.send_message(msg.message.chat.id, 'Выберите город', reply_markup=cityes)


bot.polling(logging)
