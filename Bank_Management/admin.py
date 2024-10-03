from account import Account
from bank import Bank
class Admin:
    def __init__(self):
        self.admins = {}

    def is_admin(self, username, password):
        return username in self.admins and self.admins[username] == password

    def add_admin(self, username, password):
        self.admins[username] = password
        print(f"Admin account for {username} created successfully.")

    def add_user(self, bank, name, email, address, account_type):
        new_account = Account(name, email, address, account_type)
        bank.create_account(new_account)
        print(f"Account created: {new_account.account_number} - {new_account.account_type}")

    def delete_user(self, bank, account_number):
        bank.delete_account(account_number)

    def show_all_accounts(self, bank):
        bank.show_all_accounts()

    def show_account(self, bank, account_number):
        bank.show_account(account_number)

    def total_balance(self, bank):
        total = bank.total_balance()
        print(f"Total balance of all accounts: ${total:.2f}")

    def total_loan(self, bank):
        total = bank.total_loan()
        print(f"Total loan amount of all accounts: ${total:.2f}")

    @staticmethod
    def toggle_loan_feature(bank):
        bank.toggle_loan_feature()
