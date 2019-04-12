#lab7.py
'''Rock Paper Scissors Lizard Spock'''

import random

rps_list = ['rock','paper','scissors', 'lizard', 'spock']
while True:
    user_hand = input("I challenge you to Rock, Paper, Scissors... Lizard, Spock! Go! >")
    user_hand = user_hand.lower()
    compy_hand = random.choice(rps_list)
    rps_dict = {
        'rock': ['rock', 'lizard', 'scissors', 'paper', 'spock'],
        'paper': ['paper', 'rock', 'spock' , 'rock', 'lizard'],
        'scissors':['scissors', 'paper', 'lizard', 'rock', 'spock'],
        'lizard':['lizard', 'paper', 'spock', 'scissors', 'rock'],
        'spock':['spock', 'rock', 'scissors', 'lizard', 'paper']}
    if user_hand not in rps_list:
        print("That's not a real hand! Cheater!")
    if compy_hand == rps_dict[user_hand][0]:
        print(compy_hand)
        print('A tie?')
    if compy_hand == rps_dict[user_hand][1]:
        print(compy_hand)
        print('You win...')
    if compy_hand == rps_dict[user_hand][2]:
        print(compy_hand)
        print('You win...')
    if compy_hand == rps_dict[user_hand][3]:
        print(compy_hand)
        print('I win!')
    if compy_hand == rps_dict[user_hand][4]:
        print(compy_hand)
        print('I win!')
    cont = input("Want to play again? >")
    if cont.lower() != 'yes':
        break

# {Notes}
# import random
# rps_list = ['rock','paper','scissors', 'lizard', 'spock']
# while True:
#     user_hand = ''
#     compy_hand = ''
#     user_hand = input("I challenge you to Rock, Paper, Scissors... Lizard, Spock! Go! >")
#     compy_hand = random.choice(rps_list)
#     if user_hand.lower() not in rps_list:
#         print("That's not a real hand! Cheater!")
#     if user_hand.lower() == 'rock':
#         if compy_hand == 'paper':
#             print("Paper covers rock.")
#             print("I win!")
#         if compy_hand == 'spock':
#             print("Spock vaporizes rock.")
#             print("I win!")
#         if compy_hand == 'scissors':
#             print("Rock crushes scissors.")
#             print("You win...")
#         if compy_hand == 'lizard':
#             print("Rock smashes lizard")
#             print("You win...")
#     if user_hand.lower() == 'paper':
#         if compy_hand == 'scissors':
#             print("Scissors cut paper.")
#             print("I win!")
#         if compy_hand == 'lizard':
#             print("Lizard eats paper.")
#             print("I win!")
#         if compy_hand == 'rock':
#             print("Paper covers rock.")
#             print("You win...")
#         if compy_hand == 'spock':
#             print("Paper disproves Spock.")
#             print("You win...")
#     if user_hand.lower() == 'scissors':
#         if compy_hand == 'rock':
#             print("Rock crushes scissors.")
#             print("I win!")
#         if compy_hand == 'spock':
#             print("Spock smashes scissors.")
#             print("I win!")
#         if compy_hand == 'paper':
#             print("Scissors cut paper.")
#             print("You win...")
#         if compy_hand == 'lizard':
#             print("Scissors decapitate lizard.")
#             print("You win...")
#     if user_hand.lower() == 'lizard':
#         if compy_hand == 'rock':
#             print("Rock smashes lizard.")
#             print("I win!")
#         if compy_hand == 'scissors':
#             print("Scissors decapitate lizard.")
#             print("I win!")
#         if compy_hand == 'paper':
#             print("Lizard eats paper.")
#             print("You win...")
#         if compy_hand == 'spock':
#             print("Lizard poisons Spock.")
#             print("You win...")
#     if user_hand.lower() == 'spock':
#         if compy_hand == 'lizard':
#             print("Lizard poisons Spock.")
#             print("I win!")
#         if compy_hand == 'paper':
#             print("Paper disproves Spock.")
#             print("I win!")
#         if compy_hand == 'rock':
#             print("Spock vaporizes rock.")
#             print("You win...")
#         if compy_hand == 'scissors':
#             print("Spock smashes scissors.")
#             print("You win...")
#     if user_hand.lower() == compy_hand:
#         print(compy_hand)
#         print("A tie?")
#     cont = input("Want to play again? >")
#     if cont.lower() != 'yes':
#         break
