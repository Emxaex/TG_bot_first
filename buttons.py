from telebot import types

def btn_valuta():

    key_button = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Вывод валюты')

    key_button.add(item1)
    return key_button