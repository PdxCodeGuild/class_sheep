from atm import Atm

#=================================Version 2====================================
# Have the ATM maintain a list of transactions. Every time the user makes a deposit or withdrawal, add a string to a list saying 'user deposited $15' or 'user withdrew $15'.

balance = Atm()

user_deposit = int(input('how much do you want to deposit?'))

balance.deposit(user_deposit)

user_withdrawal = int(input('how much do you want to withdraw?'))

balance.withdraw(user_withdrawal)

balance.print_transactions()
