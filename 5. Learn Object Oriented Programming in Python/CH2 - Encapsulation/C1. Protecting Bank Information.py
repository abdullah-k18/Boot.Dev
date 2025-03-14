class BankAccount:
    def __init__(self, account_number, initial_balance):
        self.__account_number = account_number
        self.__initial_balance = initial_balance

    def get_account_number(self):
        return self.__account_number

    def get_balance(self):
        return self.__initial_balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError ("cannot deposit zero or negative funds")
        else:
            self.__initial_balance = amount + self.__initial_balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError ("cannot withdraw zero or negative funds")
        elif self.__initial_balance < amount:
            raise ValueError ("insufficient funds")
        else:
            self.__initial_balance -= amount
