import requests
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Токен вашего бота
TOKEN = 'your_bot_token'
# URL вашего сервера
SERVER_URL = 'https://api.telegram.org'

updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

def send_message_to_admin(user_id, message):
    # Функция для отправки сообщения администратору
    payload = {
        "user_id": user_id,
        "message": message
    }
    response = requests.post(f"{SERVER_URL}/send-message", json=payload)
    if response.status_code == 200:
        print("Сообщение успешно отправлено администратору")
    else:
        print("Ошибка при отправке сообщения администратору")

def user_message_handler(update, context):
    user_id = update.effective_user.id
    user_message = update.message.text
    handle_user_message(user_id, user_message)

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Привет, я бот! Отправь мне свой вопрос.")

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

user_message_handler = MessageHandler(Filters.text & ~Filters.command, user_message_handler)
dispatcher.add_handler(user_message_handler)

updater.start_polling()
updater.idle()
