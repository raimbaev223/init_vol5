import telebot
import logging

from config import TOKEN
from get_weather import get_weather, get_news
from weather_btns import *

bot = telebot.TeleBot(TOKEN)
telebot.logger.setLevel(logging.DEBUG)
news_list = get_news()


@bot.message_handler(commands=['help', 'start'])
def hello(msg):
    message = bot.send_message(msg.chat.id, "Hello i'am weather bot press the button to find out the weather",
                               reply_markup=btns)
    bot.register_next_step_handler(message, choice_step)


def choice_step(msg):
    if msg.text == 'Новости' or msg.text == 'Еще новости':

        message = bot.send_message(msg.chat.id, news_list.pop(0), reply_markup=next)
        bot.register_next_step_handler(message, choice_step)
    elif msg.text == 'Узнать погоду':
        message = bot.send_message(msg.chat.id, 'Выберите город', reply_markup=cityes)
        bot.register_next_step_handler(message, show_weather)


# @bot.callback_query_handler(func=lambda call: True)
def show_weather(msg):
    if msg.text == 'Бишкек':
        city = 'bishkek'
    elif msg.text == 'Кара-Балта':
        city = 'kara-balta'
    elif msg.text == 'Кант':
        city = 'kant'
    elif msg.text == 'Сокулук':
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

    message = bot.send_message(msg.chat.id, message, reply_markup=btns)
    bot.register_next_step_handler(message, choice_step)


bot.polling(logging)
