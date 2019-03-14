# 1.Create a deck with 13 cards (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K)
# 2.Assign numerical values to each card (Ace = 1, face = 10)
# 3.Ask the user to enter their first, second, and third card
# 4.Add up the three cards
# 5.Based on the total of the cards give advise:
    #Less than 17, advise to "Hit"
    #Greater than or equal to 17, but less than 21, advise to "Stay"
    #Exactly 21, advise "Blackjack!"
    #Over 21, advise "Already Busted"


#version 1
cards = {'ace': 1, '2': 2, 'two': 2, '3': 3, 'three': 3, '4': 4, 'four': 4, '5': 5, 'five': 5, '6': 6, 'six': 6, '7': 7, 'seven': 7, '8': 8, 'eight': 8, '9': 9, 'nine': 9, 'jack': 10, 'queen': 10, 'king': 10}

card1 = input("What is your first card? ")
card2 = input("What is your second card? ")
card3 = input("What is your third card? ")

card_total = cards[card1] + cards[card2] + cards[card3]
print(card_total)

if card_total >= 17 and card_total <21:
    print('Stay')
elif card_total < 17:
    print('Hit')
elif card_total == 21:
    print('Blackjack!')
elif card_total > 21:
    print('Busted!')
