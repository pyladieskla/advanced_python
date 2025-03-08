"""
Access Modifiers: Access modifiers are used to control access to the data
and methods of a class.

--> public: Accessible from anywhere
--> private: Accessible only within the class, 
    class attribute is defined with an underscore eg: _balance
"""

class BankAccount:
    def __init__(self, balance):
        self._balance = balance      

    def deposit(self, amount):
        self._balance = self._balance + amount
        # self._balance += amount
    
    def get_balance(self):
        return self._balance
    
account = BankAccount(100)
account.deposit(50)
print(account.get_balance())


