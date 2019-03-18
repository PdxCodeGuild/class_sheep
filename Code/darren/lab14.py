#lab14.py
#pick6
import random

balance = 0
earnings = 0
expenses = 0
total_matches = 0
user_ticket = []
# user_ticket = [8, 18, 28, 38, 48, 58]
match_dict = {0:0, 1:4, 2:7, 3:100, 4:50000, 5:1000000, 6:25000000}
match_count_dict = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
#key = number of matches, value = amount to add to balance per 1 of key.

def auto_charge(in_num):
    #adjusts balance and expense total according to input number of tickets
    expenses = 0
    for attempt in range(in_num):
        expenses += 2
    return expenses

def random_ticket():
    #creates random ticket with 6 numbers by default)
    rand_ticket = []
    for num in range(6):
        rand_ticket.append(random.randint(1,99))
    return rand_ticket

def match_total(in_num):
    #counts total number of matches per ticket
    ticket_matches = 0
    for index in range(6):
        if in_num[index] == user_ticket[index]:
            ticket_matches += 1
    return ticket_matches

# def matchcountertool(in_num):
#     #categorizes frequency of specific match numbers
#     updaterdict = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
#     updaterdict[in_num] += 1
#     return updaterdict

total_tickets = int(input("Please enter number of tickets to purchase. >"))
for choice in range(6):
    user_choice = int(input("Please select a number between 1 and 99. >"))
    user_ticket.append(user_choice)
print(user_ticket)
expenses = auto_charge(total_tickets)
balance -= expenses
for attempt in range(total_tickets):
    ticket = random_ticket()
    ticket_matches = match_total(ticket)
    total_matches += ticket_matches
    balance += match_dict[ticket_matches]
    match_count_dict[ticket_matches] += 1
earnings = balance - expenses
ROI = (earnings - expenses)/expenses
print(f"You had {total_matches} total matches on your {total_tickets} tickets.")
print(f"You spent {expenses} on tickets.")
print(f"You earned {earnings} from winnings.")
print(f"Your ending balance is ${balance}.")
print(f"Your ROI is {ROI}.")
print(f"These are your total of matches: {match_count_dict}.")

#notes
#                         123456
# For tomorrow: matches = [3, 1, 1, 0, 0, 1]
# index+1
# matches[2]+1
