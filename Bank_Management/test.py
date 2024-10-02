

class Account():
    account_counter = 10000

    def __init__(self, name, email, address, account_type):
        self.name = name
        self.email = email
        self.address = address
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

    

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Invalid amount")
        self.balance += amount
        self.transactions.append(f"Deposited: ${amount:.2f}")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Invalid amount")
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            self.transactions.append(f"Withdrawn: ${amount:.2f}")

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
    def __init__(self, name, email, address, account_type):
        super().__init__(name, email,address, account_type)
        
    def add_user(self, bank, name, email,address, account_type):
        new_account = Account(name, email, address, account_type)  
        bank.create_account(new_account)
        
    def delete_user(self, bank, account_number):
        bank.delete_account(account_number)
        
    def show_all_accounts(self, bank):
        return bank.show_all_accounts()
        
    def show_account(self, bank, account_number):
        return bank.show_account(account_number)
        
    def total_balance(self, bank):
        return bank.total_balance()
    
    def total_loan(self, bank):
        return bank.total_loan()
    
    def total_transactions(self, bank):
        return bank.total_transactions()
    
    def loan_request(self, account, ok):
        account.loan_feature_enabled = ok
        
class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account):
        self.accounts[account.account_number] = account
        
    def delete_account(self, account_number):
        if account_number in self.accounts:
            del self.accounts[account_number]
            print("Account deleted successfully.")
        else:
            print("Account does not exist")
            
    def show_all_accounts(self):
        for account_number, account in self.accounts.items():
            print(f"{account_number} - {account.account_type}")

    def show_account(self, account_number):
        if account_number in self.accounts:
            account = self.accounts[account_number]
            print(f"Account number: {account.account_number}")
            print(f"Name: {account.name}")
            print(f"Email: {account.email}")
            print(f"Account type: {account.account_type}")
            print(f"Balance: ${account.balance:.2f}")
            print("Transactions:", account.get_transactions())
            print(f"Loan quantity: ${account.loan_quantity:.2f}")
        else:
            print("Account does not exist")
            
    def total_balance(self):
        return sum(account.balance for account in self.accounts.values())
    
    def total_loan(self):
        return sum(account.loan_quantity for account in self.accounts.values())
    
    def total_transactions(self):
        return sum(len(account.transactions) for account in self.accounts.values())
    


