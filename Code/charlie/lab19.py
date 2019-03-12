import random
card_dict = {'A': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9 , '10': 10, 'j':10, 'J': 10, 'q':10, 'Q':10,'k':10, 'K':10}

first_card = input("what's your first card?")
# while first_card not in card_dict.keys:
#     first_card = input("what's your first card? Pick a card between 2 and 10, J, Q, K, or ace")

second_card = input("what's your second card?")
# while second_card not in card_dict.keys:
#     second_card = input("what's your first card? Pick a card between 2 and 10, J, Q, K, or ace")

third_card = input("what's your third card?")
# while third_card not in card_dict.keys:
#     third_card = input("what's your first card? Pick a card between 2 and 10, J, Q, K, or ace")


sum_of_hand = card_dict[first_card] + card_dict[second_card] + card_dict[third_card]
print(sum_of_hand)
while first_card == 'A' or second_card == 'A' or third_card == 'A':
    Ace = 0
    if sum_of_hand - card_dict['A'] > 10:
        Ace == 1
        break
    elif sum_of_hand - card_dict['A'] <= 10:
        Ace == 11
        break

sum_of_hand = card_dict[first_card] + card_dict[second_card] + card_dict[third_card] - 11 + Ace


print(sum_of_hand)

if sum_of_hand < 17:
    print('Hit')
elif sum_of_hand >= 17 and sum_of_hand < 21:
    print('Stay')
elif sum_of_hand == 21:
    print('Blackjack!')
else:
    print('Already busted')
