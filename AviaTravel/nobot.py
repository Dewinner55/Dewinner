import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import requests

# авторизация
headers = {
    'apikey': 'YOUR_API_KEY',
}

# функция для получения данных о дешевых авиабилетах


def get_cheapest_flights(origin, destination, outbound_date, inbound_date):
    # задаем параметры запроса
    params = {
        'country': 'US',
        'currency': 'USD',
        'locale': 'en-US',
        'originplace': origin,
        'destinationplace': destination,
        'outbounddate': outbound_date,
        'inbounddate': inbound_date,
        'adults': 1
    }

    # отправляем GET-запрос к API Skyscanner
    response = requests.get('https://partners.api.skyscanner.net/apiservices/browsedates/v1.0/US/USD/en-US/{}/{}'.format(
        origin, destination), params=params, headers=headers)

    # обрабатываем ответ от API
    if response.status_code == 200:
        data = response.json()
        cheapest_quotes = data['Dates']['OutboundDates'][:3]
        cheapest_quotes = [q['QuoteId'] for q in cheapest_quotes]
        return cheapest_quotes
    else:
        return None

# функция, которая будет вызываться при команде /start


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Привет! Я помогу тебе найти самый выгодный тур, билет или отель.")

# функция, которая будет вызываться при команде /help


def help(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Напиши /flight, чтобы получить информацию о самых дешевых авиабилетах на заданные даты между указанными городами.")

# функция, которая будет вызываться при команде /flight


def flight(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="Введите город отправления:")
    context.user_data['step'] = 1

# функция, которая будет вызываться при получении текстового сообщения от пользователя


def text(update, context):
    text = update.message.text
    chat_id = update.effective_chat.id
    step = context.user_data.get('step', 0)

# если пользователь ввел город отправления
    if step == 1:
        context.user_data['origin'] = text
        context.bot.send_message(chat_id=chat_id, text="Введите город назначения:")
        context.user_data['step'] = 2

# если пользователь ввел город назначения
    elif step == 2:
        context.user_data['destination'] = text
        context.bot.send_message(
            chat_id=chat_id, text="Введите дату отправления (в формате YYYY-MM-DD):")
        context.user_data['step'] = 3

    # если пользователь ввел дату отправления
    elif step == 3:
        context.user_data['outbound_date'] = text
        context.bot.send_message(
            chat_id=chat_id, text="Введите дату возвращения (в формате YYYY-MM-DD):")
        context.user_data['step'] = 4
        
    # если пользователь ввел дату возвращения
    elif step == 4:
        context.user_data['inbound_date'] = text
        origin = context.user_data['origin']
        destination = context.user_data['destination']
        outbound_date = context.user_data['outbound_date']
        inbound_date = context.user_data['inbound_date']
        cheapest_quotes = get_cheapest_flights(
            origin, destination, outbound_date, inbound_date)
        if cheapest_quotes is not None:
            context.bot.send_message(
                chat_id=chat_id, text="Самые дешевые авиабилеты:")
            for quote_id in cheapest_quotes:
                context.bot.send_message(
                    chat_id=chat_id, text="https://www.skyscanner.com/transport/flights/{}/{}/{}/".format(origin, destination, quote_id))
        else:
            context.bot.send_message(
                chat_id=chat_id, text="Произошла ошибка при поиске авиабилетов.")
        context.user_data.clear()
