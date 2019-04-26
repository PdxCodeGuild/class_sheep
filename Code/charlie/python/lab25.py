from atm import Atm
#=================================Version 1====================================

#my initial balance.  setting the balance variable to the aAtm type
var = Atm()

#calling the check balance method
print(var.check_balance())

#calling the deposit method
user_deposit = round(int(input("How much money do you want to depost.\n: $")), 2)
var.deposit(user_deposit)

#calling the check balance method
print(var.check_balance())

#inputting how much money to withdraw, calls the check_withdrawal method, calls the withdraw funtio in the print statement
user_withdrawal = round(int(input("How much money do you want to withdraw? \n: $")), 2)
var.check_withdrawal(user_withdrawal)
print(f"you have ${var.withdraw(user_withdrawal)} remaining in your account")

#to determine the interest, i input how many months the account has been open and then call the calc_interest method.
time = float(input("How many months has your account been open"))
print(f" your total balance including interst earned is {var.calc_interest(time)}")
