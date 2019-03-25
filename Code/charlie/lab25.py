
# Let's represent an ATM with a class containing two attributes: a balance and an interest rate. A newly created account will default to a balance of 0 and an interest rate of 0.1%. Implement the initializer, as well as the following functions:
class Atm:
    def __init__(self, account_balance = 0, interest_rate =0.1/100, transaction_summary = []):
        self.account_balance = account_balance
        self.interest_rate = interest_rate
        self.transaction_summary = transaction_summary


# check_balance() returns the account balance
    def check_balance(self):
        return self.account_balance

# deposit(amount) deposits the given amount in the account
    def deposit(self, in_money):
        self.account_balance += in_money
        self.transaction_summary.append(f"User deposited ${in_money}.")
        return self.account_balance

# check_withdrawal(amount) returns true if the withdrawn amount won't put the account in the negative
    def check_withdrawal(self, out_money):
        if self.account_balance >= out_money:
            return True


# withdraw(amount) withdraws the amount from the account and returns it
    def withdraw(self, out_money):
        if balance.check_withdrawal(out_money) == True:
            self.account_balance -= out_money
            self.transaction_summary.append(f"User withdrew ${out_money}.")
            return self.account_balance

        else:
            print("Not enough funds to complete this transaction.")
            return self.account_balance




# calc_interest() returns the amount of interest calculated on the account per month
    def calc_interest(self, time):
        #A = P(1 +rt)
        #t = months
        interest_earned = self.account_balance*(1 + ((self.interest_rate)*time))

        return interest_earned

#Add a new function print_transactions() to your class for printing out the list of transactions.
    def print_transactions(self):
        for transaction in self.transaction_summary:
            print(transaction)
        return print(f" Previous transacitons: \n {self.transaction_summary}")

#=================================Version 1====================================

#my initial balance.  setting the balance variable to the aAtm type
balance = Atm()

#calling the check balance method
print(balance.check_balance())

#calling the deposit method
in_money = round(int(input("How much money do you want to depost.\n: $")), 2)
balance.deposit(in_money)

#calling the check balance method
print(balance.check_balance())

#inputting how much money to withdraw, calls the check_withdrawal method, calls the withdraw funtio in the print statement
out_money = round(int(input("How much money do you want to withdraw? \n: $")), 2)
balance.check_withdrawal(out_money)
print(f"you have ${balance.withdraw(out_money)} remaining in your account")

#to determine the interest, i input how many months the account has been open and then call the calc_interest method.
time = float(input("How many months has your account been open"))
print(f" your total balance including interst earned is {balance.calc_interest(time)}")


#==================================Version 2===================================


# Version 2
# Have the ATM maintain a list of transactions. Every time the user makes a deposit or withdrawal, add a string to a list saying 'user deposited $15' or 'user withdrew $15'.





#==================================Version 3===================================
# Version 3
# Allow the user to enter commands into a REPL.
#
# > what would you like to do (deposit, withdraw, check balance, history)?
# > deposit
# > how much would you like to deposit?
# > $5
# > what would you like to do (deposit, withdraw, check balance, history)?
# > check balance
# > balance: $5
