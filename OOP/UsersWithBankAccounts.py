class User:
    def __init__(self, name ,int_rate=.01, balance=0):
        self.name = name
        self.account=BankAccount(int_rate, balance)
    
    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    def make_withdraw(self, amount):
        self.account.withdraw(amount)
        return self

    def display_user_balance(self):
        # print(f"User: {self.name} Balance: $ {self.balance}")
        self.account.display_account_info()
        return self

    # def transfer_money(self, other_user, amount):
    #     self.balance -= amount
    #     other_user.balance += amount


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

rachel= User("Rachel Lorentson", .05, 600)
rachel.make_deposit(5000).display_user_balance()
