user_money = float(input("How much money do you have, written as a dollar amount (e.g. 10.45)? >"))
user_money = int(user_money * 100)
user_quarters = user_money // 25
user_money = user_money % 25
user_dimes = user_money // 10
user_money = user_money % 10
user_nickles = user_money // 5
user_money = user_money % 5
user_pennies = user_money // 1
print(f"You have {user_quarters} quarters, {user_dimes} dimes, {user_nickles} nickles, and {user_pennies} pennies.")
