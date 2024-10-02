from account import Account
class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, name, email, account_type):
        new_account = Account(name, email, account_type)
        self.accounts[new_account.account_number] = new_account
        
    def delete_account(self, account_number):
        if account_number in self.accounts:
            del self.accounts[account_number]
            print("Account deleted successfully.")
        else:
            print("Account does not exist")
            
    def show_all_accounts(self):
        for account_number, account in self.accounts.items():
            print(f"{account_number} - {account.account_type}")
            print()
            
    def show_account(self, account_number):
        if account_number in self.accounts:
            account = self.accounts[account_number]
            print(f"Account number: {account.account_number}")
            print(f"Name: {account.name}")
            print(f"Email: {account.email}")
            print(f"Account type: {account.account_type}")
            print(f"Balance: {account.balance}")
            print(f"Transactions: {account.transactions}")
            print(f"Loan quantity: {account.loan_quantity}")
        else:
            print("Account does not exist")
            
    def total_balance(self):
        return sum(account.balance for account in self.accounts.values())
    
    def total_loan(self):
        return sum(account.loan_quantity for account in self.accounts.values())
    def total_transactions(self):
        return sum(len(account.transactions) for account in self.accounts.values())
    