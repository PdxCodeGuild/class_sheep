#lab14.py
#pick6
import random
#                         123456
# For tomorrow: matches = [3, 1, 1, 0, 0, 1]
# index+1
# matches[2]+1

balance = 0
earnings = 0
expenses = 0
totalmatches = 0
userticket = []
# userticket = [8, 18, 28, 38, 48, 58]
matchdict = {0:0, 1:4, 2:7, 3:100, 4:50000, 5:1000000, 6:25000000}
#key = number of matches, value = amount to add to balance per 1 of key.

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

def matchtotaltool(innum):
    ticketmatches = 0
    for index in range(6):
        if ticket[index] == userticket[index]:
            ticketmatches += 1
    return ticketmatches

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
    ticketmatches = matchtotaltool(ticket)
    totalmatches += ticketmatches
    balance += matchdict[ticketmatches]
earnings = balance - expenses
ROI = (earnings - expenses)/expenses
print(f"You had {totalmatches} total matches on your {totaltickets} tickets.")
print(f"You spent {expenses} on tickets.")
print(f"You earned {earnings} from winnings.")
print(f"Your ending balance is ${balance}.")
print(f"Your ROI is {ROI}.")
