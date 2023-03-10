import telebot
import requests
from telebot import types
import time

# Функция для получения контактной информации с сайта


def get_contacts():
    url = "https://travel55.ru/o-nas/2009-kontakty"
    response = requests.get(url)
    if response.status_code == 200:
        # Извлекаем контактную информацию из HTML-кода страницы
        # Здесь нужно использовать соответствующую библиотеку для парсинга HTML, например, BeautifulSoup
        # В данном примере я просто возвращаю HTML-код страницы
        return response.text
    else:
        return "Произошла ошибка при получении контактной информации"


# def handle_contacts_button(message):
#     bot.send_message(
#         message.chat.id, "Наши контакты: https://travel55.ru/o-nas/2009-kontakty", disable_web_page_preview=True)


bot = telebot.TeleBot("5842673789:AAHvjs9z6jjUQdZUgvaLrhloQErzA-OilQk")

# Функция для запроса контактных данных, включая имя пользователя


def request_contact_info(message):
    markup = telebot.types.ReplyKeyboardMarkup(
        resize_keyboard=True, one_time_keyboard=True)
    contact_button = telebot.types.KeyboardButton(
        text="Отправить контактные данные", request_contact=True)
    skip_button = telebot.types.KeyboardButton(text="Пропустить")
    markup.add(contact_button, skip_button)
    # time.sleep(2)
    bot.send_message(message.chat.id, "Спасибо, что вы заинтересовались нашими турами! Чтобы мы могли помочь вам выбрать наилучший вариант отдыха, пожалуйста, отправьте свои контактные данные - имя и номер телефона:", reply_markup=markup)

    # Ожидание нажатия кнопки "Пропустить"
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
            message.chat.id, "Мы рады, что вы заинтересовались нашими турами. Пожалуйста, ответьте на несколько вопросов, чтобы мы могли подобрать наилучший вариант отдыха для вас.\nКуда бы вы хотели поехать?")
        # time.sleep(2)
        bot.register_next_step_handler(message, get_destination)


def get_destination(message):
    # time.sleep(1)
    destination = message.text
    bot.send_message(
        message.chat.id, f"Отлично! Мы найдем для вас лучший вариант тура в {destination}.\nКакой у вас бюджет на поездку?")
    # time.sleep(2)
    bot.register_next_step_handler(message, request_contact_info)
и

# def get_budget(message):
#     budget = message.text
#     markup = telebot.types.ReplyKeyboardRemove(selective=False)
#     bot.send_message(message.chat.id, f"Отлично! Мы найдем для вас лучший вариант тура в соответствии с вашим бюджетом. Если у вас есть какие-либо дополнительные требования, пожалуйста, сообщите нам.", reply_markup=markup)
#     bot.send_message(message.chat.id, "Также мы предлагаем скидку в размере 5% на бронирование тура для всех новых клиентов. Если вы хотите воспользоваться этой скидкой, оставьте, пожалуйста, свой номер телефона или email, и наш менеджер свяжется с вами в ближайшее время.", reply_markup=markup)


def handle_skip_button(message):
    # time.sleep(1)
    if message.text == "Пропустить":
        bot.send_message(
            message.chat.id, "Вы пропустили этот шаг. Если у вас будут какие-либо дополнительные требования, пожалуйста, сообщите нам.")
        # time.sleep(2)
        bot.send_message(message.chat.id, "Также мы предлагаем скидку в размере 5% на бронирование тура для всех новых клиентов. Если вы хотите воспользоваться этой скидкой, оставьте, пожалуйста, свой номер телефона или email, и наш менеджер свяжется с вами в ближайшее время.", reply_markup=telebot.types.ReplyKeyboardRemove())

    else:
        # time.sleep(2)
        bot.send_message(
            message.chat.id, "Спасибо! Мы свяжемся с вами в ближайшее время и предложим вам наилучший вариант отдыха. Если у вас есть какие-либо вопросы, пожалуйста, не стесняйтесь и задайте их нашему менеджеру.", reply_markup=telebot.types.ReplyKeyboardRemove())

    markup = telebot.types.ReplyKeyboardMarkup(
        resize_keyboard=True, one_time_keyboard=True)
    tours_button = telebot.types.KeyboardButton(text="Поиск туров")
    sea_button = telebot.types.KeyboardButton(text="Рассчитать стоимость тура")
    contacts_button = telebot.types.KeyboardButton(text="Контакты")
    contacts_button1 = telebot.types.KeyboardButton(text="Оставить контакт")
    markup.add(tours_button, sea_button, contacts_button,
               contacts_button1)
    bot.send_message(
        message.chat.id, "Выберите тип тура, который вас интересует используя интерективное меню:", reply_markup=markup)
    markup1 = telebot.types.InlineKeyboardMarkup()
    url_button = telebot.types.InlineKeyboardButton(
        text="Написать менеджеру в группу VK", url="https://vk.com/app5898182_-64890783#u=1465684&amp;s=1785391&amp;force=1")
    markup1.add(url_button)
    bot.send_message(
        message.chat.id, "Вы также можете связаться с менеджером в группе VK", reply_markup=markup1)
    bot.register_next_step_handler(message, handle_tour_type)

