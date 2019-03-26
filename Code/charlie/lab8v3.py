
#====================VERSION 3- Custom Coin==========================


#i want to allow the user to create custom coin values.
user_coins = ['quarter', 'dime', 'nickel', 'penny']

coin_values = []
coin_value = 0
for i in range(len(user_coins)):
    coin_value = int(input(f'How much do you want a {user_coins[i]} to be worth?\n:'))
    coin_values.append(coin_value)

#I want to create a dictionary of custom coins, and then sort them from largest to smallest
custom_coins = {}
for i in range(len(user_coins)):
    if user_coins[i] not in custom_coins:
        custom_coins[user_coins[i]] = coin_values[i]
sorted(custom_coins, reverse=True)
print(custom_coins)

user_change = float(input('how much money do you have?'))
total_pennies = round(user_change / custom_coins['penny'])
print(total_pennies)

quarters = total_pennies // custom_coins['quarter']
remainder = total_pennies % custom_coins['quarter']
dimes = remainder // custom_coins['dime']
remainder_step2 = remainder % custom_coins['dime']
nickels = remainder_step2 // custom_coins['nickel']
pennies = remainder_step2 % custom_coins['nickel']


print(f'quarters {quarters}, dimes {dimes}, nickels {nickels}, pennies {pennies}')
