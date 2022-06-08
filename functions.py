def int_r(num):
    num = int(num + (0.5 if num > 0 else -0.5))
    return num


def calculate_mass(state):
    coef_height = (state['height'] / 100) ** 2
    state['body_mass_index'] = state['weight'] / coef_height
    state['coefs']['coef_gender'] = (1 if state['gender'] == 'man' else 0)
    state['coefs']['coef_age'] = (0.5 if state['age'] > 60 else 0)
    coef_gender = state['coefs']['coef_gender']
    coef_age = state['coefs']['coef_age']
    state['max_normal_weight'] = 25 + coef_gender + coef_age

    if state['body_mass_index'] < 18.5:
        result = 18.5 * coef_height - state['weight']
        return f'Тебе нужно набрать {int_r(result)} кг!'
    elif (state['body_mass_index'] >= 18.5) and (state['body_mass_index'] <= state['max_normal_weight']):
        return 'У тебя нормальный вес!'
    elif state['body_mass_index'] > state['max_normal_weight']:
        result = state['weight'] - state['max_normal_weight'] * coef_height
        return f'Тебе нужно сбросить {int_r(result)} кг!'


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
        bot.send_message(message.chat.id, new_message, reply_markup=keyboard_none)
    elif message.text.lower() == 'женский':
        state['label'] = 'height'
        state['gender'] = 'wooman'
        bot.send_message(message.chat.id, new_message, reply_markup=keyboard_none)
    else:
        bot.send_message(message.chat.id, 'Выбери подходящий ответ ниже!')


def set_height(state, bot, message):
    try:
        state['height'] = int(message.text.lower())
        state['label'] = 'weight'
        bot.send_message(message.chat.id, 'Укажите Ваш вес в кг (округлённый)!')
    except:
        bot.send_message(message.chat.id, 'Укажите правильный рост в сантиметрах!')


def set_weight(keyboard_none, state, bot, message):
    try:
        state['weight'] = int(message.text.lower())
        state['label'] = 'age'
        bot.send_message(
            message.chat.id,
            'Укажите свой возраст!',
            reply_markup=keyboard_none
        )
    except:
        bot.send_message(message.chat.id, 'Укажите правильный вес в кг!')


def set_age(types, markup, state, bot, message):
    try:
        state['age'] = int(message.text)
        state['label'] = 'end'
        markup.add(
            types.KeyboardButton('В основное меню!'),
        )
        bot.send_message(
            message.chat.id,
            calculate_mass(state),
            reply_markup=markup
        )
    except:
        bot.send_message(message.chat.id, 'Укажите правильный возраст!')


def restart(state, message, bot, types, markup):
    try:
        if message.text.lower() == 'в основное меню!':
            state['label'] = 'start'
            markup.add(
                types.KeyboardButton('Хочу похудеть!'),
                types.KeyboardButton('Хочу узнать, сколько мне нужно сбросить!')
            )
            bot.send_message(
                message.chat.id,
                'Удачи!',
                reply_markup=markup
            )
    except:
        bot.send_message(message.chat.id, 'Нажмите на кнопку ниже!')