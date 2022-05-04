# class BankAccount:
#     all_accounts = []

#     @classmethod
#     def get_info(cls):
#         for bank_account in cls.all_accounts:
#             bank_account.display_account()

#     def __init__(self, interest_rate, balance):
#         self.interest_rate = interest_rate
#         self.balance = balance
#         BankAccount.all_accounts.append(self)

#     def deposit(self, amount):
#         self.balance += amount
#         return self

#     def withdraw(self, amount):
#         if self.balance > amount:
#             self.balance -= amount
#         else:
#             print("Insufficient funds: Charging a $5 fee")
#             self.balance -= 5
#         return self

#     def display_account(self):
#         print(f"Balance: ${self.balance}")
#         return self

#     def yield_interest(self):
#         if self.balance > 0:
#             interest = self.interest_rate * self.balance
#             self.balance += interest
#         return self


# if __name__ == "__main__":
#     firstaccount = BankAccount(0.07, 100)
#     secondaccount = BankAccount(0.02, 50)

#     firstaccount.deposit(20).deposit(50).deposit(110).withdraw(
#         100
#     ).yield_interest().display_account()
#     secondaccount.deposit(120).deposit(250).withdraw(10).withdraw(50).withdraw(
#         90
#     ).withdraw(30).yield_interest().display_account()

#     BankAccount.get_info()


# Grad Student also inherits from the Person class
favorite_color = input(
    "What is your favorite color? "
)  # input takes a prompt, which needs to be a string
print(
    f"Your favorite color is: {favorite_color}"
)  # output, prints the color given to the console
