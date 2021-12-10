"""
Create a new BankAccount class. 
Balance should start at zero. 
Interest rate

Class BankAccount
"""

class BankAccount:
    
    def __init__(self, intRate, balance):
        self.intRate = intRate
        self.balance = balance
    
    def deposit(self,amount):
        self.balance = self.balance + amount
        return self
    
    def withdraw(self, amount):
        self.balance = self.balance - amount
        return self

    def display_account_info(self):
        print(f'The users interest rate is {self.intRate}% and balance is {self.balance}')

    def yield_interest_rate(self):
        if self.balance > 0:
            self.balance = (self.balance * self.intRate) + self.balance
            self.display_account_info()
        else:
            print('We are sorry, your account is negative')


paige_acct = BankAccount(.02,100)
liina_acct = BankAccount(.04, 300)

paige_acct.deposit(500).deposit(150).deposit(300).yield_interest_rate()
liina_acct.deposit(400).deposit(900).withdraw(300).withdraw(50).withdraw(12).yield_interest_rate()


