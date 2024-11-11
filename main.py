
import requests

# URL вашего сервера
SERVER_URL = 'http://your-server-url.com'

# Хранение сообщений для пользователей и администратора
messages = {
    'admin': [],
    'user': {}
}

def send_message_to_admin(user_id, message):
    # Функция для отправки сообщения администратору
    payload = {
        'user_id': user_id,
        'message': message
    }
    response = requests.post(f'{SERVER_URL}/send-message', json=payload)

def get_messages_from_admin():
    # Функция для получения сообщений от администратора
    response = requests.get(f'{SERVER_URL}/get-messages')
    return response.json()

def respond_to_user(user_id, message):
    # Функция для отправки ответа пользователю
    print(f"Ответ админа пользователю {user_id}: {message}")
    # Здесь можно добавить логику отправки ответа пользователю

def handle_user_message(user_id, message):
    # Обработка сообщения от пользователя
    print(f"Получено сообщение от пользователя {user_id}: {message}")
    send_message_to_admin(user_id, message)

def check_admin_responses():
    # Проверка ответов от администратора
    admin_messages = get_messages_from_admin()
    for msg in admin_messages:
        user_id = msg['user_id']
        response = msg['response']
        respond_to_user(user_id, response)

# Пример использования
if __name__ == "__main__":
    # Обработка сообщений пользователей
    user_id = "user1"
    user_message = "Привет, у меня вопрос!"
    handle_user_message(user_id, user_message)

    # Проверка ответов от администратора
    check_admin_responses()
