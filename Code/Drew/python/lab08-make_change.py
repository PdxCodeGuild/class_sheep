coins = [
    ('quarter', 25),
    ('dime', 10),
    ('nickel', 5),
    ('penny', 1)
]
coins = dict(coins)
wallet = float(input('Enter an amount in dollars:\n$'))
wallet = float(wallet * 100)
quarters = wallet // coins['quarter']
print(str(int(quarters))+' quarters')
wallet %= coins['quarter']
dimes = wallet // coins['dime']
print(str(int(dimes))+' dimes')
wallet %= coins['dime']
nickels = wallet // coins['nickel']
print(str(int(nickels))+' nickels')
wallet %= coins['nickel']
pennies = wallet // coins['penny']
print(str(int(pennies))+' pennies')
wallet %= coins['penny']
