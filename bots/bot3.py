from config import TOKEN
import telebot
from telebot.types import *

bot = telebot.TeleBot(TOKEN)

user_dict = {}


class User:
    def __init__(self, name):
        self.name = name
        self.age = None
        self.sex = None


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    msg = bot.reply_to(message, "Hi there, I am Example Bot. What's your name?")
    bot.register_next_step_handler(msg, process_name_step)


def process_name_step(message):
    try:
        chat_id = message.chat.id
        name = message.text
        user = User(name)
        user_dict[chat_id] = user
        msg = bot.reply_to(message, 'How old are you?')
        bot.register_next_step_handler(msg, process_age_step)
    except Exception as ex:
        bot.reply_to(message, "OOOOPS!")


def process_age_step(message):
    try:
        chat_id = message.chat.id
        age = message.text
        if not age.isdigit():
            msg = bot.reply_to(message, "Age should be a number. How old are you?")
            bot.register_next_step_handler(msg, process_age_step)
            return
        user = user_dict[chat_id]
        user.age = age
        markup = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        markup.add('Male', 'Female')
        msg = bot.reply_to(message, "What is your gender", reply_markup=markup)
        bot.register_next_step_handler(msg, process_sex_step)
    except Exception as ex:
        bot.reply_to(message, "OOOOPS!")


def process_sex_step(message):
    try:
        chat_id = message.chat.id
        sex = message.text
        user = user_dict[chat_id]
        if (sex == u"Male") or (sex == u"Female"):
            user.sex = sex
        else:
            raise Exception("Unknown sex")
        text = 'Nice to meet you ' + user.name + '\n Age:' + str(user.age) + '\n Sex:' + user.sex
        bot.send_message(chat_id, text)
        with open("users.txt", 'a') as file:
            file.write(text + '\n')

    except Exception as ex:
        bot.reply_to(message, "OOOOPS!")


bot.enable_save_next_step_handlers(delay=2)
bot.load_next_step_handlers()
bot.polling()
