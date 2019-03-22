#lab8.py
'''Make Change'''

'''Gives second index value in tuple'''
def highest_ex(in_tuple):
    return in_tuple[1]

while True:
    coin_list = []
    total_coin = {}
    dollar_aount = input("Please give me your total money in dollars (decimal): >")
    penny_amount = float(dollar_aount)
    penny_amount = round(penny_amount * 100)
    while True:
        coin = input("Please give me the name of your coin, or type 'done' if finished: >")
        if coin.lower() == 'done':
            break
        coin_val = input("Please give me the value of the coin in pennies: >")
        coin_tuple = (coin, int(coin_val))
        coin_list.append(coin_tuple)
    for item in sorted(coin_list, key=highest_ex, reverse=True):
        total_coin[item[0]] = penny_amount // item[1]
        penny_amount -= ((item[1]) * (penny_amount // item[1]))
    print(f"You have {total_coin}")
    cont = input("Type anything to calculate change again or type 'done' if finished. >")
    if cont.lower() == 'done':
        break

# {Notes}

# coin1 = input("Give me the name of your first coin. >")
# coin1_val = input("Give me its value. >")
# coin1_val = int(coin1_val)
# coin_dict = {coin1 : coin1_val, 'dime' : 10, 'nickel' : 5, 'penny' : 1}
# print(f"Your first coin is {coin1} and its value is {coin_dict[coin1]}.")
# #lab8
# #Make Change
# while True:
#     penny_amount = input("Please give me your total cash in cents: >")
#     penny_amount = int(penny_amount)
#     quarter_amount = penny_amount // 25
#     dime_amount = (penny_amount % 25) // 10
#     nickel_amount = ((penny_amount % 25) % 10) // 5
#     left_over = ((penny_amount % 25) % 10) % 5
#     print(f"Your total change is {quarter_amount} quarters, {dime_amount} dimes, {nickel_amount} nickels, and {left_over} pennies.")
#     cont = input("Type anything to calculate change again or type 'done' if finished. >")
#     if cont.lower() == 'done':
#         break
# coin1amount = penny_amount // coin_list[0][1]
# coin2amount = (penny_amount % coin_list[0][1]) // coin_list[1][1]
# coin3amount = ((penny_amount % coin_list[0][1]) % coin_list[1][1]) // coin_list[2][1]
# coin4amount = (((penny_amount % coin_list[0][1]) % coin_list[1][1]) % coin_list[2][1]) // coin_list[3][1]
# print(f"Your total change is {coin1amount} {coin1}, {coin2amount} {coin2}, {coin3amount} {coin3}, and {coin4amount} {coin4}.")
