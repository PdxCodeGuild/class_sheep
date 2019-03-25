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
        print(f"remaining balance:\n ${self.account_balance}")
        return self.transaction_summary



#===============================Version 3====================================

balance = Atm()

while True:

    user_input = input("deposit, withdraw, check balance, history\n :" )

    if user_input == 'cancel':
        break

    if user_input == 'deposit':
        user_deposit = round(int(input("How much money do you want to deposit.\n: $")), 2)
        balance.deposit(user_deposit)
        print(balance.check_balance())

    elif user_input == 'withdraw':
        user_withdrawal = round(int(input("How much money do you want to withdraw? \n: $")), 2)
        balance.check_withdrawal(user_withdrawal)
        print(f"you have ${balance.withdraw(user_withdrawal)} remaining in your account")

    elif user_input == 'check_balance': #time is months
        time = float(input("How many months has your account been open"))
        print(f" your total balance including interst earned is {balance.calc_interest(time)}")

    elif user_input == 'history':
        balance.print_transactions()
