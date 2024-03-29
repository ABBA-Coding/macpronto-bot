from telebot import TeleBot
from telebot.types import Message

from keyboards import *
from config import *


bot = TeleBot(TOKEN)


user_info = {}

@bot.message_handler(commands=['start'])
def reaction_start(message:Message):
    chat_id = message.chat.id
    user_info[chat_id] = {}
    bot.send_message(chat_id,"Welcome to our Mac Pronto Bot!")
    bot.send_message(chat_id,'Please enter your name:')
    bot.register_next_step_handler(message,save_name)


def save_name(message):
    chat_id = message.chat.id
    user_info[chat_id]["name"] = message.text
    bot.send_message(chat_id, "Please send your number:", reply_markup=send_contact())
    bot.register_next_step_handler(message,save_phone)


def save_phone(message):
    chat_id = message.chat.id
    if chat_id in user_info:
         user_info[chat_id]['phone'] = message.contact.phone_number
         bot.send_message(CHANNEL_ID, f"Name: {user_info[chat_id]['name']}, Number: {user_info[chat_id]['phone']}")
    bot.send_message(chat_id,'Saved!', reply_markup=webbutton())


@bot.message_handler(func=lambda message: message.text == 'Our contacts')
def contacts(message: Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, '''<a href="https://www.facebook.com/people/macpronto/100083604484791/">Facebook</a> | <a href="https://www.youtube.com/channel/UCG76j-r42Ck91P3dD7LQk7A">Youtube</a> | <a href="https://www.linkedin.com/company/macpronto/">Linkedin</a> | <a href="https://www.instagram.com/macpronto/">Instagram</a>
''',parse_mode="HTML")



















if __name__ == '__main__':
    print('Bot ishladi...')
    bot.infinity_polling()
