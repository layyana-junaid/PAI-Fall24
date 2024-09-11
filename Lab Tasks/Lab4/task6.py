#Layyana Junaid 23k-0056
#Lab4 task 6

#account_number, balance,date_of_opening and customer_name, and methods like deposit, withdraw, and check_balance.
class BankAccount:
    def __init__(self, account_number, balance, date_of_opening, customer_name):
        self.account_number = account_number
        self.balance = balance
        self.date_of_opening = date_of_opening
        self.customer_name = customer_name
    
    def printing_data(self):
        print(f"Account Number: {self.account_number}")
        print(f"Balance: {self.balance}")
        print(f"Date of Opening: {self.date_of_opening}")
        print(f"Customers Name: {self.customer_name}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f}. New balance is ${self.balance:.2f}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew ${amount:.2f}. New balance is ${self.balance:.2f}.")
            else:
                print("Insufficient Balance.")

    def check_balance(self):
        print(f"Current balance is ${self.balance:.2f}.")

account = BankAccount(
        account_number="1234567890",
        customer_name="Layyana Junaid",
        balance= 320000.00,
        date_of_opening= 21 
    )
account.printing_data()

account.deposit(250.00)

account.withdraw(100.00)

account.check_balance()

