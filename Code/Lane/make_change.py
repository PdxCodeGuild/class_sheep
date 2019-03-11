#Lab 8: Make Change
#Version 1
#convert money from pennies into the other coins

user_money = ''

user_money = int(input("How many pennies do you have?: "))

user_quarters = user_money // 25, "quarters" #find how many quarters in the user input by dividing by 25
user_money = user_money % 25 #find the remainder after pulling out all the quarters
user_dimes = user_money // 10, "dimes" #divide the user money by 10 to see how many dimes are there
user_money = user_money % 10 #find the remainder after all the 10's have been pulled out
user_nickels = user_money // 5, "nickels" #divide the user money by 5 to see how many nickels are there
user_money = user_money % 5 #find the remainder after all the 5's have been pulled out
user_pennies = user_money // 1, "pennies" #divide user_money by one to see how many pennies there are

print(f"You have:\n{user_quarters}\n{user_dimes}\n{user_nickels}\n{user_pennies}")



#version 2, convert a dollar amount to total pennies

# user_money = ''
#
# #set user input to convert to a float variable
# user_money = float(input("How much money do you have?: "))
#
# #The round returns the floating point number rounded off to the given ndigits digits after the decimal point. If no ndigits is provided, it rounds off the number to the nearest integer.
# user_pennies = round(user_money * 100) # *100 to get the dollar amount to pennies
#
# print(f"You have {user_pennies} pennies.")
