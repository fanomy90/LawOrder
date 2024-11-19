from telebot import types, TeleBot
import os
from dotenv import load_dotenv
from pathlib import Path
#import requests
import datetime

# Загрузка переменных окружения из файла .env
load_dotenv()
TOKEN = os.getenv("TOKEN")
bot = TeleBot(TOKEN)
now = datetime.datetime.now()
#Основное меню
@bot.message_handler(content_types=["text"])
def next_message(message):
    print(f"{now} Получено сообщение: {message.text}")  # Логирование входящих сообщений
    from news.models import TelegramSubscriber
    if message.text.lower() == message.text.lower() == '/law_order':
        keyboard_subcategory = types.InlineKeyboardMarkup(row_width=1)
        button1 = types.InlineKeyboardButton('Найти информацию по ИНН', callback_data='key1')
        button2 = types.InlineKeyboardButton('Архив запросов по ИНН', callback_data='key2')
        keyboard_subcategory.add(button1, button2)
        chat_id = message.chat.id
        username = message.from_user.username
        subscriber, created = TelegramSubscriber.objects.get_or_create(
            chat_id=chat_id,
            defaults={'username': username}
        )
        if created:
            bot.send_message(chat_id, 
            text=f"Добро пожаловать, {username}!\nВыберите действие:")
        else:
            bot.send_message(chat_id, 
            text=f"Добро день, {username}!\nВыберите действие:")
    else:
        bot.send_message(message.chat.id, f"Недоступная операция: {message.text}")
        print(f"Недоступная операция: {message.text}")

#запуск бота через supervisord
def run_bot():
    print(f"{now} Запуск Telegram-бота...")
    try:
        # Запуск polling с настройкой тайм-аутов
        bot.polling(none_stop=True, timeout=60, long_polling_timeout=60)
    except Exception as e:
        print(f"{now} Ошибка: {e}")
if __name__ == "__main__":
    run_bot()