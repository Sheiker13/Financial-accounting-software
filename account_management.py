import json
from utils.file_handler import save_data, load_data

class Account:
    def __init__(self, name, currency, balance=0):
        self.name = name
        self.currency = currency
        self.balance = balance

    @staticmethod
    def create_account(user, name, currency):
        accounts = load_data(f'data/accounts/{user}_accounts.json')
        if name in accounts:
            raise ValueError("Счет с таким названием уже существует.")
        account = Account(name, currency)
        accounts[name] = {
            'currency': currency,
            'balance': account.balance
        }
        save_data(f'data/accounts/{user}_accounts.json', accounts)
        print(f"Счет {name} успешно создан для {user}.")

    @staticmethod
    def get_balance(user):
        accounts = load_data(f'data/accounts/{user}_accounts.json')
        total_balance = sum([account['balance'] for account in accounts.values()])
        print(f"Общий баланс пользователя {user}: {total_balance}")
        return total_balance
