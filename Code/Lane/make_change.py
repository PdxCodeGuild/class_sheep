user_money = ''

user_money = int(input("How many pennies do you have?: "))

user_quarters = user_money// 25, 'quarters'
user_money = user_money % 25
user_dimes = user_money // 10, 'dimes'
user_money = user_money % 10
user_nickels = user_money // 5, 'nickels'
user_money = user_money % 5
user_pennies = user_money // 1, 'pennies'
user_money = user_money % 1
print(f"You have:\n{user_quarters}\n{user_dimes}\n{user_nickels}\n{user_pennies}")

#
# print('You have', user_quarters, user_dimes, user_nickels, user_pennies)