# Создаем функцию для обработки кнопки "Контакты"


@bot.message_handler(func=lambda message: message.text == "Контакты")
def handle_tour_type(message):
    # time.sleep(1)
    tour_type = message.text
    if tour_type == "Поиск туров":
        bot.send_message(
            message.chat.id, "Куда вы мечтаете отправиться в следующем отпуске? Может быть, мы сможем подобрать для вас наилучший вариант отдыха.")
        # TODO: рассчитать стоимость городского тура и отправить сообщение клиенту
        bot.register_next_step_handler(message, Poisk_turov)

    elif tour_type == "Рассчитать стоимость тура":
        time.sleep(1)
        bot.send_message(
            message.chat.id, "Куда вы мечтаете отправиться в следующем отпуске? Может быть, мы сможем подобрать для вас наилучший вариант отдыха.")
        # TODO: рассчитать стоимость морского круиза и отправить сообщение клиенту
        bot.register_next_step_handler(message, Poisk_turov)

    elif tour_type == "Контакты":
        #  Если пользователь выбрал "Контакты", выводим сообщение с ссылкой на сайт
        markup = telebot.types.InlineKeyboardMarkup()
        url_button = telebot.types.InlineKeyboardButton(
            text="Перейти на страницу контактов", url="https://travel55.ru/o-nas/2009-kontakty")
        markup.add(url_button)
        # time.sleep(1)
        bot.send_message(
            message.chat.id, "Телефон: \n + 7 (3812) 211-091\n Адрес: г.Омск, ул.Орджоникидзе д. 12\nТакже можете посмотреть контакты на нашем сайте: ", reply_markup=markup)
        markup = telebot.types.InlineKeyboardMarkup()
        url_button = telebot.types.InlineKeyboardButton(
            text="Перейти на страницу в группу VK", url="https://vk.com/app5898182_-64890783#u=1465684&amp;s=1785391&amp;force=1")
        markup.add(url_button)
        # time.sleep(2)
        bot.send_message(
            message.chat.id, "Но мы советуем перейти в нашу группу VK там вы найдёте специальные бонусы или скидки при бронировании тура сейчас, либо написать менеджеру, чтобы предоставить вам дополнительную информацию о турах и помочь с выбором наилучшего варианта ", reply_markup=markup)
        bot.register_next_step_handler(message, handle_tour_type)

    elif tour_type == "Оставить контакт":
        markup = telebot.types.ReplyKeyboardMarkup(
            resize_keyboard=True, one_time_keyboard=True)
        contact_button = telebot.types.KeyboardButton(
            text="Отправить контактные данные", request_contact=True)
        markup.add(contact_button)
        # time.sleep(1)
        bot.send_message(message.chat.id, "Спасибо, что вы заинтересовались нашими турами! Чтобы мы могли помочь вам выбрать наилучший вариант отдыха, пожалуйста, отправьте свои контактные данные - имя и номер телефона:", reply_markup=markup)
        # time.sleep(2)
        bot.send_message(
            message.chat.id, "Спасибо! Мы свяжемся с вами в ближайшее время и предложим вам наилучший вариант отдыха. Если у вас есть какие-либо вопросы, пожалуйста, не стесняйтесь, вы можете задайть их менеджеру напрямую, для этого надо подписаться на нас в группе VK, также в группе проходят акции, мы предлагаем скидку в размере 5% на бронирование тура для всех новых клиентов.")
        bot.register_next_step_handler(message, handle_tour_type)

    else:
        # time.sleep(2)
        markup = telebot.types.ReplyKeyboardMarkup(
            resize_keyboard=True, one_time_keyboard=True)
        tours_button = telebot.types.KeyboardButton(text="Поиск туров")
        sea_button = telebot.types.KeyboardButton(
            text="Рассчитать стоимость тура")
        contacts_button = telebot.types.KeyboardButton(text="Контакты")
        contacts_button1 = telebot.types.KeyboardButton(
            text="Оставить контакт")
        markup.add(tours_button, sea_button, contacts_button,
                   contacts_button1)
        bot.send_message(
            message.chat.id, "Выберите тип тура, который вас интересует используя интерективное меню:", reply_markup=markup)
        markup1 = telebot.types.InlineKeyboardMarkup()
        url_button = telebot.types.InlineKeyboardButton(
            text="Написать менеджеру в группу VK", url="https://vk.com/app5898182_-64890783#u=1465684&amp;s=1785391&amp;force=1")
        markup1.add(url_button)
        bot.send_message(
            message.chat.id, "Вы также можете связаться с менеджером в группе VK", reply_markup=markup1)
        bot.register_next_step_handler(message, handle_tour_type)

