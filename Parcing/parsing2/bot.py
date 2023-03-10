import telebot
from telebot import types

# Введите токен вашего бота
TOKEN = '5842673789:AAHvjs9z6jjUQdZUgvaLrhloQErzA-OilQk'

# Функция-обработчик команды /start
# Создание объекта бота
bot = telebot.TeleBot(token=TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    print("Запуск")
    bot.send_message(
        message.chat.id, text="Привет, я бот!")
    print("Ответ получен")


# Создание объекта обновления
# updater = Updater(TOKEN, use_context=True)

# Создание обработчика команды /start и добавление его в обновление
# start_handler = CommandHandler('start', start)
# updater.dispatcher.add_handler(start_handler)

# Запуск бота
# updater.start_polling()
bot.polling()
