#lab19.py
'''Blackjack Advisor'''

card_dict = {'A':11, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':10, 'Q':10, 'K':10}
Acard_dict = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':10, 'Q':10, 'K':10}

'''Calculates the total hand value'''
def card_calculator(in_list):
    card_total = 0
    for card in range(len(in_list)):
        card_type = in_list[card]
        card_total +=  card_dict[card_type]
    return card_total

'''Calculates the total hand value (Aces worth 1 in this version)'''
def ace_calculator(in_list):
    card_total = 0
    for card in range(len(in_list)):
        card_type = in_list[card]
        card_total +=  Acard_dict[card_type]
    return card_total

'''Determines advice output based on total hand value'''
def advisor(in_num):
    if in_num > 21:
        advice = 'Already Busted'
    else:
        if in_num < 17:
            advice = "You should hit!"
        if in_num >= 17 and in_num < 21:
            advice = "Stay."
        if in_num == 21:
            advice = "Blackjack!"
    return advice

user_hand=[]
for card in range(0,3):
    user_card = input("Please pick a card, up to three.> ")
    user_hand.append(user_card)
print(user_hand)
total = card_calculator(user_hand)
if total > 21:
    total = ace_calculator(user_hand)
print(f"You have {total} points in your hand.")
tell_me = advisor(total)
print(tell_me)

# {Notes}
