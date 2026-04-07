# 🔹 Concept
# Restrict direct access to data
# Use private variables (__)

# when we add __private variable, it cannot access with the object reference, but we can use private variables in side the class using self.__private variable

class Account:
    def __init__(self, balance):
        # __ is a private variable
        self.__balance = balance
    
    def deposit(self, amount):
        if amount > 0 :
            self.__balance += amount
        else:
            print("Invalid amount")
    
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self.__balance

account = Account(1000)
account.deposit(500)
account.withdraw(200)
print(account.get_balance()) # 1300