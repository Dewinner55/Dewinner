import telebot
import sqlite3
import time

# Создаем объект бота
bot = telebot.TeleBot('6067571268:AAGOX7w_8wANm4cdPsOWbs5tV0LQarn7JmI')

# Подключаемся к базе данных
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Создаем таблицу для хранения пользователей


def get_cursor():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(
        'CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, used BOOLEAN)')
    return cursor

# Ответ на команду /start


@bot.message_handler(commands=['start'])
def send_welcome(message):
    # Получаем cursor
    cursor = get_cursor()
    # Проверяем, была ли функция уже вызвана для этого пользователя
    user_id = message.chat.id
    cursor.execute('SELECT used FROM users WHERE id = ?', (user_id,))
    result = cursor.fetchone()
    if result and result[0]:
        bot.send_message(message.chat.id, 'Вы уже использовали эту команду')
        bot.register_next_step_handler(message, handle_text)
    else:
        photo = open('/home/lenova/Desktop/py26/фото/Кадр от IMG_8837.MOV.png',
                     'rb')  # Открываем изображение
        bot.send_photo(message.chat.id, photo)  # Отправляем изображение
        # Отправляем приветственное сообщение
        bot.send_message(message.chat.id, 'Привет, я телеграмм бот!')
        time.sleep(2)
        bot.send_message(message.chat.id, 'Мы рады, что вы заинтересовались нашими турами. Пожалуйста, ответьте на несколько вопросов, чтобы мы могли подобрать наилучший вариант отдыха для вас.\nКуда бы вы хотели поехать?')
        # Помечаем пользователя как использовавшего функцию
        cursor.execute(
            'INSERT OR REPLACE INTO users (id, used) VALUES (?, ?)', (user_id, True))
        cursor.connection.commit()
        bot.register_next_step_handler(message, handle_text)

    cursor.close()
# Ответ на команду /text(любоев сообщение)


@bot.message_handler(commands=['text'])
def handle_text(message):
    destination = message.text
    bot.send_message(
        message.chat.id, f"Отлично! Мы найдем для вас лучший вариант тура в {destination}.\nКакой у вас бюджет на поездку?")


# Запускаем бота
bot.polling()
