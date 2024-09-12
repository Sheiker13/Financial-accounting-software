import uuid
from file_handler import read_json, write_json
from logger import log_operation

ACCOUNTS_FILE = "data/user_accounts.json"


class Account:
    def __init__(self, name, currency, initial_balance=0):
        self.id = str(uuid.uuid4())
        self.name = name
        self.currency = currency
        self.balance = initial_balance

    def add_income(self, amount):
        self.balance += amount

    def add_expense(self, amount):
        if self.balance < amount:
            raise ValueError("Недостаточно средств")
        self.balance -= amount

    def get_balance(self):
        return self.balance

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'currency': self.currency,
            'balance': self.balance
        }


def create_account(user, name, currency, initial_balance=0):
    accounts = read_json(ACCOUNTS_FILE)
    account = Account(name, currency, initial_balance)
    if user.username not in accounts:
        accounts[user.username] = []

    accounts[user.username].append(account.to_dict())
    write_json(ACCOUNTS_FILE, accounts)
    log_operation("Создание счета", user.username, f"Создан счет {name} с балансом {initial_balance} {currency}.")
    return account


def delete_account(user, account_id):
    accounts = read_json(ACCOUNTS_FILE)
    if user.username not in accounts:
        raise ValueError("У пользователя нет счетов")

    accounts[user.username] = [acc for acc in accounts[user.username] if acc['id'] != account_id]
    write_json(ACCOUNTS_FILE, accounts)
    log_operation("Удаление счета", user.username, f"Удален счет с ID {account_id}.")
