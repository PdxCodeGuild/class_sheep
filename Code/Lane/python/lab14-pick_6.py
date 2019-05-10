# Lab 14: Pick 6

# version 1 & 2 ===============================================================

import random
winning_ticket = []

#generate 6 random numbers between 1 and 99 that represent the winning numbers
for num in range(6):
    winning_ticket.append(random.randint(1, 99))

print('The winning numbers were:', winning_ticket)

#starting & earnings balance = $0
expenses = 0
earnings = 0

# "buy" 100,000 tickets
for num in range(100000):
    wins = 0 #start with zero wins
    one_ticket = []
    for num in range(6): # pick 6 random numbers for each 100k tickets bought
        one_ticket.append(random.randint(1, 99))

    expenses = expenses - 2 #each ticket costs $2, so the balance goes down $2 with each ticket bough
    for index in range(6):
        if winning_ticket[index] == one_ticket[index]:
            wins += 1  #if the ticket has a match to the winning numbers, the counter goes up by 1 for each match
    if wins > 0: #calculates the earnings based on the number of wins
        winning_values = [0, 4, 7, 100, 50000, 1000000, 25000000]
        earnings += winning_values[wins]
        #print(earnings) (use this line if you want to see the earning tally up 100k times)

#the more matches/wins, the more money you make. 0 matches = $2 (cost of ticket), 1 match = $4, 2 matches = $7, 3 matches = $100, 4 matches = $50k, 5 matches = $1m, 6 matches = $25m

print("Your total earnings =",earnings)
print("Your total expenses =",expenses)
print("Your total balance =",expenses + earnings)
print("The Return on Investment =",((earnings - expenses)/expenses))
