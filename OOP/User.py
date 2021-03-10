class User:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    
    def make_deposit(self, amount):
        self.balance += amount

    def make_withdrawl(self, amount):
        self.balance -= amount

    def display_user_balance(self):
        print(f"User: {self.name} Balance: $ {self.balance}")

    def transfer_money(self, other_user, amount):
        self.balance -= amount
        other_user.balance += amount

rachel= User("Rachel", 500)
caleb= User("Caleb", 900)
ryan= User("Ryan", 700)

rachel.make_deposit(50)
rachel.make_deposit(100)
rachel.make_deposit(20)
rachel.make_withdrawl(200)
rachel.display_user_balance()

caleb.make_deposit(45)
caleb.make_deposit(100)
caleb.display_user_balance()

ryan.make_deposit(300)
ryan.make_withdrawl(30)
ryan.make_withdrawl(10)
ryan.make_withdrawl(250)
ryan.display_user_balance()

rachel.transfer_money(ryan, 60)
rachel.display_user_balance()
ryan.display_user_balance()