import telebot
from telebot import types
from functions import *

bot = telebot.TeleBot('5332131635:AAEv9FtOmTZY8TiZmLJ2xqa3MsEdZwz94AA')

state = {
    'label': '',
    'result': 0,
    'gender': '',
    'koef': 0,
    'height': 0,
    'weight': 0.0,
    'athlet': False,
    'body_mass_index': 0,
}

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Хочу похудеть!')
    item2 = types.KeyboardButton('Хочу узнать, сколько мне нужно сбросить!')

    markup.add(item1, item2)
    state['label'] = 'start'
    bot.send_message(
        message.chat.id,
        f'''Привет, {message.from_user.first_name} {message.from_user.last_name}! 
Я - бот-консультант по похудению! 
Чтобы начать процесс похудения, кликни на кнопку “Хочу похудеть!”.
Если хочешь узнать, сколько тебе нужно сбросить, кликни на кнопку “Хочу узнать, сколько мне нужно сбросить!”
        ''',
        reply_markup=markup
    )


@bot.message_handler(content_types=['text'])
def bot_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard_none = types.ReplyKeyboardRemove()

    if state['label'] == 'start':
        select_option(state, bot, types, message, markup)

    elif state['label'] == 'gender':
        set_gender(state, bot, keyboard_none, message)

    elif state['label'] == 'height':
        set_height(state, bot, message)

    elif state['label'] == 'weight':
        set_weight(types, state, bot, message)


bot.polling(none_stop=True)