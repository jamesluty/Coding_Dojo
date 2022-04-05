class User:
    bank_name = "First National Dojo"
    def __init__(self, name, email, dob):
        self.name = name
        self.email = email
        self.dob = dob
        self.balance = 0

    def make_deposit(self, amount):
        self.balance += amount
        return amount

    def make_withdrawal(self, withdraw):
        self.balance -= withdraw
        return withdraw
    
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.balance}")

    def transfer_money(self, otherUser, amount):
        otherUser.make_deposit(amount)
        self.make_withdrawal(amount)
        print(f"User: {otherUser.name}, Balance: {otherUser.balance}")
        print(f"User: {self.name}, Balance: {self.balance}")

oliver = User("Oliver Oli", "guido@python.com", "2/12/2000")
matt = User("Matty Matt", "monty@python.com", "9/6/1990")
james = User("James Luty", "jluty@python.com", "1/25/1986")

# Making deposits to accounts
oliver.make_deposit(100)
oliver.make_deposit(200)
oliver.make_deposit(500)
matt.make_deposit(250)
james.make_deposit(2000000)

# print(oliver.balance)
# print(matt.balance)

# Making withdrawls from accounts
oliver.make_withdrawal(100)
matt.make_withdrawal(20)
matt.make_withdrawal(100)
james.make_withdrawal(20000)

# print(oliver.balance)
# print(matt.balance)
# print(james.balance)

# Transfer
james.transfer_money(matt, 500)

# oliver.display_user_balance()
# matt.display_user_balance()
# james.display_user_balance()
