#Layyana Junaid 23k-0056 BSAI-3A
#task 3

class Account:
    def __init__(self, account_no, account_bal, security_code):
        self.__account_no = account_no
        self.__account_bal = account_bal
        self.__security_code = security_code

    def print_account(self):
        print(f"Account number: {self.__account_no}")
        print(f"Account Balance: {self.__account_bal}")
        print(f"Security Code: {self.__security_code}")

account1 = Account(123456, 35000, 456)
account1.print_account()
