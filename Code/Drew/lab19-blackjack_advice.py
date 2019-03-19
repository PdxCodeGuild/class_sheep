import random

# Read the number of points and gives advice, hit vs. stay
def advice_func(x):
    if x < 17:
        return 'I suggest you hit'
    elif 17 <= x < 21:
        return 'I suggest you stay'
    elif x == 21:
        return 'Blackjack!'
    elif x > 21:
        return 'Sorry, busted...'

# Check the cards against a dictionary and adds up the points
def check_points(hand):
    card_values = {'A': 1, 'B': 10, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10}
    points = 0
    for c in hand:
        points += card_values[c]
    return points

# Get a new card from the deck
def get_card():
    deck = ['Q', 'K', 'A']
    #deck = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    new_card = random.choice(deck)
    return new_card

# Define empty lists/variables
potential_list = []
user_hand = []
points = 0

# Two cards for first deal
user_hand.append(get_card())
user_hand.append(get_card())
potential_list.append(user_hand)

# Create separate list for aces
if 'A' in user_hand:
    temp_hand = user_hand[:]
    temp_hand.append('B')
    potential_list.append(temp_hand)
print(f"You have {potential_list[0]}.")
points = check_points(user_hand)
points = check_points(user_hand)
advice = advice_func(points)

while True:
    hit = input("(h)it or (s)tay?\n")
    if hit == 'h':
        new_card = get_card()
        print(f"You got a {new_card}.")
        for i in range(len(potential_list)):
            potential_list[i].append(new_card)
        if new_card == 'A':
            temp_hand = potential_list[-1][:]
            temp_hand.append('B')
            potential_list.append(temp_hand)
        print(user_hand)
        print(potential_list)
        advice = advice_func(points)
        print(advice)
        continue
    elif hit == 's':
        print(f"You ended up at {points}")
        break
    else:
        print("Try again")
