import telegram
from telegram.ext import Updater, CommandHandler

# Введите токен вашего бота
TOKEN = 'YOUR_TOKEN_HERE'

# Функция-обработчик команды /start


def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Привет, я бот!")


# Создание объекта бота
bot = telegram.Bot(token=TOKEN)

# Создание объекта обновления
updater = Updater(TOKEN)

# Создание обработчика команды /start и добавление его в обновление
start_handler = CommandHandler('start', start)
updater.dispatcher.add_handler(start_handler)

# Запуск бота
updater.start_polling()
