user_money = ''

user_money = int(input("How many pennies do you have?: "))

user_quarters = user_money//25, "quarters"
user_money = user_money % 25
user_dimes = user_money // 10, "dimes"
user_money = user_money % 10
user_nickels = user_money // 5, "nickels"
user_money = user_money % 5
user_pennies = user_money // 1, "pennies"
user_money = user_money % 1
print(f"You have {user_quarters} quarters, {user_dimes} dimes, {user_nickels} nickels, and {user_pennies} pennies")
