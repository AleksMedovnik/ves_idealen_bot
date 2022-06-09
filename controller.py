def start_controller(keyboard_none, state, message, bot):
    try:
        if message.text == 'Начать!':
            state.label = 'controller'
            bot.send_message(
                message.chat.id,
                'Введите показания весов в кг. Например, 72.4. Дробную часть пишите через точку!',
                reply_markup=keyboard_none
            )
    except:
        bot.send_message(message.chat.id, 'Выберите подходящий вариант!')


# def controller(message, state, bot):
#     try:
#         state.label = 'controller'
#         bot.send_message(
#             message.chat.id,
#             'Введите показания весов в кг. Например, 72.4. Дробную часть пишите через точку!'
#         )
#     except:
#         bot.send_message(message.chat.id, 'Выберите подходящий вариант!')