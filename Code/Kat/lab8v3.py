user_money = float(input("How much money do you have, written as a dollar amount (e.g. 10.45)? >"))
user_money = int(user_money * 100)
coins = [('quarter', 25), ('dime', 10), ('nickel', 5), ('penny', 1), ('sneakel', 50), ('quime', 35)]
def coin_amount(in_tuple):
    return in_tuple[1]
ordered_coins_list = sorted(coins, key=coin_amount, reverse=True)
change_dict = {}
print(ordered_coins_list)
for metal in ordered_coins_list:
    change_dict[metal[0]] = user_money // metal[1]
    print(f"You have {change_dict[metal[0]]} of {metal[0]}.")
    user_money = user_money % metal[1]
