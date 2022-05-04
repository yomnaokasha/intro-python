class User:
    def __init__(self, name):
        self.name = name
        self.balance = 0

    def make_deposit(self, amount):
        self.balance += amount
        return self

    def make_withdrawal(self, amount):
        self.balance -= amount
        return self

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.balance}")
        return self

    def transfer_money(self, other_user, amount):
        self.balance -= amount
        other_user.balance += amount


user_a = User("Ahmed").make_deposit(120).make_deposit(150).make_deposit(110).make_withdrawal(100).display_user_balance()

user_b = User("Mostafa").make_deposit(120).make_deposit(150).make_withdrawal(50).make_withdrawal(20).display_user_balance()

user_c = User("Yomna").make_deposit(200).make_withdrawal(100).make_withdrawal(20).make_withdrawal(20).display_user_balance()

user_a.transfer_money(user_c, 80)
user_a.display_user_balance()
user_c.display_user_balance()
