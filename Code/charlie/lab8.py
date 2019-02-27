# change = dict['quarters': 25,'dimes': 10, 'nickels': 5, 'pennies': 1]



user_change = float(input("how much change do you have?"))
total_pennies = round((user_change * 100.00))
print(total_pennies)

quarters = (total_pennies) // 25
remainder = total_pennies % 25
dimes = (remainder) // 10
remainder2 = remainder % 10
nickels = (remainder2) // 5
remainder3 = remainder2 % 5
pennies = (remainder3) // 1


print(f'quarters {quarters}, dimes {dimes}, nickels {nickels}, pennies {pennies}')
#
# dimes= remainder % 10
# remainder2 = user_change -
