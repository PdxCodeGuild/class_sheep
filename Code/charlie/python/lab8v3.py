
#====================VERSION 3- Custom Coin==========================


#i want to allow the user to create custom coin values.
coins = ['quarter', 'dime', 'nickel', 'penny']

values = []
coin_value = 0
for i in range(len(coins)):
    coin_value = int(input(f'How much do you want a {coins[i]} to be worth?\n:'))
    values.append(coin_value)

#Create a dictionary of custom coins, and then sort them from largest to smallest
coin_dictionary = {}
for i in range(len(coins)):
    if coins[i] not in coin_dictionary:
        coin_dictionary[coins[i]] = values[i]
sorted(coin_dictionary, reverse=True)
print(coin_dictionary)

#convert user change into the custom amount of pennies
user_change = float(input('how much money do you have?'))
total_pennies = round(user_change / coin_dictionary['penny'])
print(total_pennies)

#use total pennies to determine how many of the larger coins we have
quarters = total_pennies // coin_dictionary['quarter']
remainder = total_pennies % coin_dictionary['quarter']
dimes = remainder // coin_dictionary['dime']
remainder_step2 = remainder % coin_dictionary['dime']
nickels = remainder_step2 // coin_dictionary['nickel']
pennies = remainder_step2 % coin_dictionary['nickel']


print(f'quarters {quarters}, dimes {dimes}, nickels {nickels}, pennies {pennies}')
