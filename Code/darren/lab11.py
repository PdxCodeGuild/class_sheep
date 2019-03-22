#lab11.py
'''Simple Calculator'''

'''Normal Version'''
while True:
    val1 = input("Enter first integer: >")
    val2 = input("Enter second integer: >")
    proc = input("Enter equation symbol (+ - / *): >")
    if proc == '+':
        result = (float(val1)) + (float(val2))
        print(f"{val1} + {val2} = {result}")
    if proc == '-':
        result = (float(val1)) - (float(val2))
        print(f"{val1} - {val2} = {result}")
    if proc == '/':
        result = (float(val1)) / (float(val2))
        print(f"{val1} / {val2} = {result}")
    if proc == '*':
        result = (float(val1)) * (float(val2))
        print(f"{val1} * {val2} = {result}")
    cont = input("Enter anything to solve another equation or 'done' to quit. >")
    if cont.lower() == 'done':
        break

# '''Eval Version'''
# while True:
#     equ = input("Enter your equation to solve here: >")
#     result = eval(equ)
#     print(f"{equ} is {result}.")
#     cont = input("Enter anything to solve another equation or 'done' to quit. >")
#     if cont.lower() == 'done':
#         break
