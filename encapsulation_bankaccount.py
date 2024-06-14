class BankAccount:
    def __init__(self,account_number,balance):
        self.__account_number = account_number
        self.__balance = balance
    def deposite(self,amount):
        self.__balance+=amount
    def withdraw(self,amount):
        if amount<=self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient Balance")
    def get_balance(self):
        return self.__balance

account = BankAccount("3636939345", 2000)
print(account.get_balance())

account.withdraw(500)
# print(account.withdraw(500))
print(account.get_balance())

account.deposite(2500)
print(account.get_balance())