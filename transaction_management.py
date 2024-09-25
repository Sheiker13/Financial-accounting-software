from datetime import datetime
from utils.file_handler import load_data, save_data


class Transaction:
    def __init__(self, account, amount, transaction_type):
        self.account = account
        self.amount = amount
        self.transaction_type = transaction_type
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    @staticmethod
    def add_transaction(user, account_name, amount, transaction_type):
        accounts = load_data(f'data/accounts/{user}_accounts.json')
        if account_name not in accounts:
            raise ValueError("Счет не найден.")
        if transaction_type == "expense" and accounts[account_name]['balance'] < amount:
            raise ValueError("Недостаточно средств.")

        accounts[account_name]['balance'] += amount if transaction_type == "income" else -amount
        transactions = load_data(f'data/transactions/{user}_transactions.json')

        transaction = Transaction(account_name, amount, transaction_type)
        transactions.append({
            'account': account_name,
            'amount': amount,
            'type': transaction_type,
            'date': transaction.date
        })

        save_data(f'data/accounts/{user}_accounts.json', accounts)
        save_data(f'data/transactions/{user}_transactions.json', transactions)
        return transaction
