#lab8
#Make Change
def highestex(in_tuple):
    return in_tuple[1]
while True:
    coinlist = []
    totalcoin = {}
    dollaramount = input("Please give me your total money in dollars (decimal): >")
    pennyamount = float(dollaramount)
    pennyamount = round(pennyamount * 100)
    while True:
        coin = input("Please give me the name of your coin, or type 'done' if finished: >")
        if coin.lower() == 'done':
            break
        else:
            coinval = input("Please give me the value of the coin in pennies: >")
            coinlist.append((str(coin), int(coinval)))
    for coin_tuple in sorted(coinlist, key=highestex, reverse=True):
        totalcoin[coin_tuple[0]] = pennyamount // coin_tuple[1]
        pennyamount -= ((coin_tuple[1]) * (pennyamount // coin_tuple[1]))
    print(f"You have {totalcoin}")
    cont = input("Type anything to calculate change again or type 'done' if finished. >")
    if cont.lower() == 'done':
        break
# coin1 = input("Give me the name of your first coin. >")
# coin1val = input("Give me its value. >")
# coin1val = int(coin1val)
# coin_dict = {coin1 : coin1val, 'dime' : 10, 'nickel' : 5, 'penny' : 1}
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
# coin1amount = pennyamount // coinlist[0][1]
# coin2amount = (pennyamount % coinlist[0][1]) // coinlist[1][1]
# coin3amount = ((pennyamount % coinlist[0][1]) % coinlist[1][1]) // coinlist[2][1]
# coin4amount = (((pennyamount % coinlist[0][1]) % coinlist[1][1]) % coinlist[2][1]) // coinlist[3][1]
# print(f"Your total change is {coin1amount} {coin1}, {coin2amount} {coin2}, {coin3amount} {coin3}, and {coin4amount} {coin4}.")
