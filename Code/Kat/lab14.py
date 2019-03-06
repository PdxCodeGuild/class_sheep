import random

def pick6():
    ticket = []
    for item in range(6):
        ticket.append(random.randint(1, 99))
    return ticket

def payout(winning_ticket, new_ticket):
    matches = 0
    for selection in range(0, 6):
        if winning_ticket[selection] == new_ticket[selection]:
            matches += 1
    possible_winnings = [0, 4, 7, 100, 50000, 1000000, 25000000]
    winnings = possible_winnings[matches]
    return winnings

def calculation():
    balance = 0
    total_matches = 0
    winning_ticket = pick6()
    for tickets in range(0, 100000):
        new_ticket = pick6()
        balance -= 2
        balance += payout(winning_ticket, new_ticket)
    return balance

print(calculation())
