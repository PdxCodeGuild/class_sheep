# prompt user for input, which is used to determine how many of each coin is possible.

user_change = float(input('how much money do you have?'))
total_pennies = round(user_change * 100.00)
print(total_pennies)

quarters = total_pennies // 25
remainder = total_pennies % 25
dimes = (remainder) // 10
remainder2 = remainder % 10
nickels = (remainder2) // 5
remainder3 = remainder2 % 5
pennies = (remainder3) // 1


print(f'quarters {quarters}, dimes {dimes}, nickels {nickels}, pennies {pennies}')
