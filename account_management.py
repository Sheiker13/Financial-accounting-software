from utils.file_handler import load_data, save_data

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
            'currency': account.currency,
            'balance': account.balance
        }
        save_data(f'data/accounts/{user}_accounts.json', accounts)
        return account

    @staticmethod
    def get_balance(user):
        accounts = load_data(f'data/accounts/{user}_accounts.json')
        total_balance = sum([acc['balance'] for acc in accounts.values()])
        return total_balance
