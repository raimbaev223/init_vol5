from telebot.types import KeyboardButton, ReplyKeyboardMarkup, \
    InlineKeyboardMarkup, InlineKeyboardButton

weather = KeyboardButton('Узнать погоду')
news = KeyboardButton('Новости')
btns = ReplyKeyboardMarkup(resize_keyboard=True).add(weather, news)

next = ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton('Еще новости'))

bishkek = KeyboardButton(text='Бишкек')
kara_balta = KeyboardButton(text='Кара-Балта')
sokuluk = KeyboardButton(text='Сокулук')
kant = KeyboardButton(text='Кант')
cityes = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=2).add(bishkek, kara_balta,
                                                                                            sokuluk, kant)
