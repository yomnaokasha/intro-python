from bank_account import BankAccount


class User:
    def __init__(self, name):
        self.name = name
        self.accounts = {
            "Checking": BankAccount(interest_rate=0.02, balance=0),
            "Savings": BankAccount(interest_rate=0.07, balance=0),
        }

    def deposit(self, amount, account_name):
        self.accounts[account_name].deposit(amount)

    def withdraw(self, amount, account_name):
        self.accounts[account_name].withdraw(amount)

    def display_user_balance(self):
        checking = self.accounts["Checking"]
        print(f"User: {self.name}, Checking Balance: {checking.balance}")
        savings = self.accounts["Savings"]
        print(f"User: {self.name}, Savings Balance: {savings.balance}")


ahmed = User("ahmed")
ahmed.deposit(200, "Checking")
ahmed.withdraw(50, "Checking")
ahmed.deposit(500, "Savings")
ahmed.withdraw(20, "Savings")
ahmed.display_user_balance()
