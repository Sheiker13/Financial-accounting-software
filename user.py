import hashlib
from utils.file_handler import save_data, load_data

class User:
    def __init__(self, username, password, email):
        self.username = username
        self.password = hashlib.sha256(password.encode()).hexdigest()  # Хеширование пароля
        self.email = email

    @staticmethod
    def register(username, password, email):
        users = load_data('data/users.json')
        if username in users:
            raise ValueError("Пользователь уже существует.")
        user = User(username, password, email)
        users[username] = {
            'password': user.password,
            'email': email
        }
        save_data('data/users.json', users)
        return user

    @staticmethod
    def login(username, password):
        users = load_data('data/users.json')
        if username not in users or users[username]['password'] != hashlib.sha256(password.encode()).hexdigest():
            raise ValueError("Неверный логин или пароль.")
        return True
