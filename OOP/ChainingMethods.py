class User:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    
    def make_deposit(self, amount):
        self.balance += amount
        return self

    def make_withdrawl(self, amount):
        self.balance -= amount
        return self

    def display_user_balance(self):
        print(f"User: {self.name} Balance: $ {self.balance}")
        return self

    def transfer_money(self, other_user, amount):
        self.balance -= amount
        other_user.balance += amount
        return self

rachel= User("Rachel", 500)
caleb= User("Caleb", 900)
ryan= User("Ryan", 700)

rachel.make_deposit(50).make_deposit(100).make_deposit(20).make_withdrawl(200).display_user_balance()

caleb.make_deposit(45).make_deposit(100).display_user_balance()

ryan.make_deposit(300).make_withdrawl(30).make_withdrawl(10).make_withdrawl(250).display_user_balance()

rachel.transfer_money(ryan, 60).display_user_balance().display_user_balance()