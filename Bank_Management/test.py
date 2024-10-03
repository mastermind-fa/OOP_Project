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

    def deposit(self, amount):
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Invalid amount. Please enter a positive number.")
        self.balance += amount
        self.transactions.append(f"Deposited: ${amount:.2f} successfully!!!")

    def withdraw(self, amount):
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

    def take_loan(self, amount):
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



bank = Bank()
admin = Admin()

while True:
    print("\nWelcome to the Bank!")
    print("1. Register")
    print("2. Login")
    print("3. Admin Actions")
    print("4. Exit")
    choice = input("Choose an option: ")

    if choice == '1':  # Register
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        address = input("Enter your address: ")
        account_type = input("Enter account type (savings/current): ")
        admin.add_user(bank, name, email, address, account_type)
        print("Registration successful!")

    elif choice == '2':  # Login
        account_number = int(input("Enter your account number: "))
        account = bank.find_account(account_number)

        if account:
            print(f"Welcome, {account.name}!")
            while True:
                print("\n1. Check Balance")
                print("2. Deposit")
                print("3. Withdraw")
                print("4. Transfer")
                print("5. Take Loan")
                print("6. Show Transactions")
                print("7. Logout")
                action = input("Choose an action: ")

                if action == '1':  
                    print(f"Your balance is: ${account.check_balance():.2f}")

                elif action == '2':  
                    amount = float(input("Enter amount to deposit: "))
                    try:
                        account.deposit(amount)
                        print("Deposit successful!")
                    except ValueError as e:
                        print(e)

                elif action == '3':  
                    amount = float(input("Enter amount to withdraw: "))
                    try:
                        account.withdraw(amount)
                        print("Withdrawal successful!")
                    except ValueError as e:
                        print(e)

                elif action == '4':  
                    dest_account = int(input("Input Account Number: "))
                    amount = float(input("Enter amount: "))
                    if dest_account in bank.accounts:
                        try:
                            receiver = bank.accounts[dest_account]
                            account.transfer(amount, receiver)
                            print("Transfer successful!")
                        except ValueError as e:
                            print(e)
                    else:
                        print("Account Not found")
                        
                elif action == '5':  
                    loan_amount = int(input("Input loan amount: "))
                    result = account.take_loan(loan_amount)
                    print(result)

                elif action == '6':  
                    transactions = account.get_transactions()
                    print("Transactions:")
                    for transaction in transactions:
                        print(transaction)

                elif action == '7':  
                    print("Logging out...")
                    break
                else:
                    print("Invalid action. Please try again.")
        else:
            print("Account not found.")

    elif choice == '3':  
        while True:
            command = input("1. Admin Login\n2. Admin Register\n3. Exit Admin Actions\nChoose an option: ")
            if command == '1':  
                username = input("Enter username: ")
                password = input("Enter password: ")
                if admin.is_admin(username, password):
                    print("Login successful!")
                    while True:
                        admin_action = input("1. Show all accounts\n2. Delete account\n3. Show Particular Account\n4. Total Balance\n5. Total Loan\n6. Toggle Loan Feature\n7. Logout\nChoose an action: ")
                        if admin_action == '1':
                            admin.show_all_accounts(bank)
                        elif admin_action == '2':
                            account_number = int(input("Enter the account number to delete: "))
                            admin.delete_user(bank, account_number)
                        elif admin_action == '3':
                            account_number = int(input("Enter the account number to show: "))
                            admin.show_account(bank, account_number)
                        elif admin_action == '4':
                            admin.total_balance(bank)
                        elif admin_action == '5':
                            admin.total_loan(bank)
                        elif admin_action == '6':
                            admin.toggle_loan_feature(bank)
                        elif admin_action == '7':
                            print("Logging out...")
                            break
                        else:
                            print("Invalid action. Please try again.")
                else:
                    print("Invalid username or password. Please try again.")
                    
            elif command == '2':  
                username = input("Enter username: ")
                password = input("Enter password: ")
                admin.add_admin(username, password)

            elif command == '3':  
                break

    elif choice == '4':  
        print("Thank you for using the bank. Goodbye!")
        break
    else:
        print("Invalid option. Please choose again.")
