class User:
    def __init__(self, name):
        self.name = name
        self.balance = 0

    def make_deposit(self, amount):
        self.balance += amount

    def make_withdrawal(self, amount):
        self.balance -= amount

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.balance}")

    def transfer_money(self, other_user, amount):
        self.balance -= amount
        other_user.balance += amount


user_a = User("Ahmed")
user_a.make_deposit(120)
user_a.make_deposit(150)
user_a.make_deposit(110)
user_a.make_withdrawal(100)
user_a.display_user_balance()

user_b = User("Mostafa")
user_b.make_deposit(120)
user_b.make_deposit(150)
user_b.make_withdrawal(50)
user_b.make_withdrawal(20)
user_b.display_user_balance()

user_c = User("Yomna")
user_c.make_deposit(200)
user_c.make_withdrawal(100)
user_c.make_withdrawal(20)
user_c.make_withdrawal(20)
user_c.display_user_balance()

user_a.transfer_money(user_c, 80)
user_a.display_user_balance()
user_c.display_user_balance()
