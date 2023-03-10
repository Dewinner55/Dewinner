import telebot
from telebot import types

bot = telebot.TeleBot("5842673789:AAHvjs9z6jjUQdZUgvaLrhloQErzA-OilQk")

# Функция для запроса контактных данных, включая имя пользователя


def request_contact_info(message):
    markup = types.ReplyKeyboardMarkup(
        resize_keyboard=True, one_time_keyboard=True)
    contact_button = types.KeyboardButton(
        text="Отправить контактные данные", request_contact=True)
    skip_button = types.KeyboardButton(text="Пропустить")
    markup.add(contact_button, skip_button)
    bot.send_message(message.chat.id, "Спасибо, что вы заинтересовались нашими турами! Чтобы мы могли помочь вам выбрать наилучший вариант отдыха, пожалуйста, отправьте свои контактные данные - имя и номер телефона:", reply_markup=markup)
    bot.register_next_step_handler(message, handle_skip_button)

# Функция для обработки текстовых сообщений


@bot.message_handler(content_types=["text"])
def handle_text(message):
    text = message.text.lower()
    if "телефон" in text or "email" in text or "@" in text or "номер" in text:
        # Если в сообщении есть упоминание о контактных данных, предлагаем клиенту оставить свои данные
        request_contact_info(message)
    else:
        # Если в сообщении нет контактных данных, задаем вопросы, чтобы выявить потребности клиента
        bot.send_message(
            message.chat.id, "Мы рады, что вы заинтересовались нашими турами. Пожалуйста, ответьте на несколько вопросов, чтобы мы могли подобрать наилучший вариант отдыха для вас.")
        bot.send_message(message.chat.id, "Куда бы вы хотели поехать?")
        bot.register_next_step_handler(message, get_destination)

# Функция для получения названия страны


def get_destination(message):
    destination = message.text
    bot.send_message(
        message.chat.id, f"Отлично! Мы найдем для вас лучший вариант тура в {destination}.")
    bot.send_message(message.chat.id, "Какой у вас бюджет на поездку?")
    bot.register_next_step_handler(message, get_budget)

# Функция для получения бюджета клиента


def get_budget(message):
    budget = message.text
    markup = types.ReplyKeyboardMarkup(
        resize_keyboard=True, one_time_keyboard=True)
    search_tours_button = types.KeyboardButton(text="Поиск туров")
    calculate_cost_button = types.KeyboardButton(
        text="Рассчитать стоимость тура")
    contacts_button = types.KeyboardButton(text="Контакты")
    markup.add(search_tours_button, calculate_cost_button, contacts_button)
    bot.send_message(message.chat.id, f"Отлично! Мы найдем для вас лучший вариант тура в соответствии с вашим бюджетом. Если у вас есть какие-либо дополнительные требования, пожалуйста, сообщите нам.", reply_markup=markup)
    bot.send_message(message.chat.id, "Также мы предлагаем скидку в размере 5% на бронирование тура для всех новых клиентов. Если вы хотите воспользоваться этой скидкой, оставьте, пожалуйста, свой номер телефона или email, и наш менеджер свяжется с вами в ближайшее время.", reply_markup=markup)
    bot.register_next_step_handler(message, handle_callback_query)


@bot.callback_query_handler(func=lambda message: True)
def handle_callback_query(message):
    tour_type = message.text

    if tour_type == "Поиск туров":
        # Если пользователь выбрал "Поиск туров", выводим сообщение с инструкцией
        bot.send_message(
            message.chat.id, "Чтобы найти тур, пожалуйста, введите город или страну, куда вы хотели бы отправиться.")
        bot.register_next_step_handler(message, get_tour_search_query)

    elif tour_type == "Рассчитать стоимость тура":
        # Если пользователь выбрал "Рассчитать стоимость тура", выводим сообщение с инструкцией
        bot.send_message(message.chat.id, "Чтобы рассчитать стоимость тура, пожалуйста, введите следующую информацию: город или страну, куда вы хотели бы отправиться; даты начала и конца поездки; количество взрослых и детей.")
        bot.register_next_step_handler(message, get_tour_price_query)

    elif tour_type == "Контакты":
        # Если пользователь выбрал "Контакты", выводим сообщение с ссылкой на сайт
        markup = telebot.types.InlineKeyboardMarkup()
        url_button = telebot.types.InlineKeyboardButton(
            text="Перейти на страницу контактов", url="https://travel55.ru/o-nas/2009-kontakty")
        markup.add(url_button)
        bot.send_message(
            message.chat.id, "Вы можете найти наши контакты на нашем сайте:", reply_markup=markup)


def get_tour_search_query(message):
    search_query = message.text
    # TODO: Обработка запроса на поиск тура
    pass


def get_tour_price_query(message):
    tour_info = message.text
    # TODO: Рассчет стоимости тура
    pass


bot.polling()
