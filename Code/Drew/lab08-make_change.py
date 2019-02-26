coins = [
    ('quarter', 25),
    ('dime', 10),
    ('nickel', 5),
    ('penny', 1)
]
coins = dict(coins)
wallet = input('Enter an amount in dollars:\n$')
wallet = int(wallet)
quarters = wallet // coins['quarter']
print(str(quarters)+' quarters')
wallet %= coins['quarter']
dimes = wallet // coins['dime']
print(str(dimes)+' dimes')
wallet %= coins['dime']
nickels = wallet // coins['nickel']
print(str(nickels)+' nickels')
wallet %= coins['nickel']
pennies = wallet // coins['penny']
print(str(pennies)+' pennies')
wallet %= coins['penny']
