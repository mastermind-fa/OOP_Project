from bank import Bank
from abc import ABC, abstractmethod
class Account(ABC):
    account_counter = 10000
    def __init__(self, name, email, account_type):
        self.name = name
        self.email = email
        self.account_type = account_type
        self.balance = 0
        self.account_number = Account.generate_account_number()
        self.transactions = []
        self.loan_quantity = 0
        self.loan_counter = 0
        self.loan_feature_enabled = True
        
    @staticmethod
    def generate_account_number():
        account_number = Account.account_counter
        Account.account_counter += 1
        return account_number
    
    def account_info(self):
        pass
    def deposit(self, amount):
        if(amount <= 0):
            raise ValueError("Invalid amount")
        self.balance += amount
        self.transactions.append(f"Deposited: ${amount:.2f}")
    
    def withdraw(self, amount):
        if(amount > Bank.total_balance()):
            raise ValueError("The bank is bankrupt")
        
        elif(amount <= 0):
            raise ValueError("Invalid amount")
        elif amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            self.transactions.append(f"Withdrawn: {amount:.2f}")
            
    def check_balance(self):
        return self.balance
    def get_transactions(self):
        return self.transactions
    def take_loan(self, amount):
        if self.loan_counter >= 2 or not self.loan_feature_enabled:
            return "Loan limit exceeded or loan feature disabled"
        self.loan_counter += 1
        self.loan_quantity += amount
        self.balance += amount
        self.transactions.append(f"Loan taken: ${amount:.2f}")
        return f"Loan taken: ${amount:.2f}"
    def transfer(self, amount, account):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            account.balance += amount
            self.transactions.append(f"Transferred: ${amount:.2f} to {account.account_number}")
            account.transactions.append(f"Received: ${amount:.2f} from {self.account_number}")
            
            
            
            
            
class Admin(Account):
    def __init__(self, name, email, account_type):
        super().__init__(name, email, account_type)
        
    def add_user(self, name, email, account_type):
        new_account = Account(name, email, account_type)
        Bank.create_account(self, name, email, account_type)
        
    def delete_user(self, account_number):
        Bank.delete_account(self, account_number)
        
    def show_all_accounts(self):
        Bank.show_all_accounts(self)
        
    def show_account(self, account_number):
        Bank.show_account(self, account_number)
        
    def total_balance(self):
        return Bank.total_balance(self)
    
    def total_loan(self):
        return Bank.total_loan(self)
    
    def total_transactions(self):
        return Bank.total_transactions(self)
    def loan_request(self, account, ok):
        if ok:
            account.loan_feature_enabled = True
        else:
            account.loan_feature_enabled = False
        
        
        
        
if __name__ == "__main__":
    bank = Bank()
    admin = Admin("Admin", "admin@example.com", "Admin")

    # Admin adds users
    admin.add_user(bank, "Alice", "alice@example.com", "Savings")
    admin.add_user(bank, "Bob", "bob@example.com", "Current")

    # Show all accounts
    admin.show_all_accounts(bank)

    # Show individual account details
    admin.show_account(bank, 10000)  # Example account number