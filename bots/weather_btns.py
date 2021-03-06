from telebot.types import KeyboardButton, ReplyKeyboardMarkup, \
    InlineKeyboardMarkup, InlineKeyboardButton


weather = KeyboardButton('Узнать погоду')
btns = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True).add(weather)

bishkek = InlineKeyboardButton(text='Бишкек', callback_data='bishkek')
kara_balta = InlineKeyboardButton(text='Кара-Балта', callback_data='kara-balta')
sokuluk = InlineKeyboardButton(text='Сокулук', callback_data='sokuluk')
kant = InlineKeyboardButton(text='Кант', callback_data='kant')
cityes = InlineKeyboardMarkup(row_width=2).add(bishkek, kara_balta, sokuluk, kant)
