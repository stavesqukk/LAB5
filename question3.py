#3. Create a class BankAccount with attributes account_holder,
#ccount_number, and balance.
# Add methods deposit(amount) and withdraw(amount) that update the
#alance.
# Add a method show_balance() that prints the current balance.
# Create an object and perform a deposit, a withdrawal, and show the
#alance.

class BankAccount:
    def __init__(self, account_holder, account_number, balance):
        self.ah = account_holder
        self.an = account_number
        self.b = balance

    def deposit(self, amount):
        self.b += amount 

    def withdraw(self, amount):
        if amount <= self.b:   
            self.b -= amount 
        else:
            print("Insufficient balance!")

    def show_balance(self):
        print(f"{self.ah} has account number {self.an} with balance {self.b}")

a = BankAccount("muskan", "2023005", 12000)

a.show_balance()
a.deposit(1200)
a.show_balance()
a.withdraw(1300)
a.show_balance()
