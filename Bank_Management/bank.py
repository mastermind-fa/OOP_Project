class Bank:
    def __init__(self):
        self.accounts = {}
        self.loan_feature_enabled = True  

    def create_account(self, account):
        self.accounts[account.account_number] = account

    def delete_account(self, account_number):
        if account_number in self.accounts:
            del self.accounts[account_number]
            print("Account deleted successfully.")
        else:
            print("Account does not exist")

    def find_account(self, account_number):
        return self.accounts.get(account_number, None)

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
        else:
            print("Account does not exist")

    def total_balance(self):
        return sum(account.balance for account in self.accounts.values())

    def total_loan(self):
        return sum(account.loan_quantity for account in self.accounts.values())

    def total_transactions(self):
        return sum(len(account.transactions) for account in self.accounts.values())

    def toggle_loan_feature(self):
        self.loan_feature_enabled = not self.loan_feature_enabled
        state = "enabled" if self.loan_feature_enabled else "disabled"
        print(f"Loan feature has been {state}.")
