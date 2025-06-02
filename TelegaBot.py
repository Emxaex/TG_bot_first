import telebot
#помогает переходить по ссылкам на сайт
import webbrowser
import buttons
import STbot3


bot=telebot.TeleBot('')
@bot.message_handler(commands=['start'])
def start(message):
    #from_user для личных сообщений
    bot.send_message(message.from_user.id, f'<b>Привет {message.from_user.first_name}</b>, <em>как у тебя дела?</em>',parse_mode='html', reply_markup=buttons.btn_valuta())
    #отправляет информацию о сессии
    #bot.send_message(message.from_user.id, message)
    #chat для группы
    #bot.send_message(message.chat.id,'Привет')

@bot.message_handler(commands=['site'])
def site(message):
    #команда для перехода на сайт
    webbrowser.open('https://nbu.uz/ru/fizicheskim-litsam-kursy-valyut')

@bot.message_handler(func=lambda message: True)
def handle_button_press(message):
    if message.text == 'Вывод валюты':
        info_value = STbot3.func_valuta()
        bot.reply_to(message,  info_value)
    else:
        bot.reply_to(message, 'окак')

@bot.message_handler()
def random_text(message):
    bot.reply_to(message, f'Не понимаю ваш запрос')
bot.polling(non_stop=True)
