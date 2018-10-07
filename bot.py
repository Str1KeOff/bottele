import telebot
import users

r = 0

bot = telebot.TeleBot('182033786:AAE3oyMwV8YtKruwlCZghWaAbnQI2qq6_24')

@bot.message_handler(commands=['start', 'старт'])
def handle_start(message):
    global r
    if r == 0:
        bot.send_message(message.chat.id, 'Работа начата!')
        r = 1
    else:
        bot.send_message(message.chat.id, 'Я уже работаю!')

@bot.message_handler(commands=['stop', 'стоп'])
def handle_stop(message):
    global r
    if r == 1:
        bot.send_message(message.chat.id, 'Работа оконченна!')
        bot.send_message(message.chat.id, 'Спасибо за использование! ' + message.from_user.first_name)
        r = 0
    else:
        bot.send_message(message.chat.id, 'Работа еще не начата!')
    
@bot.message_handler(commands=['info', 'инфо'])
def handle_info(message):
    global r
    if r == 1:
        bot.send_message(message.chat.id, 'Актуальная версия бота - 0.0.1a \n' +
                         'Бота написал Str1Ke \n' +
                         'С участием Winner_oK')
    else:
        bot.send_message(message.chat.id, 'Работа еще не начата! \n' +
                         message.from_user.first_name +', пожалуйста напиши: \n' +
                         '/start \n' +
                         'Что бы начать работу со мной')

@bot.message_handler(commands=['stoprog'])
def end(message):
    bot.send_message(message.chat.id, 'Выполнение завершенно')
    sys.exit()

@bot.message_handler(commands=['myid'])
def status(message):
    if users.users['started'][str(message.from_user.id)] == 1:
        st = 'начата'
    else:
        st = 'не начата'

    if users.users['banstatus'][str(message.from_user.id)] == 1:
        st1 = 'забанен'
    else:
        st1 = 'не забенен'
    stat = users.users['status'][str(message.from_user.id)]
    idd = message.from_user.id
    bot.send_message(message.chat.id, 'Привет, ' + message.from_user.first_name + '! \n' +
                     'Твой статус: \n' +
                     'Твой ID - ' + str(idd) + '\n' +
                     'Работа бота относительно тебя - ' + str(st) + '\n' +
                     'Твой статус в системе - ' + str(stat) + '\n' +
                     'Твой бан статус - ' + str(st1))

@bot.message_handler(content_types=["text"])
def any_msg(message):
    if message.text == 'пример':
        keyboard = telebot.types.InlineKeyboardMarkup()
        callback_button1 = telebot.types.InlineKeyboardButton(text="2", callback_data="test")
        callback_button = telebot.types.InlineKeyboardButton(text="4", callback_data="tett")
        keyboard.add(callback_button, callback_button1)
        bot.send_message(message.chat.id, "2 + 2 = ", reply_markup=keyboard)
    elif message.text == '.старт':
        handle_start(message)
    elif message.text == '.стоп':
        handle_stop(message)

@bot.callback_query_handler(func=lambda call: True)
def but_klick(call):
    if call.data == 'tett':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Абсолюно верно!')
    else:
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Тебе стоит пересмотреть свои взгляды на жизнь!')

bot.polling(none_stop=True)
