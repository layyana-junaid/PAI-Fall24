#Layyana Junaid 23k-0056
#Lab 4 task 8

class Account:
    class Account:
        def __init__(self):
            self.__account_no = None
            self.__account_bal = None
            self.__security_code = None

        def initialize_and_print(self, account_no, account_bal, security_code):
            self.__account_no = account_no
            self.__account_bal = account_bal
            self.__security_code = security_code

            print(f"Account Number: {self.__account_no}")
            print(f"Account Balance: ${self.__account_bal:.2f}")
            print(f"Security Code: {self.__security_code}")


account = Account()
account.initialize_and_print("123456789", 1500.75, "ABC123")
