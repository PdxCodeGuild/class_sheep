#Lab 19: Blackjack Advice

#INSTRUCTIONS
# Let's write a python program to give basic blackjack playing advice during a game by asking the player for cards. First, ask the user for three playing cards (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K). Then, figure out the point value of each card individually. Number cards are worth their number, all face cards are worth 10. At this point, assume aces are worth 1. Use the following rules to determine the advice:
#
# - Less than 17, advise to 'Hit'
# - Greater than or equal to 17, but less than 21, advise to "Stay"
# - Exactly 21, advise "Blackjack!"
# - Over 21, advise "Already Busted

# Print out the current total point value and the advice.

#get user's cards
card1 = input('What is your first card? ')
card2 = input('What is your second card? ')
card3 = input('What is your third card? ')

#function for assigning value to cards
def card_value(card):
    if card == 'A':
        return 1
    if card == 'J' or card == 'Q' or card == 'K':
        return 10
    return int(card)

total = card_value(card1) + card_value(card2) + card_value(card3)

#Version 2:
#INSTRUCTIONS Aces can be worth 11 if they won't put the total point value of both cards over 21. Remember that you can have multiple aces in a hand. Try generating a list of all possible hand values by doubling the number of values in the output whenever you encounter an ace. For one half, add 1, for the other, add 11. This ensures if you have multiple aces that you account for the full range of possible values.

if card1 == 'A' and total <= 11:
    total += 10
if card2 == 'A' and total <= 11:
    total += 10
if card3 == 'A' and total <= 11:
    total += 10

#Print values and advice
if total < 17:
    print (f'{total}. Hit!')
elif 17 <= total <= 20:
    print (f'{total}. Stay!')
elif total == 21:
    print (f'{total}. Blackjack!')
elif total > 21:
    print (f'{total}. Already busted!')
