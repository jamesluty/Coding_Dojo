from genericpath import exists


class User:
    bank_name = "First National Dojo"
    def __init__(self, name, email, dob, accountType = "Checking", int_rate = .01, balance = 0):
        self.name = name
        self.email = email
        self.dob = dob
        self.account = BankAccount(accountType, int_rate, balance)

    def make_deposit(self, amount, account):
        accountType = self.account.account_type
        if account == accountType:
            self.account.balance += amount
        else:
            print(f"{account} account does not exist!")
        return self

    def make_withdrawal(self, withdraw, account):
        accountType = self.account.account_type
        if account == accountType:
            self.account.balance -= withdraw
        else:
            print(f"{account} account does not exist!")
        return self

    def display_user_balance(self, account):
        accountType = self.account.account_type
        if account == accountType:
            print(f"User: {self.name}, Balance: ${self.account.balance}")
        else:
            print(f"{account} account does not exist!")

    def interest(self):
        self.account.balance += self.account.balance * self.account.int_rate
        return self.balance

    def transfer_money(self, otherUser, otherUserAccount, amount, account):
        account_type = self.account.account_type
        # other_account = otherUserAccount.account.account_type
        if self.account.balance >= amount and account == account_type:
            otherUser.account.deposit(amount, "Checking")
            self.make_withdrawal(amount, account)
            # print(f"User: {otherUser.name}, Balance: {otherUser.balance}")
            # print(f"User: {self.name}, Balance: {self.balance}")
        else:
            print("test")

class BankAccount:
    all_accounts = []
    def __init__(self, account_type, int_rate, balance):
        self.account_type = account_type 
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        return self

    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self

    def yield_interest(self):
        self.balance += self.balance * self.int_rate
        return self.balance

    @classmethod
    def display_all_info(cls):
        for account in cls.all_accounts:
            print(f"{account.account_type} account has a balance of {account.balance} with an interest rate of {account.int_rate}")


oliver = User("Oliver Oli", "guido@python.com", "2/12/2000", "Checking")
matt = User("Matty Matt", "monty@python.com", "9/6/1990", "Checking", .01, 0)
james = User("James Luty", "jluty@python.com", "1/25/1986", "Checking", .01, 0)
james_savings = User("James Luty", "jluty@python.com", "1/25/1986", "Savings", .8, 0)


oliver.make_deposit(500, "Checking").make_deposit(200, "Checking").make_deposit(1000, "Checking").make_withdrawal(300, "Checking") # .display_user_balance("Checking")
matt.make_deposit(1000, "Checking").make_deposit(1500, "Checking").make_withdrawal(500, "Checking").make_withdrawal(200, "Checking").make_withdrawal(300, "Checking").make_withdrawal(100, "Checking") # .display_user_balance("Checking")
james_savings.make_deposit(500, "Savings") # .display_user_balance("Savings")

print(james_savings.transfer_money("matt", "Checking", 500, "Savings"))

# BankAccount.display_all_info()

