import telebot
from telebot import types

# Вставьте сюда токен вашего бота
bot_token = '5842673789:AAHvjs9z6jjUQdZUgvaLrhloQErzA-OilQk'

# Создаем объект бота
bot = telebot.TeleBot(bot_token)

# Обработчик команды /start


@bot.message_handler(commands=['start'])
def start_handler(message):
    # Создаем объект InlineKeyboardMarkup
    markup = types.InlineKeyboardMarkup(row_width=2)

    # Создаем 8 объектов InlineKeyboardButton с нужными названиями
    balance_button = types.InlineKeyboardButton(
        "Ваш баланс", callback_data='balance')
    tours_button = types.InlineKeyboardButton(
        "Поиск туров", callback_data='tours')
    tickets_button = types.InlineKeyboardButton(
        "Авиабилеты", callback_data='tickets')
    russia_button = types.InlineKeyboardButton(
        "Россия", callback_data='russia')
    request_button = types.InlineKeyboardButton(
        "Запрос на подбор тура", callback_data='request')
    hot_tours_button = types.InlineKeyboardButton(
        "Горящие туры", callback_data='hot_tours')
    hotels_button = types.InlineKeyboardButton("Отели", callback_data='hotels')
    contacts_button = types.InlineKeyboardButton(
        "Контакты", callback_data='contacts')

    # Добавляем все кнопки на экран
    markup.add(balance_button, tours_button, tickets_button, russia_button,
               request_button, hot_tours_button, hotels_button, contacts_button)

    # Отправляем приветственное сообщение с инлайн-кнопками
    bot.send_message(
        message.chat.id, "Добро пожаловать! Выберите нужный пункт меню:", reply_markup=markup)


# Обработчик нажатий на инлайн-кнопки
@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    if call.data == 'balance':
        bot.send_message(call.message.chat.id, "Ваш баланс: 1000")
    elif call.data == 'tours':
        bot.send_message(call.message.chat.id,
                         "Введите место, куда хотите поехать:")
    elif call.data == 'tickets':
        bot.send_message(call.message.chat.id,
                         "Введите даты вашего вылета и прилета:")
    elif call.data == 'russia':
        bot.send_message(call.message.chat.id,
                         "Выберите город в России, куда хотите поехать:")
    elif call.data == 'request':
        bot.send_message(
            call.message.chat.id, "Оставьте заявку на подбор тура и наш менеджер свяжется с вами в ближайшее время.")
    elif call.data == 'hot_tours':
        bot.send_message(call.message.chat.id, "Список горящих туров:")
    elif call.data == 'hotels':
        bot.send_message(call.message.chat.id,
                         "Введите город, в котором хотите забронировать отель:")
    elif call.data == 'contacts':
        bot.send_message(call.message.chat.id,
                         "Номер телефона для связи: 8-800-555-35-35")


# Запускаем бота
bot.polling()
