import random

# Dictionary of card values.
card_values = {'A': 1, 'B': 10, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10}

# Check the cards against that dictionary and add up the points
def check_points(hand):
    points = 0
    for card in hand:
        points += card_values[card]
    return points

# If any hand goes over 21 points, pop that hand from list of hands
def pop_hands(hands):
    for i in range(len(hands)):
        points = check_points(hands[i])
        if points > 21:
            hands.pop(i)
    return hands

# Choose the hand that is closest to 21
def best_hand(hands):
    highest = 0
    for i in range(len(hands)):
        points = check_points(hands[i])
        if points < 21 and points > highest:
            highest = points
            best = i
    return best

# Get advice based on points
def advice_func(points):
    if points < 17:
        advice = "you should hit"
    if points >= 17:
        advice = "you should stay"
    return advice

# Get a new card from the deck
def get_card():
    deck = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    new_card = random.choice(deck)
    return new_card

# Define empty lists/variables
potential_list = []
user_hand = []
points = 0
blackjack = False

# Two cards for first deal
user_hand.append(get_card())
user_hand.append(get_card())
potential_list.append(user_hand)

# Create separate list for aces
if 'A' in user_hand:
    temp_hand = user_hand[:]
    temp_hand.append('B')
    potential_list.append(temp_hand)
print(f"Your current hand is {potential_list[0]}.")

# Check if any hand = 21
points = check_points(user_hand)
if len(potential_list) == 1:
    for hand in potential_list:
        if check_points(hand) == 21:
            print("Blackjack!")
            blackjack = True
if len(potential_list) > 1:
    for hand in potential_list:
        if check_points(hand) == 21:
            print("Blackjack!")
            blackjack = True
    if blackjack == False:
        print("With aces being 1 or 11 points,")
        for hand in potential_list:
            print(f"You could have {check_points(hand)} points. ({advice_func(check_points(hand))})")
else:
    print(f"You have {points} points. ({advice_func(check_points(user_hand))})")

while blackjack == False:
    hit = input("(h)it or (s)tay?\n")
    if hit == 's':
        print()
        print(f"You ended up at {check_points(potential_list[best_hand(potential_list)])} points.")
        blackjack = True
        break
    elif hit == 'h':
        print()
        new_card = get_card()
        print(f"You got a {new_card}.")
        for i in range(len(potential_list)):
            potential_list[i].append(new_card)
        if new_card == 'A':
            temp_hand = potential_list[-1][:]
            temp_hand.append('B')
            potential_list.append(temp_hand)
        potential_list = pop_hands(potential_list)
        if len(potential_list) < 1:
            print("Sorry, busted")
            break
        if len(potential_list) == 1:
            if check_points(potential_list[0]) == 21:
                blackjack = True
                print("Blackjack!")
                break
            else:
                print(f"Your current hand is {potential_list[0]}")
                print(f"You have {check_points(potential_list[0])} points. ({advice_func(check_points(user_hand))})")
        if len(potential_list) > 1:
            for hand in potential_list:
                if check_points(hand) == 21:
                    print("Blackjack!")
                    blackjack = True
                    break
            if blackjack == False:
                print(f"Your current hand is {potential_list[0]}")
                print("With aces being 1 or 11 points,")
                for hand in potential_list:
                    print(f"You could have {check_points(hand)} points. (in which case {advice_func(check_points(hand))})")
            continue
    else:
        print()
        print("Try again")
