card1 = input("What is your first card? ")
card2 = input("What is your second card? ")
card3 = input("What is your third card? ")

def card_value(card):
    if card == "A":
        return 1
    if card == 'J' or card == 'Q' or card == 'K':
        return 10
    return int(card)

total = card_value(card1) + card_value(card2) + card_value(card3)

if card1 == "A" and total <= 11:
    total += 10
if card2 == "A" and total <= 11:
    total += 10
if card3 == "A" and total <= 11:
    total += 10

if total < 17:
    print (f"{total}. Hit!")
elif 17 <= total <= 20:
    print (f"{total}. Stay!")
elif total == 21:
    print (f"{total}. Blackjack!")
elif total > 21:
    print (f"{total}. Already busted!")
