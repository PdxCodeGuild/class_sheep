# Lab 25: ATM
# Let's represent an ATM with a class containing two attributes: a balance and an interest rate. A newly created account will default to a balance of 0 and an interest rate of 0.1%. Implement the initializer, as well as the following functions:
#1.  check_balance() returns the account balance
#2. deposit(amount) deposits the given amount in the account
#3.  check_withdrawal(amount) returns true if the withdrawn amount won't put the account in the negative
#4.  withdraw(amount) withdraws the amount from the account and returns it
#5.  calc_interest() returns the amount of interest calculated on the account
# Version 2
# Have the ATM maintain a list of transactions. Every time the user makes a deposit or withdrawal, add a string to a list saying 'user deposited $15' or 'user withdrew $15'. Add a new function print_transactions() to your class for printing out the list of transactions.
#
# Version 3
# Allow the user to enter commands into a REPL.
# > what would you like to do (deposit, withdraw, check balance, history)?
# > deposit
# > how much would you like to deposit?
# > $5
# > what would you like to do (deposit, withdraw, check balance, history)?
# > check balance
# > balance: $5


class Atm:
    def __init__(self, b, r):
        self.b = b
        self.r = r

    def check_balance(self):
        return self.b

    def deposit(self, amount):
        self.b += amount
        return self.b

    def check_withdrawal(self, amount):
        if amount <= self.b:
            return True
        return False

    def withdraw(self, amount):
        return self.b - amount

    def calc_interest(self):
        return self.b*self.r

    def print_transactions(self, deposit, withdraw):
        transaction_list = []
        transaction_list.append(deposit())
        transaction_list.append(withdraw())
        return transation_list

atm = Atm(0, 0.1)
balance = atm.check_balance()
deposit = atm.deposit(100)
check_withdrawal = atm.check_withdrawal(150)
withdraw = atm.withdraw(50)
interest = atm.calc_interest()
transaction_list = atm.print_transactions(deposit, withdraw)

print (balance, deposit, check_withdrawal, withdraw, interest, transaction_list)
