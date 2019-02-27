#lab8
#Make Change
while True:
    dollaramount = input("Please give me your total money in dollars (decimal): >")
    pennyamount = float(dollaramount)
    pennyamount = round(pennyamount * 100)
    coin1 = input("Please give me the name of your first coin: >")
    coin1value = input("Please give me the value of your first coin in pennies: >")
    coin1value = int(coin1value)
    coin2 = input("Please give me the name of your second coin: >")
    coin2value = input("Please give me the value of your second coin in pennies: >")
    coin2value = int(coin2value)
    coin3 = input("Please give me the name of your third coin: >")
    coin3value = input("Please give me the value of your third coin in pennies: >")
    coin3value = int(coin3value)
    coin4 = input("Please give me the name of your fourth coin: >")
    coin4value = input("Please give me the value of your fourth coin in pennies: >")
    coin4value = int(coin4value)
    coin_dict = {coin1 : coin1value, coin2 : coin2value, coin3 : coin3value, coin4 : coin4value}
    coin1amount = pennyamount // coin1value
    coin2amount = (pennyamount % coin1value) // coin2value
    coin3amount = ((pennyamount % coin1value) % coin2value) // coin3value
    coin4amount = (((pennyamount % coin1value) % coin2value) % coin3value) // coin4value
    print(f"Your total change is {coin1amount} {coin1}, {coin2amount} {coin2}, {coin3amount} {coin3}, and {coin4amount} {coin4}.")
    cont = input("Type anything to calculate change again or type 'done' if finished. >")
    if cont.lower() == 'done':
        break
# coin1 = input("Give me the name of your first coin. >")
# coin1value = input("Give me its value. >")
# coin1value = int(coin1value)
# coin_dict = {coin1 : coin1value, 'dime' : 10, 'nickel' : 5, 'penny' : 1}
# print(f"Your first coin is {coin1} and its value is {coin_dict[coin1]}.")
# #lab8
# #Make Change
# while True:
#     pennyamount = input("Please give me your total cash in cents: >")
#     pennyamount = int(pennyamount)
#     quarteramount = pennyamount // 25
#     dimeamount = (pennyamount % 25) // 10
#     nickelamount = ((pennyamount % 25) % 10) // 5
#     leftover = ((pennyamount % 25) % 10) % 5
#     print(f"Your total change is {quarteramount} quarters, {dimeamount} dimes, {nickelamount} nickels, and {leftover} pennies.")
#     cont = input("Type anything to calculate change again or type 'done' if finished. >")
#     if cont.lower() == 'done':
#         break
