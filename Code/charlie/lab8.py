
# #Ver 3
# #===========================================================================
#Defining the coin dictionary

#i want to allow the user to create custom coin values.
user_coins = ['quarters', 'dimes', 'nickels', 'penny']

coin_values = []
coin_value = 0
for i in range(len(user_coins)):
    coin_value = int(input(f'How much do you want a {user_coins[i]} to be worth?'))
    coin_values.append(coin_value)

#I want to create a dictionary of custom coins, and then sort them from largest to smallest
custom_coins = {}
for i in range(len(user_coins)):
    if user_coins[i] not in custom_coins:
        custom_coins[user_coins[i]] = coin_values[i]
sorted(custom_coins, reverse=True)

user_change = float(input('how much money do you have?'))
total_pennies = round(user_change * 100.00)
print(total_pennies)

quarters = total_pennies // 25
remainder = total_pennies % 25
dimes = remainder // 10
remainder2 = remainder % 10
nickels = remainder2 // 5
remainder3 = remainder2 % 5
pennies = remainder3 // 1


print(f'quarters {quarters}, dimes {dimes}, nickels {nickels}, pennies {pennies}')





# change_dict = {
#         'quarters': 25,
#         'dimes': 10,
#         'nickels': 5,
#         'pennies': 1
# }
# user_change = float(input('how much change do you have?'))
# total_pennies = round((user_change * 100.00))
# print(total_pennies)
#
# quarters = (total_pennies) // 25
# remainder = total_pennies % 25
# dimes = (remainder) // 10
# remainder2 = remainder % 10
# nickels = (remainder2) // 5
# remainder3 = remainder2 % 5
# pennies = (remainder3) // 1
#
#
# print(f'quarters {quarters}, dimes {dimes}, nickels {nickels}, pennies {pennies}')
# #
# dimes= remainder % 10
# remainder2 = user_change -
