#Lab 07-Rock, Paper, Scissors

# version 1=====================================================================

import random
choice = ['rock', 'paper', 'scissors']
computer_choice = random.choice(choice)
user_choice = input("Rock, paper or scissors?").lower()

if user_choice == computer_choice:
    print("Tie!")
elif computer_choice == 'rock':
    if user_choice == 'scissors':
        print('Computer wins!')
    else:
        print("You win!")
elif computer_choice =='paper':
    if user_choice == 'rock':
        print("Computer wins!")
    else:
        print("You win!")
elif computer_choice == 'scissors':
    if user_choice == 'paper':
        print("Computer wins!")
    else:
        print("You win!")


# version 2====================================================================
#
# import random
# choice = ['rock', 'paper', 'scissors']
# computer_choice = random.choice(choice)
#
# while True:
#     continue_playing = input("Would you like to play? yes or no: ")
#     if continue_playing == "no":
#         break
#
#     user_choice = input('pick rock, paper, or scissors? ').lower()
#
#     if user_choice == computer_choice:
#         print("Tie!")
#
#     elif computer_choice == 'rock':
#         if user_choice == 'scissors':
#             print('Computer wins!')
#         else:
#             print("You win!")
#
#     elif computer_choice =='paper':
#         if user_choice == 'rock':
#             print("Computer wins!")
#         else:
#             print("You win!")
#
#     elif computer_choice == 'scissors':
#         if user_choice == 'paper':
#             print("Computer wins!")
#         else:
#             print("You win!")
#
#     if continue_playing == "yes":
#         continue
