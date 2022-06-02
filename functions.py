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
        bot.send_message(message.chat.id, 'Укажите Ваш вес!')
    except:
        bot.send_message(message.chat.id, 'Укажите правильный рост!')


def say_result(state, bot, message):
    try:
        state['weight'] = float(message.text.lower())
        state['label'] = 'end'
        state['result'] = state['weight'] - (state['height'] - 100)
        bot.send_message(message.chat.id, f'Тебе нужно сбросить {state["result"]} кг!')
    except:
        bot.send_message(message.chat.id, 'Укажите правильный вес кг!')