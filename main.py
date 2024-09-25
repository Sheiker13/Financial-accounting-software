from models.user import User
from models.account import Account
from models.transaction import Transaction

def main_menu():
    print("1. Регистрация")
    print("2. Вход")
    print("3. Выход")

def account_menu():
    print("1. Создать счет")
    print("2. Просмотреть баланс")
    print("3. Добавить транзакцию")
    print("4. Выйти")

def main():
    while True:
        main_menu()
        choice = input("Выберите опцию: ")
        if choice == '1':
            username = input("Введите имя пользователя: ")
            password = input("Введите пароль: ")
            email = input("Введите email: ")
            User.register(username, password, email)
        elif choice == '2':
            username = input("Введите имя пользователя: ")
            password = input("Введите пароль: ")
            if User.login(username, password):
                while True:
                    account_menu()
                    option = input("Выберите действие: ")
                    if option == '1':
                        name = input("Название счета: ")
                        currency = input("Валюта счета: ")
                        Account.create_account(username, name, currency)
                    elif option == '2':
                        balance = Account.get_balance(username)
                        print(f"Ваш общий баланс: {balance}")
                    elif option == '3':
                        account_name = input("Название счета: ")
                        amount = float(input("Введите сумму: "))
                        transaction_type = input("Тип транзакции (income/expense): ")
                        Transaction.add_transaction(username, account_name, amount, transaction_type)
                    elif option == '4':
                        break
        elif choice == '3':
            break

if __name__ == "__main__":
    main()
