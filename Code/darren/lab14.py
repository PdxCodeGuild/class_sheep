#lab14.py
#pick6
import random
def matchchecker(innum):
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
balance = 0
totalmatches = 0
userticket = []
# userticket = [8, 18, 28, 38, 48, 58]
onematches = 0
twomatches = 0
threematches = 0
fourmatches = 0
fivematches = 0
sixmatches = 0
for innum in range(6):
    userchoice = int(input("Please select a number between 1 and 99. >"))
    userticket.append(userchoice)
print(userticket)
for attempt in range(100000):
    balance -= 2
    ticket = []
    ticketmatches = 0
    for num in range(6):
        ticket.append(random.randint(1,99))
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
print(f"You had {totalmatches} total matches on your 100,000 tickets.")
print(f"{onematches} single matches.")
print(f"{twomatches} dual matches.")
print(f"{threematches} triple matches.")
print(f"{fourmatches} quadruple matches.")
print(f"{fivematches} quintuple matches.")
print(f"{sixmatches} sextuple matches.")
print(f"Your ending balance is ${balance}.")
