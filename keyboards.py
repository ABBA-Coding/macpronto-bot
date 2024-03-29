from telebot.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, WebAppInfo


def webbutton():
    markup = ReplyKeyboardMarkup(resize_keyboard=True,row_width=2)
    longcut = WebAppInfo('https://www.macpronto.com/category/2')
    shortcut = WebAppInfo('https://www.macpronto.com/category/3')
    markup.add(KeyboardButton("Long cut pasta", web_app=longcut), KeyboardButton("Short cut pasta", web_app=shortcut),
               KeyboardButton("Our contacts"))

    return markup


def send_contact():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(KeyboardButton("Send contact", request_contact=True))

    return markup
