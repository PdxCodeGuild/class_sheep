# Lab 14: Pick6
# Have the computer play pick6 many times and determine net balance.
# Initially the program will pick 6 random numbers as the 'winner'. Then try playing pick6 100,000 times, with the ticket cost and payoff below.
# A ticket contains 6 numbers, 1 to 99, and the number of matches between the ticket and the winning numbers determines the payoff. Order matters, if the winning numbers are [5, 10] and your ticket numbers are [10, 5] you have 0 matches. If the winning numbers are [5, 10, 2] and your ticket numbers are [10, 5, 2], you have 1 match. Calculate your net winnings (the sum of all expenses and earnings).
# a ticket costs $2
# if 1 number matches, you win $4
# if 2 numbers match, you win $7
# if 3 numbers match, you win $100
# if 4 numbers match, you win $50,000
# if 5 numbers match, you win $1,000,000
# if 6 numbers match, you win $25,000,000
#
# Steps
# 1. Generate a list of 6 random numbers representing the winning tickets
# 2. Start your balance at 0
# 3. Loop 100,000 times, for each loop:
# 4. Generate a list of 6 random numbers representing the ticket
# 5. Subtract 2 from your balance (you bought a ticket)
# 6. Find how many numbers match
# 7. Add to your balance the winnings from your matches
# 8. After the loop, print the final balance


import random

# function to generate six random numbers
def pick6():
    ticket = []
    for item in range(6):
        ticket.append(random.randint(1, 99))
    return ticket

# function to compare tickets and assess number of matches and subsequent winnings
def payout(winning_ticket, new_ticket):
    matches = 0
    for selection in range(0, 6):
        if winning_ticket[selection] == new_ticket[selection]:
            matches += 1
    #possible winnings were provided in the instructions
    possible_winnings = [0, 4, 7, 100, 50000, 1000000, 25000000]
    winnings = possible_winnings[matches]
    return winnings

#function to combine cost and expeditures and determine player balance taking into account ticket price and winnings
def calculation():
    balance = 0
    total_matches = 0
    winning_ticket = pick6()
    for tickets in range(0, 100000):
        new_ticket = pick6()
        balance -= 2
        balance += payout(winning_ticket, new_ticket)
    return balance

print(f"You spent $200000 and won ${200000 + calculation()} for a net loss of ${abs(calculation())}.")
