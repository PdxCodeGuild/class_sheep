import random

card_values = {'A': 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10, 'J': 10, 'Q': 10, 'K': 10}
user_cards = []
points = 0

def blackjack(l):
    points = 0
    for i in l:
        points += card_values[i]
    return points

def advice_func(x):
    if x < 17:
        return 'I suggest you hit'
    elif 17 <= x < 21:
        return 'I suggest you stay'
    elif x == 21:
        return 'Blackjack!'
    elif x > 21:
        return 'Sorry, busted...'

while points <= 21:
    hit = input("(h)it or (s)tay?\n")
    if hit == 'h':
        new_card = random.choice(list(card_values))
        user_cards.append(new_card)
        points = blackjack(user_cards)
        print(f"You got a {new_card}")
        advice = advice_func(points)
        print(advice)
        continue
    elif hit == 's':
        print(f"You ended up at {points}")
        break
