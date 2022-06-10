import telebot
from telebot import types
from menu import \
    select_option, \
    set_gender, \
    set_height, \
    set_weight, \
    set_age, \
    restart, \
    start_losing_weight, \
    back_options, \
    show_first_options
from controller import start_controller

bot = telebot.TeleBot('5332131635:AAEv9FtOmTZY8TiZmLJ2xqa3MsEdZwz94AA')

class State:
    label = 0
    result = 0
    body_mass_index = 0
    max_normal_weight = 0
    coefs = {'coef_gender': 0, 'coef_age': 0}
    gender = ''
    height = 0
    weight = 0.0
    age = 0
    indicators = []

state = State()


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    show_first_options(state, markup, types)
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

    if state.label == 'start':
        select_option(state, bot, types, message, markup)

    elif state.label == 'gender':
        set_gender(state, bot, keyboard_none, message)

    elif state.label == 'height':
        set_height(state, bot, message)

    elif state.label == 'weight':
        set_weight(keyboard_none, state, bot, message)

    elif state.label == 'age':
        set_age(types, markup, state, bot, message)

    elif state.label == 'end':
        restart(state, message, bot, types, markup)

    elif state.label == 'start_losing_weight':
        start_losing_weight(state, message, bot, types, markup)

    elif state.label == 'start_controller':
        start_controller(keyboard_none, state, message, bot)

    elif state.label == 'rules':
        back_options(state, message, bot, types, markup)


bot.polling(none_stop=True)