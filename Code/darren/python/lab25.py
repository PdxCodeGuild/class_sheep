# lab25.py
'''ATM'''

import string

class ATM:

    '''Initializer'''
    def __init__(self):
        self.b = 0
        self.i = 0.1
        self.h = []

    '''Check Balance'''
    def balance(self):
        return f'Your current balance is ${self.b}'

    '''Make Deposit'''
    def deposit(self, d):
        self.d = d
        self.b += self.d
        self.h.append(f"+${self.d} deposit")
        return f'Successfully deposited ${self.d}. Your current balance is ${self.b}'

    '''Check for Overdraft'''
    def overdraft(self, c):
        self.c = c
        check = self.b - self.c
        if check < 0:
            return True

    '''Make Withdrawal'''
    def withdraw(self, w):
        self.w = w
        self.b -= self.w
        self.h.append(f"-${self.w} withdrawal")
        result = f'Successfully withdrew ${self.w}. Your current balance is ${self.b}.'
        return result

    '''Calculate Interest'''
    def interest(self):
        interest = self.i / 100
        with_interest = interest * self.b
        return f'With your current balance, the interest is ${with_interest}.'

    '''Print Transactions'''
    def transactions(self):
        transaction_record = ''
        for item in self.h:
            transaction_record += item + '\n'
        transaction_record += f'Balance: ${self.b}'
        return transaction_record

    '''User Interface'''
    def ATM_command(self, c):
        if c == 'check balance':
            output = a.balance()
            return(f'\n{output}')
        if c == 'make deposit':
            d = input('Please enter the amount you wish to deposit: ')
            for letter in d:
                if letter not in string.digits:
                    return('Invalid Deposit')
            d = int(d)
            output = a.deposit(d)
            return(f'\n{output}')
        if c == 'make withdrawal':
            w = input('Please enter the amount you wish to withdraw: ')
            for letter in w:
                if latter not in string.digits:
                    return('Invalid Withdrawal')
            w = int(w)
            overdraft_check = a.overdraft(w)
            if overdraft_check == True:
                return('\nInsufficient account balance.')
            output = a.withdraw(w)
            return(f'\n{output}')
        if c == 'calculate interest':
            output = a.interest()
            return(f'\n{output}')
        if c == 'transaction history':
            output = a.transactions()
            return(f'\n{output}')

a = ATM() # call the initializer, instantiate the class
commands = ['check balance', 'make deposit', 'make withdrawal', 'calculate interest', 'transaction history', 'exit']

while True:
    user_input = input("\nCheck Balance \nMake Deposit \nMake Withdrawal \nCalculate Interest \nTransaction History \nPlease select an option, or enter 'Exit' when finished: ")
    user_input = user_input.lower()
    print(f'\n{user_input} \n')
    if user_input not in commands:
        print("Invalid command.")
        continue
    if user_input == 'exit':
        print("Thank you for your visit today.")
        break
    else:
        result = a.ATM_command(user_input)
        if result == '\nInsufficient account balance.':
            print(result)
            continue
        print(result)
