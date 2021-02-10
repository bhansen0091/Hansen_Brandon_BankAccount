

class BankAccount:
    def __init__(self, int_rate = 0.01, balance = 0):
        self.account_balance = balance
        self.interest_rate = int_rate

    def deposit(self, amount):
        self.account_balance += amount
        return self

    def withdraw(self, amount):
        if amount > self.account_balance:
            print("Insufficient funds")
        else:
            self.account_balance -= amount
        return self

    def display_account_info(self):
        print(f"Balance: {self.account_balance} | Interest Rate: {self.interest_rate}")
        return self

    def yield_interest(self):
        if self.account_balance > 0:
            self.account_balance = (self.account_balance + (self.account_balance * self.interest_rate))
        return self

new_account_1 = BankAccount()
new_account_2 = BankAccount(0.02, 10)

new_account_1.deposit(10).deposit(10).deposit(10).withdraw(10).yield_interest().display_account_info()
new_account_2.deposit(15).deposit(15).withdraw(5).withdraw(5).withdraw(5).withdraw(5).yield_interest().display_account_info()