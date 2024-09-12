import hashlib
import uuid
from file_handler import read_json, write_json
from logger import log_operation

USERS_FILE = "data/users.json"


class User:
    def __init__(self, username, password, email):
        self.username = username
        self.password = self._hash_password(password)
        self.email = email

    def _hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def check_password(self, password):
        return self.password == self._hash_password(password)

    def serialize(self):
        return {'username': self.username, 'password': self.password, 'email': self.email}


def register(username, password, email):
    users = read_json(USERS_FILE)
    if username in users:
        raise ValueError("Пользователь уже существует")
    new_user = User(username, password, email)
    users[username] = new_user.serialize()
    write_json(USERS_FILE, users)
    log_operation("Регистрация", username, f"Пользователь {username} зарегистрировался.")
    return new_user


def login(username, password):
    users = read_json(USERS_FILE)
    if username not in users:
        raise ValueError("Пользователь не найден")
    user_data = users[username]
    user = User(username, user_data['password'], user_data['email'])
    if not user.check_password(password):
        raise ValueError("Неверный пароль")
    log_operation("Вход", username, f"Пользователь {username} вошел в систему.")
    return user
