import telebot
import webbrowser
from telebot import types


bot = telebot.TeleBot("7187132387:AAEwgH35MjH8O0J0PTD1RkdSHrYsV0490ck")
image_one = open('./one.jpg', 'rb')
image_two = open('./two.jpg', 'rb')

@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Записаться на прием')
    btn2 = types.KeyboardButton('Контактный телефон')
    btn3 = types.KeyboardButton('Где принимаю?')
    btn4 = types.KeyboardButton('Узнать цены на прием')
    markup.row(btn1, btn2)
    markup.row(btn4, btn3)
    bot.send_message(message.chat.id,
                     f'Привет {message.from_user.first_name},  я помощник Артема!\nНажми на кнопку которая тебя интересует:', reply_markup=markup)
    bot.register_next_step_handler(message, on_click)

def on_click(message):
    if message.text == "Записаться на прием":
        bot.send_message(message.chat.id, 'https://dikidi.ru/1017456?p=0.pi')
    elif message.text == "Узнать цены на прием":
        bot.send_message(message.chat.id,"Мануальный прием: 4000 рублей\nКонсультация: 1000 рублей\nФормовка стелек под ключ: 10000 рублей\nПодбор цветов Баха: 3000 рублей")
    elif message.text == "Где принимаю?":
        bot.send_message(message.chat.id,"метро Братиславская, улица братиславская дом 8")
        bot.send_photo(message.chat.id, image_one)
        bot.send_photo(message.chat.id, image_two)

    elif message.text == "Контактный телефон":
        bot.send_message(message.chat.id,"+79772807771")


@bot.message_handler()
def info(message):
    if message.text.lower() == "записаться на прием":
        bot.send_message(message.chat.id, 'https://dikidi.ru/1017456?p=0.pi')
    elif message.text.lower() == "узнать цены на прием":
        bot.send_message(message.chat.id,"Мануальный прием: 4000 рублей\nКонсультация: 1000 рублей\nФормовка стелек под ключ: 10000 рублей\nПодбор цветов Баха: 3000 рублей")
    elif message.text.lower() == "где принимаю?":
        bot.send_message(message.chat.id,"метро Братиславская, улица братиславская дом 8")
        bot.send_photo(message.chat.id, image_one)
        bot.send_photo(message.chat.id, image_two)
    elif message.text.lower() == "контактный телефон":
        bot.send_message(message.chat.id,"+79772807771")


bot.polling(none_stop=True)