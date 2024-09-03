from authentication import register, login
from account_management import create_account, delete_account
from transaction_management import add_transaction, get_transactions
import datetime

def main():
    user = None

    while True:
        print("1. Регистрация")
        print("2. Вход")
        print("3. Добавить счет")
        print("4. Добавить транзакцию")
        print("5. Сгенерировать отчет")
        print("0. Выйти")

        choice = input("Выберите опцию: ")

        if choice == "1":
            username = input("Введите имя пользователя: ")
            password = input("Введите пароль: ")
            email = input("Введите email: ")
            try:
                user = register(username, password, email)
                print(f"Пользователь {username} успешно зарегистрирован.")
            except ValueError as e:
                print(e)
        elif choice == "2":
            username = input("Введите имя пользователя: ")
            password = input("Введите пароль: ")
            try:
                user = login(username, password)
                print(f"Пользователь {username} успешно вошел в систему.")
            except ValueError as e:
                print(e)
        elif choice == "3" and user:
            name = input("Название счета: ")
            currency = input("Валюта счета: ")
            initial_balance = float(input("Начальный баланс: "))
            account = create_account(user, name, currency, initial_balance)
            print(f"Счет {account.name} создан с балансом {account.balance} {account.currency}.")
        elif choice == "4" and user:
            account_id = input("ID счета: ")
            amount = float(input("Сумма: "))
            transaction_type = input("Тип транзакции (доход/расход): ")
            category = input("Категория: ")
            transaction = add_transaction(user, account_id, amount, transaction_type, category)
            print(f"Транзакция {transaction.id} добавлена.")
        elif choice == "5" and user:
            account_id = input("ID счета: ")
            start_date = input("Введите начальную дату (YYYY-MM-DD): ")
            end_date = input("Введите конечную дату (YYYY-MM-DD): ")
            start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d')
            end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d')
            transactions = get_transactions(user, account_id, start_date, end_date)
            for trans in transactions:
                print(trans)
        elif choice == "0":
            break
        else:
            print("Неверный ввод или необходимо войти в систему.")

if __name__ == "__main__":
    main()
