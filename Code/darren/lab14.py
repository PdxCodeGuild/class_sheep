#lab14.py
#pick6
import random

balance = 0
earnings = 0
expenses = 0
totalmatches = 0
userticket = []
# userticket = [8, 18, 28, 38, 48, 58]
onematches = 0
twomatches = 0
threematches = 0
fourmatches = 0
fivematches = 0
sixmatches = 0

def autochargetool(innum):
    #adjusts balance and expense total according to input number of tickets
    autolist = []
    auto1 = 0
    auto2 = 0
    for attempt in range(innum):
        auto1 += 2
        auto2 += 2
    autolist.append(auto1)
    autolist.append(auto2)
    return autolist

def randomtickettool():
    #creates random ticket with 6 numbers by default)
    randticket = []
    for num in range(6):
        randticket.append(random.randint(1,99))
    return randticket

totaltickets = int(input("Please enter number of tickets to purchase. >"))
for choice in range(6):
    userchoice = int(input("Please select a number between 1 and 99. >"))
    userticket.append(userchoice)
print(userticket)
autocharge = autochargetool(totaltickets)
balance -= autocharge[0]
expenses += autocharge[1]
for attempt in range(totaltickets):
    ticket = randomtickettool()
    ticketmatches = 0
    for index in range(6):
        if ticket[index] == userticket[index]:
            totalmatches += 1
            ticketmatches += 1
    if ticketmatches == 1:
        balance += 4
        onematches += 1
    if ticketmatches == 2:
        balance += 7
        twomatches += 1
    if ticketmatches == 3:
        balance += 100
        threematches += 1
    if ticketmatches == 4:
        balance += 50000
        fourmatches += 1
    if ticketmatches == 5:
        balance += 1000000
        fivematches += 1
    if ticketmatches == 6:
        balance += 25000000
        sixmatches += 1
earnings = balance - expenses
ROI = (earnings - expenses)/expenses
print(f"You had {totalmatches} total matches on your {totaltickets} tickets.")
print(f"{onematches} single matches.")
print(f"{twomatches} dual matches.")
print(f"{threematches} triple matches.")
print(f"{fourmatches} quadruple matches.")
print(f"{fivematches} quintuple matches.")
print(f"{sixmatches} sextuple matches.")
print(f"You spent {expenses} on tickets.")
print(f"You earned {earnings} from winnings.")
print(f"Your ending balance is ${balance}.")
print(f"Your ROI is {ROI}.")
