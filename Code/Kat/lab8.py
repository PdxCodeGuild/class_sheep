# Lab 8: Make Change
# INSTRUCTIONS: Let's convert a dollar amount into a number of coins. The input will be the total amount, the output will be the number of quarters, dimes, nickles, and pennies. Always break the total into the highest coin value first, resulting in the fewest amount of coins. For this, you'll have to use floor division //, which throws away the remainder. 10/3 is 3.333333, 10//3 is 3.

# Version 2
# Have the user enter a dollar amount (1.36), convert this to the total in pennies.

# Get user input
# user_money = float(input("How much money do you have, written as a dollar amount (e.g. 10.45)? >"))
# Convert to pennies
# user_money = int(user_money * 100)
#Determine how many of each coin there is using floor division, then check the remainder for the coin next highest in value. The leftovers are pennies.
# user_quarters = user_money // 25
# user_money = user_money % 25
# user_dimes = user_money // 10
# user_money = user_money % 10
# user_nickles = user_money // 5
# user_money = user_money % 5
# user_pennies = user_money // 1
# print(f"You have {user_quarters} quarters, {user_dimes} dimes, {user_nickles} nickles, and {user_pennies} pennies.")

# Version 3 (optional)
# Instead of hard-coding the coins, store them in a list. This way you can make custom coins.


# Sort by value
coins = [('quarter', 25), ('dime', 10), ('nickel', 5), ('penny', 1), ('sneakel', 50), ('quime', 35)]
def coin_amount(in_tuple):
    return in_tuple[1]
coins = sorted(coins, key=coin_amount, reverse=True)
def coin_count(user_money):
    coin_list = []
    for coin in coins:
        for i in range(len(coins)):
        user_money = user_money // coins[i][1]
        coin_list.append((coins[i][0], user_money))
    return coin_list
user_money = float(input("How much money do you have, written as a dollar amount (e.g. 10.45)? >"))
user_money = int(user_money * 100)
print(coin_count(user_money))
