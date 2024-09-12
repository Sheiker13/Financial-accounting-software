import uuid
import datetime
from file_handler import read_json, write_json
from logger import log_operation
from account_management import create_account

TRANSACTIONS_FILE = "data/user_transactions.json"


class Transaction:
    def __init__(self, account_id, amount, transaction_type, category):
        self.id = str(uuid.uuid4())
        self.account_id = account_id
        self.amount = amount
        self.transaction_type = transaction_type
        self.category = category
        self.date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def to_dict(self):
        return {
            'id': self.id,
            'account_id': self.account_id,
            'amount': self.amount,
            'transaction_type': self.transaction_type,
            'category': self.category,
            'date': self.date
        }


def add_transaction(user, account_id, amount, transaction_type, category):
    transactions = read_json(TRANSACTIONS_FILE)
    transaction = Transaction(account_id, amount, transaction_type, category)

    if user.username not in transactions:
        transactions[user.username] = []

    transactions[user.username].append(transaction.to_dict())
    write_json(TRANSACTIONS_FILE, transactions)
    log_operation("Транзакция", user.username,
                  f"{transaction_type.capitalize()} на сумму {amount} в категории {category}.")
    return transaction


def get_transactions(user, account_id, start_date, end_date):
    transactions = read_json(TRANSACTIONS_FILE)
    if user.username not in transactions:
        return []

    result = []
    for trans in transactions[user.username]:
        trans_date = datetime.datetime.strptime(trans['date'], '%Y-%m-%d %H:%M:%S')
        if trans['account_id'] == account_id and start_date <= trans_date <= end_date:
            result.append(trans)
    return result
