#lab8
#Make Change
while True:
    pennyamount = input("Please give me your total cash in cents: >")
    pennyamount = int(pennyamount)
    quarteramount = pennyamount // 25
    dimeamount = (pennyamount % 25) // 10
    nickelamount = ((pennyamount % 25) % 10) // 5
    leftover = ((pennyamount % 25) % 10) % 5
    print(f"Your total change is {quarteramount} quarters, {dimeamount} dimes, {nickelamount} nickels, and {leftover} pennies.")
    cont = input("Type anything to calculate change again or type 'done' if finished. >")
    if cont.lower() == 'done':
        break
