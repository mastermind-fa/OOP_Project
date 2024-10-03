from bank import Bank
from account import Account
from admin import Admin


bank = Bank()
admin = Admin()

while True:
    print("\nWelcome to the Bank!")
    print("1. Register")
    print("2. Login")
    print("3. Admin Actions")
    print("4. Exit")
    choice = input("Choose an option: ")

    if choice == '1':  
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        address = input("Enter your address: ")
        account_type = input("Enter account type (savings/current): ")
        admin.add_user(bank, name, email, address, account_type)
        print("Registration successful!")

    elif choice == '2':  
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
                        account.deposit(amount,bank)
                        print("Deposit successful!")
                    except ValueError as e:
                        print(e)

                elif action == '3':  
                    amount = float(input("Enter amount to withdraw: "))
                    try:
                        account.withdraw(amount, bank)
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
                    result = account.take_loan(loan_amount, bank)
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
