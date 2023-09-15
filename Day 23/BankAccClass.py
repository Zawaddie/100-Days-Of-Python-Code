class BankAccount:
    def __init__(self, account_number):
        self.account_number = account_number
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print(" You have Insufficient funds!")

    def get_balance(self):
        return str(self.balance)

# Create a bank account object
account = BankAccount("0123456789")

# Make deposits
account.deposit(1000)
account.deposit(500)

# Make a withdrawal
account.withdraw(200)

# Check the balance
balance = account.get_balance()
print("Current Balance:", balance)
