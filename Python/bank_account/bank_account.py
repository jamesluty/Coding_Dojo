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
        # return self

    def yield_interest(self):
        self.balance = self.balance * self.int_rate + self.balance
        return self

    @classmethod
    def display_all_info(cls):
        for account in cls.all_accounts:
            print(f"{account.account_type} account has a balance of {account.balance} with an interest rate of {account.int_rate}")

checking = BankAccount("Checking", .02, 7000)
savings = BankAccount("Savings", .08, 2000)

checking.deposit(500).deposit(200).deposit(1000).withdraw(2000).yield_interest() # .display_account_info()
savings.deposit(1000).deposit(1500).withdraw(500).withdraw(200).withdraw(300).withdraw(100).yield_interest() # .display_account_info()

BankAccount.display_all_info()