# Lab 25: ATM
# Let's represent an ATM with a class containing two attributes: a balance and an interest rate. A newly created account will default to a balance of 0 and an interest rate of 0.1%. Implement the initializer, as well as the following functions:
#1.  check_balance() returns the account balance
#2. deposit(amount) deposits the given amount in the account
#3.  check_withdrawal(amount) returns true if the withdrawn amount won't put the account in the negative
#4.  withdraw(amount) withdraws the amount from the account and returns it
#5.  calc_interest() returns the amount of interest calculated on the account
# Version 2
# Have the ATM maintain a list of transactions. Every time the user makes a deposit or withdrawal, add a string to a list saying 'user deposited $15' or 'user withdrew $15'. Add a new function print_transactions() to your class for printing out the list of transactions.

# create class
class Atm:

    # assigning class attributes
    def __init__(self, b=0, r=0.001):
        self.b = b
        self.r = r
        self.transactions = []

    # method to check balance
    def check_balance(self):
        return f'Your balance is ${self.b}.'

    # method to make a deposit and add it to the list of transactions
    def deposit(self, amount):
        self.b += amount
        self.transactions.append(f'Amount deposited: ${amount}.')

    # method to check if the withdrawal amount is greater than the balance
    def check_withdrawal(self, amount):
        if amount <= self.b:
            return True
        return False

    # method to withdraw money and add to list of transactions
    def withdraw(self, amount):
        self.b -= amount
        self.transactions.append(f'Amount withdrawn: ${amount}.')

    # method to calculate interest based on balance and interest rate
    def calc_interest(self):
        return self.b*self.r

    # method to print list of past transactions
    def print_transactions(self):
        return '\n'.join(self.transactions)

#instantiations and variable assignments
# atm = Atm(0, 0.001)
# balance = atm.check_balance()
# deposit = atm.deposit(100)
# check_withdrawal = atm.check_withdrawal(200)
# withdraw = atm.withdraw(100)
# interest = atm.calc_interest()
# transaction_list = atm.print_transactions()


# Version 3
# Allow the user to enter commands into a REPL.
# > what would you like to do (deposit, withdraw, check balance, history)?


atm = Atm()
while True:
    # get command and lowercase it
    user_input = input('What would you like to do: deposit, withdraw, check balance, history, exit? > ').lower()
    # escape loop option to exit program
    if user_input == 'exit':
        print ('Thank you! Have a nice day.')
        break
    # make a deposit
    elif user_input == 'deposit':
        user_deposit = float(input('How much would you like to deposit? > '))
        atm.deposit(user_deposit)
    # make a withdrawal
    elif user_input == 'withdraw':
        user_withdraw = float(input('How much would you like to withdraw? > '))
        # check if withdrawal amount is valid
        check_withdrawal = atm.check_withdrawal(user_withdraw)
        # allow withdrawal if valid amount
        if check_withdrawal:
            atm.withdraw(user_withdraw)
        # tell user withdrawal is over their balance and restart loop
        if check_withdrawal == False:
            print ('That amount is more than your balance. Please select a different amount.')
    # check balance
    elif user_input == 'check balance':
        print(atm.check_balance())
    # print past transactions
    elif user_input == 'history':
        print(atm.print_transactions())
    # catchall for bad commands
    else:
        print('Invalid command. Please try again.')
