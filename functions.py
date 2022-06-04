def build_menu(buttons, n_cols,
               header_buttons=None,
               footer_buttons=None):
    menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
    if header_buttons:
        menu.insert(0, [header_buttons])
    if footer_buttons:
        menu.append([footer_buttons])
    return menu


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


def set_weight(types, state, bot, message):
    try:
        state['weight'] = int(message.text.lower())
        state['label'] = 'test-athlet'
        button_list = [
            types.InlineKeyboardButton(text='Да', callback_data='1'),
            types.InlineKeyboardButton(text='Нет', callback_data='0'),
        ]
        markup = types.InlineKeyboardMarkup(build_menu(button_list, n_cols=2))
        bot.send_message(
            message.chat.id,
            'Имеете ли Вы большую мышечную массу?',
            reply_markup=markup
        )
    except:
        bot.send_message(message.chat.id, 'Укажите правильный вес в кг!')

def test_athlet(state, bot, message):
    try:
        state['athlet'] = int(message.text)
        state['label'] = 'weight'
        bot.send_message(message.chat.id, 'Укажите Ваш вес в кг!')
    except:
        bot.send_message(message.chat.id, 'Укажите правильный рост в метрах (например, 1.72)!')


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