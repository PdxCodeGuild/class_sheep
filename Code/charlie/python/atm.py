

class Atm:
    """Performs a series of transactions similar\
 to that of an Automated Teller Machine."""

    def __init__(self,
                account_balance = 0,
                interest_rate =0.1/100,
                transaction_summary = []
                ):
        """This is the initializer, this function assumes the account balance
        is $0 and the interest reate is .1% """
        self.account_balance = account_balance
        self.interest_rate = interest_rate
        self.transaction_summary = transaction_summary



    def check_balance(self):
        """Calling this function will return the current balance. """
        return self.account_balance


    def deposit(self, in_money):
        """Calling this function will allow the user to add money to the account.
        Each deposit will be appended to the transaction_summary list."""
        self.account_balance += in_money
        self.transaction_summary.append(f"User deposited ${in_money}.")
        return self.account_balance

    def check_withdrawal(self, out_money):
        """Calling this funtion will return true if the account balance is
         greater than the user's withdrawal amount."""
        if self.account_balance >= out_money:
            return True

    def withdraw(self, out_money):
        """Calling this funtion will allow the user to deduct money from their account.
        Each deduction will be appended to the transaction_summary list."""
        if balance.check_withdrawal(out_money) == True:
            self.account_balance -= out_money
            self.transaction_summary.append(f"User withdrew ${out_money}.")
            return self.account_balance

        else:
            print("Not enough funds to complete this transaction.")
            return self.account_balance

    def calc_interest(self, time):
        """Calling this function will return the interest earned plus the
        current balance."""
        #A = P(1 +rt)
        #t = months
        interest_earned = self.account_balance*(1 + ((self.interest_rate)*time))
        return interest_earned

    def print_transactions(self):
        """Calling this function will return a list of transactions in an easy
        to read format."""
        for transaction in self.transaction_summary:
            print(transaction)
        print(f"remaining balance:\n ${self.account_balance}")
        return self.transaction_summary
