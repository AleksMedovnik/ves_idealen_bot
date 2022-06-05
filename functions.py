def int_r(num):
    num = int(num + (0.5 if num > 0 else -0.5))
    return num


def calculate_mass(state):
    state['body_mass_index'] = state['weight'] / state['height'] ** 2
    # state['result'] = state['weight'] - (state['height'] - state['koef']) * 1.1
    if state['result'] < 18.5:
        return 'Тебе нужно набрать!'
    elif state['result'] >= 18.5 and state['result'] <= 25:
        return 'У тебя нормальный вес!'
    elif state['result'] > 25:
        return 'Тебе нужно сбросить!'


def select_option(state, bot, types, message, markup):
    if message.text == 'Хочу узнать, сколько мне нужно сбросить!':
        markup.add(
            types.KeyboardButton('Мужской'),
            types.KeyboardButton('Женский'),
        )
        state['label'] = 'gender'
        bot.send_message(message.chat.id, 'Укажите Ваш пол!', reply_markup=markup)


def set_gender(state, bot, keyboard_none, message):
    new_message = 'Укажите Ваш рост в см!'
    if message.text.lower() == 'мужской':
        state['label'] = 'height'
        state['gender'] = 'man'
        state['koef'] = 100
        bot.send_message(message.chat.id, new_message, reply_markup=keyboard_none)
    elif message.text.lower() == 'женский':
        state['label'] = 'height'
        state['gender'] = 'wooman'
        state['koef'] = 110
        bot.send_message(message.chat.id, new_message, reply_markup=keyboard_none)
    else:
        bot.send_message(message.chat.id, 'Выбери подходящий ответ ниже!')


def set_height(state, bot, message):
    try:
        state['height'] = int(message.text.lower())
        state['label'] = 'weight'
        bot.send_message(message.chat.id, 'Укажите Ваш вес в кг!')
    except:
        bot.send_message(message.chat.id, 'Укажите правильный рост в сантиметрах!')


def set_weight(types, markup, state, bot, message):
    try:
        state['weight'] = int(message.text.lower())
        state['label'] = 'athlet'
        markup.add(
            types.KeyboardButton('Да'),
            types.KeyboardButton('Нет'),
        )
        bot.send_message(
            message.chat.id,
            'Имеете ли Вы большую мышечную массу?',
            reply_markup=markup
        )
    except:
        bot.send_message(message.chat.id, 'Укажите правильный вес в кг!')


def test_athlet(state, bot, keyboard_none, message):
    try:
        new_message = 'Укажите свой полный возраст!'
        if message.text.lower() == 'да':
            state['athlet'] = True
            state['label'] = 'age'
            bot.send_message(message.chat.id, new_message, reply_markup=keyboard_none)
        elif message.text.lower() == 'нет':
            state['athlet'] = False
            state['label'] = 'age'
            bot.send_message(message.chat.id, new_message, reply_markup=keyboard_none)
    except:
        bot.send_message(message.chat.id, 'Укажите правильный ответ!')


def set_age(state, bot, message):
    try:
        state['age'] = int(message.text)
        state['label'] = 'end'
        bot.send_message(
            message.chat.id,
            'Все понятно!'
        )
    except:
        bot.send_message(message.chat.id, 'Укажите правильный возраст!')


def say_result(state, bot, message):
    try:
        state['weight'] = float(message.text.lower())
        state['label'] = 'end'


        new_message = ('сбросить' if state['result'] > 0 else 'набрать')
        bot.send_message(
            message.chat.id,
            f'Тебе нужно {new_message} {abs(int_r(state["result"]))} кг!'
        )
    except:
        bot.send_message(message.chat.id, 'Укажите правильный вес кг!')