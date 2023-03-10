import telegram
from telegram.ext import Updater, CommandHandler

# Введите токен вашего бота
TOKEN = '5842673789:AAHvjs9z6jjUQdZUgvaLrhloQErzA-OilQk'

# Функция-обработчик команды /start


def start(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="Привет, я бот!")


# Создание объекта бота
bot = telegram.Bot(token=TOKEN)

# Создание объекта обновления
updater = Updater(TOKEN, use_context=True)

# Создание обработчика команды /start и добавление его в обновление
start_handler = CommandHandler('start', start)
updater.dispatcher.add_handler(start_handler)

# Запуск бота
updater.start_polling()
