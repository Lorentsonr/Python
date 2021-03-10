class BankAccount:
    def __init__(self, int_rate=.01, balance=0):
        self.int_rate=int_rate
        self.balance=balance
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        if self.balance-amount < 0:
            print("Insufficient funds: Charging a $5 fee")
            self.balance-= 5
        else:
            self.balance-= amount
        return self
    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self
    def yield_interest(self):
        if self.balance > 0:
            self.balance *= self.int_rate + 1
        return self

acct1=BankAccount(.02, 500)
acct2=BankAccount(.1, 600)
acct1.deposit(50).deposit(400).deposit(20).withdraw(300).yield_interest().display_account_info()
acct2.deposit(20).deposit(200).withdraw(50).withdraw(10).withdraw(20).withdraw(70).yield_interest().display_account_info()