# Функция для обработки нажатия на кнопку "Контакты"


def Poisk_turov(message):
    # time.sleep(1)
    bot.send_message(
        message.chat.id, "Сколько времени у вас есть на отпуск и в какие даты вы планируете отпуск?")
    bot.register_next_step_handler(message, Poisk_turov2)


def Poisk_turov2(message):
    # time.sleep(2)
    bot.send_message(
        message.chat.id, "Сколько человек будет ехать вместе с вами? Может быть, мы сможем предложить вам выгодные условия для больших групп.")
    bot.register_next_step_handler(message, Poisk_turov3)


def Poisk_turov3(message):
    # time.sleep(2)
    bot.send_message(
        message.chat.id, "Какой бюджет вы планируете на отдых? Мы можем подобрать для вас оптимальный вариант тура, учитывая ваши финансовые возможности.")
    bot.register_next_step_handler(message, Poisk_turov4)


def Poisk_turov4(message):
    # time.sleep(2)
    bot.send_message(
        message.chat.id, "Отлично! Мы найдем для вас лучший вариант тура в соответствии с вашим бюджетом.")
    markup = telebot.types.InlineKeyboardMarkup()
    url_button = telebot.types.InlineKeyboardButton(
        text="Написать менеджеру в группу VK", url="https://vk.com/app5898182_-64890783#u=1465684&amp;s=1785391&amp;force=1")
    markup.add(url_button)
    # time.sleep(3)
    bot.send_message(
        message.chat.id, "Спасибо! Мы свяжемся с вами в ближайшее время и предложим вам наилучший вариант отдыха. Если у вас есть какие-либо вопросы, пожалуйста, не стесняйтесь, вы можете задайть их менеджеру напрямую, для этого надо подписаться на нас в группу VK, также в группе проходят акции, мы предлагаем скидку в размере 5% на бронирование тура для всех новых клиентов.", reply_markup=markup)
    # time.sleep(7)

    markup1 = telebot.types.ReplyKeyboardMarkup(
        resize_keyboard=True, one_time_keyboard=True)
    tours_button = telebot.types.KeyboardButton(text="Поиск туров")
    sea_button = telebot.types.KeyboardButton(
        text="Рассчитать стоимость тура")
    contacts_button = telebot.types.KeyboardButton(text="Контакты")
    contacts_button1 = telebot.types.KeyboardButton(
        text="Оставить контакт")
    markup1.add(tours_button, sea_button, contacts_button,
                contacts_button1)
    bot.send_message(
        message.chat.id, "Вы также можете использовать интерективное меню. \nЕсли у вас есть какие-либо дополнительные требования, пожалуйста, сообщите нам.", reply_markup=markup1)

    bot.register_next_step_handler(message, handle_tour_type)

# @bot.message_handler(func=lambda message: message.text == "Контакты")
# def handle_contacts(message):
#     # Получаем контактную информацию с сайта
#     contacts = get_contacts()
#     # Отправляем контактную информацию пользователю
#     bot.send_message(message.chat.id, contacts, parse_mode="HTML")


bot.polling()
