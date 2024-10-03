from bank import Bank
class Account:
    account_counter = 20000

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

    @staticmethod
    def generate_account_number():
        account_number = Account.account_counter
        Account.account_counter += 1
        return account_number

    def deposit(self, amount, bank):
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Invalid amount. Please enter a positive number.")
        self.balance += amount
        self.transactions.append(f"Deposited: ${amount:.2f} successfully!!!")

    def withdraw(self, amount, bank):
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Invalid amount. Please enter a positive number.")
        if amount > self.balance:
            raise ValueError("Withdrawal limit exceeded")
        if amount > bank.total_balance() - bank.total_loan():
            raise ValueError("The bank is bankrupt")
        self.balance -= amount
        self.transactions.append(f"Withdrawn: ${amount:.2f} successfully!!!")

    def check_balance(self):
        return self.balance

    def get_transactions(self):
        return self.transactions

    def take_loan(self, amount, bank):
        if self.loan_counter >= 2 or not bank.loan_feature_enabled:
            return "Loan limit exceeded or loan feature disabled"
        self.loan_counter += 1
        self.loan_quantity += amount
        self.balance += amount
        self.transactions.append(f"Loan taken: ${amount:.2f}")
        return f"Loan taken: ${amount:.2f}"

    def transfer(self, amount, account):
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        account.balance += amount
        self.transactions.append(f"Transferred: ${amount:.2f} to {account.account_number}")
        account.transactions.append(f"Received: ${amount:.2f} from {self.account_number}")

