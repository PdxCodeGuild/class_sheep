from atm import Atm

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
