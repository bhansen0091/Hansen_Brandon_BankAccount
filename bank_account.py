

class User:
    def __init__(self, name, email, initial_rate = 0.01, initial_balance = 0):
        self.name = name
        self.email = email
        self.accounts = [BankAccount(int_rate = initial_rate, balance = initial_balance)]

    def make_new_account(self, int_rate = 0.01, balance = 0):
        new_account = BankAccount(int_rate, balance)
        for account in self.accounts:
            if new_account.account_number <= account.account_number:
                new_account.make_acct_number()
        print(f"User: {self.name} created a new account.")
        self.accounts.append(new_account)

    def display_user_accounts(self):
        print(f"User: {self.name}")
        for account in self.accounts:
            print(f"Account: {account}")

    def make_deposit(self, amount, account = 1):
        self.accounts[account-1].account_balance += amount

    def make_withdrawal(self, amount, account = 1):
        if amount > self.accounts[account-1].account_balance:
            print(f"${amount} cannot be withdrawn from {self.accounts[account-1].account_number}.  Please try again.")
            return False
        self.accounts[account-1].account_balance -= amount
        return True

    def self_transfer(self, sender_acct, amount, receiver_acct):
        # is_success = False
        is_success = self.make_withdrawal(amount, sender_acct)
        if is_success:
            self.make_deposit(amount, receiver_acct)
            print(f"${amount} Transfered from Account: {sender_acct} to Account: {receiver_acct}.")
        else:
            print(f"${amount} cannot be withdrawn from {sender_acct}.  Please try again.")

    def user_to_user_transfer(self, sender_acct, amount, reciever_user, reciever_acct):
        is_success = self.make_withdrawal(amount, sender_acct)
        if is_success:
            reciever_user.make_deposit(amount, reciever_acct)
            print(f"${amount} Transfered from {self.name} Account: {sender_acct} to {reciever_user.name} Account: {reciever_acct}.")

    def __repr__(self):
        return f"{self.name} {self.email} {str(self.accounts)}"

    def __str__(self):
        return f"{self.name}, {self.email}, {self.accounts}"

class BankAccount:
    def __init__(self, int_rate = 0.01, balance = 0):
        self.account_balance = balance
        self.interest_rate = int_rate
        self.account_number = 1
        
    def make_acct_number(self):
        self.account_number += 1

    def display_account_info(self):
        print(f"Account Number: {self.account_number} | Balance: {self.account_balance} | Interest Rate: {self.interest_rate}")
        return self

    def yield_interest(self):
        if self.account_balance > 0:
            self.account_balance = (self.account_balance + (self.account_balance * self.interest_rate))
        return self

    def __repr__(self):
        return f"Account: {self.account_number} | Int_Rate: {self.interest_rate} | Balance: {self.account_balance}\n"

    def __str__(self):
        return f"{self.account_number} | {self.interest_rate} | {self.account_balance}"

# newUser1 = User("Bob", "bob@bobsemail.com", initial_balance = 300)
# newUser2 = User("Jane", "jane@janesemail.com", initial_rate = 0.5, initial_balance = 100)
# newUser3 = User("Dave", "dave@davesemail.com")
# newUser4 = User("Andy", "andy@andysemail.com", initial_rate = 0.1, initial_balance = 200)

# newUser1.display_user_accounts()
# newUser2.display_user_accounts()
# newUser3.display_user_accounts()
# newUser4.display_user_accounts()

# newUser1.make_deposit(100, 1)
# newUser1.make_new_account(balance=50)
# newUser1.make_withdrawal(10)
# newUser1.self_transfer(1, 50, 2)
# newUser1.display_user_accounts()

# newUser2.make_deposit(100, 1)
# newUser2.make_new_account(balance=50)
# newUser2.make_withdrawal(10)
# newUser2.self_transfer(1, 50, 2)
# newUser2.display_user_accounts()

# newUser1.display_user_accounts()
# newUser2.display_user_accounts()
# newUser1.user_to_user_transfer(1, 100, newUser2, 1)
# newUser1.display_user_accounts()
# newUser2.display_user_accounts()

# newUser1.accounts[0].yield_interest()
# newUser1.display_user_accounts()
