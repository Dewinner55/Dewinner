import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler

# функция для обработки команд


def start(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="Hello, I'm a bot!")

# функция для обработки сообщений


def echo(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=update.message.text)


# создание объекта бота
updater = Updater(
    token='5842673789:AAHvjs9z6jjUQdZUgvaLrhloQErzA-OilQk', use_context=True)

# создание обработчиков команд и сообщений
start_handler = CommandHandler('start', start)
echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)

# добавление обработчиков в бота
updater.dispatcher.add_handler(start_handler)
updater.dispatcher.add_handler(echo_handler)

# запуск бота
updater.start_polling()
updater.idle()
