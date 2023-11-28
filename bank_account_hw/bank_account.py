from hashlib import sha224
from datetime import datetime


class PasswordError(Exception):
    pass


class TransactionError(Exception):
    pass


class BankAccount:
    """ A Bank Account Class"""

    def __init__(self, account_number, password, balance=0):
        self._balance = balance
        self._password_encoded = sha224(password.encode())
        self.blocked = False
        self.account_number = account_number

    def __repr__(self):
        return f'BankAccount({self.account_number})'

    def credit(self, value):
        self._balance += value

    def debit(self, value):
        self._balance -= value

    def get_balance(self):
        return self._balance

    def transfer(self, account, value):
        account.credit(value)
        self.debit(value)

    def check_password(self, password):
        return self._password_encoded.digest() == sha224(password.encode()).digest()


class Bank:
    next_account_number = 10_000

    def __init__(self, bank_name):
        self.bank_name = bank_name
        self.accounts = {}
        self.transactions = []

    def __repr__(self):
        return f"Bank('{self.bank_name}')"

    def add_account(self, ac_password, amount=0):
        Bank.next_account_number += 1
        self.accounts[Bank.next_account_number] = BankAccount(Bank.next_account_number, ac_password, amount)
        return Bank.next_account_number

    def check_account_number(self, ac_number):
        return ac_number in self.accounts.keys()

    def transact(self, source_account, dest_account, amount, transaction_datetime=datetime.now()):
        if amount <= 0:
            raise TransactionError("Transaction must be for a positive amount")

        if source_account.get_balance() < amount:
            raise TransactionError("Insufficient funds in source account")

        source_account.transfer(dest_account, amount)
        self.transactions.append({
            "date": transaction_datetime,
            "source_acc": source_account.account_number,
            "destination_acc": dest_account.account_number,
            "amount": amount,
        })


if __name__ == "__main__":
    my_bank = Bank("Highgate Bank")
    account_1 = my_bank.add_account("qwerty", 1000)
    account_2 = my_bank.add_account("password", 2000)
    my_bank.transact(my_bank.accounts[account_1], my_bank.accounts[account_2], 500)
    print(my_bank.transactions)
