import random

""" lab26-adventure.py imports this as a module """

def blackjack_game():
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

    # Choose the hand that is closest to 21 without being over
    def best_hand(hands):
        highest = 0
        best = 0
        for i in range(len(hands)):
            points = check_points(hands[i])
            if points <= 21 and points > highest:
                highest = points
                best = i
        return best

    # Get a new card from the deck
    def get_card():
        deck = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        new_card = random.choice(deck)
        return new_card

    # Define empty lists/variables
    user_list = []
    user_hand = []
    points = 0
    blackjack = False
    busted = False
    print()

    # Two cards for first deal
    user_hand.append(get_card())
    user_hand.append(get_card())
    user_list.append(user_hand)

    # If user gets an ace, user's hand will actually be a list of potential hands
    if 'A' in user_hand:
        temp_hand = user_hand[:]
        temp_hand.append('B')
        user_list.append(temp_hand)
    print(f"Your current hand is {user_list[0]}.")

    # Check if any hand = 21
    points = check_points(user_hand)
    if len(user_list) == 1:
        for hand in user_list:
            if check_points(hand) == 21:
                print("Blackjack!")
                print()
                blackjack = True
    # This is really only calculated separately to display ace options if no blackjack
    if len(user_list) > 1:
        for hand in user_list:
            if check_points(hand) == 21:
                print("Blackjack!")
                print()
                blackjack = True
        if blackjack == False:
            print("With aces being 1 or 11 points,")
            for hand in user_list:
                print(f"You could have {check_points(hand)} points.")
    else:
        print(f"You have {points} points.")

    # Computer opponent:
    comp_list = []
    comp_hand = []
    comp_hand.append(get_card())
    comp_hand.append(get_card())
    comp_list.append(comp_hand)
    if 'A' in comp_hand:
        temp_hand = comp_hand[:]
        temp_hand.append('B')
        comp_list.append(temp_hand)
    comp_points = check_points(comp_list[best_hand(comp_list)])
    # Computer will always take the advice to hit if points are under 17
    while comp_points < 17:
        comp_card = get_card()
        for i in range(len(comp_list)):
            comp_list[i].append(comp_card)
            comp_points = check_points(comp_list[best_hand(comp_list)])

    if blackjack == False:
        print(f"The computer's hand is ['{comp_hand[0]}', '?']")

    while blackjack == False:
        hit = input("(h)it or (s)tay?\n")
        # If user stays, break loop and print points of best hand
        if hit == 's':
            print()
            print(f"You ended up at {check_points(user_list[best_hand(user_list)])} points.")
            blackjack = True
            break
        # If user hits, add card, split deck for aces
        elif hit == 'h':
            print()
            new_card = get_card()
            print(f"You got a {new_card}.")
            for i in range(len(user_list)):
                user_list[i].append(new_card)
            if new_card == 'A':
                temp_hand = user_list[-1][:]
                temp_hand.append('B')
                user_list.append(temp_hand)
            # last_hand variable records the hand in case it's the last hand, and it busts and pops out of the list
            last_hand = user_list[0][:]
            last_points = check_points(user_list[0])
            # Pop busted hands
            user_list = pop_hands(user_list)
            # Print results based on number of hands in list
            # If there are no hands left in list, the player busted
            if len(user_list) < 1:
                print()
                print(f"Your current hand is {last_hand}.")
                print(f"That puts you at {last_points}.")
                print("Sorry, busted")
                busted = True
                return 'lose'
            # Check hand and print results
            if len(user_list) == 1:
                print()
                if check_points(user_list[0]) == 21:
                    blackjack = True
                    print(f"Your current hand is {user_list[0]}")
                    print("Blackjack!")
                    print()
                    return 'win'
                else:
                    print(f"Your current hand is {user_list[0]}")
                    print(f"You have {check_points(user_list[0])} points.")
            # If user has more than one hand, check which is closest to 21 and print results
            if len(user_list) > 1:
                print()
                for hand in user_list:
                    if check_points(hand) == 21:
                        print(f"Your current hand is {user_list[0]}")
                        print("Blackjack!")
                        print()
                        blackjack = True
                        return 'win'
                if blackjack == False:
                    print(f"Your current hand is {user_list[0]}")
                    print("With aces being 1 or 11 points,")
                    for hand in user_list:
                        print(f"You could have {check_points(hand)} points.")
                continue
        else:
            print()
            print("Try again")

    # This will run if user stays.
    if busted == False:
        print(f"The computer's hand is {comp_list[best_hand(comp_list)]}.")
        print(f"The computer has {check_points(comp_list[best_hand(comp_list)])} points.")
        if check_points(comp_list[best_hand(comp_list)]) > 21:
            return 'win'
        elif check_points(comp_list[best_hand(comp_list)]) == check_points(user_list[best_hand(user_list)]):
            return 'tie'
        elif check_points(comp_list[best_hand(comp_list)]) < check_points(user_list[best_hand(user_list)]):
            return 'win'
        elif check_points(comp_list[best_hand(comp_list)]) > check_points(user_list[best_hand(user_list)]):
            return 'lose'
