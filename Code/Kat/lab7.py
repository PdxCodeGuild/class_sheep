# Lab 7: Rock Paper Scissors
# Let's play rock-paper-scissors with the computer.
# 1. The computer will ask the user for their choice (rock, paper, scissors)
# 2. The computer will randomly choose rock, paper or scissors
# 3. Determine who won and tell the user

import random

# Basic version
choice_list = ['rock', 'paper', 'scissors']
# get user input
user_choice = input(f"Which would you like, {choice_list[0]} or {choice_list[1]} or {choice_list[2]}?")
# catch bad entries
while user_choice not in choice_list:
    user_choice = [f"Which would you like, {choice_list[0]} or {choice_list[1]} or {choice_list[2]}?"]
computer_play = random.choice(choice_list)
print(f"I choose {computer_play}.")
if computer_play == choice_list:
    print("Tie!")
elif user_choice == 'rock':
    if computer_play == 'paper':
        print("Paper wins!")
    else:
        print("Rock wins!")
elif user_choice == 'scissors':
    if computer_play == 'paper':
        print("Scissors wins!")
    else:
        print("Rock wins!")
elif user_choice == 'paper':
    if computer_play == 'rock':
        print("Paper wins!")
    else:
        print("Scissors wins!")


# Dictionary version
# create dictionary entries with keys[beats key, loses to key]
rps_dict = {'rock': ['paper', 'scissors'], 'paper': ['scissors', 'rock'], 'scissors': ['rock', 'paper']}
# get user input
user_choice = input("Rock, paper, or scissors? > ").lower()
# randomly select computer play
computer_choice = random.choice(list(rps_dict))
if user_choice == computer_choice:
    print(f'The computer chose {computer_choice}. Tie!')
if computer_choice == rps_dict[user_choice][0]:
    print(f'The computer chose {computer_choice}. You lose!')
if computer_choice == rps_dict[user_choice][1]:
    print(f'The computer chose {computer_choice}. You win!')


# Function version with dictionary
def rock_paper_scissors(user_choice):
    rps_dict = {'rock': ['paper', 'scissors'], 'paper': ['scissors', 'rock'], 'scissors': ['rock', 'paper']}
    # randomly select computer play
    comp_choice = random.choice(list(rps_dict))
    if user_choice == comp_choice:
        return f'The computer chose {comp_choice}. You tie!'
    if comp_choice == rps_dict[user_choice][0]:
        return f'The computer chose {comp_choice}. You lose!'
    if comp_choice == rps_dict[user_choice][1]:
        return f'The computer chose {comp_choice}. You win!'
# get user input
user_choice = input("Rock, paper, or scissors? > ").lower()
print(rock_paper_scissors(user_choice))


# Version 3: Rock, paper, scissors, lizard, Spock!
move_list = ['rock', 'paper', 'scissors', 'lizard', 'spock']
# get user input
selection_list = input(f"Would you like to play {move_list[0]}, {move_list[1]}, {move_list[2]}, {move_list[3]}, or {move_list[4]} >")
# catch bad entries
while selection_list not in move_list:
    selection_list = [f"Which would you like, {move_list[0]}, {move_list[1]}, {move_list[2]}, {move_list[3]}, or {move_list[4]}?"]
# randomly select computer play
my_move = random.choice(move_list)
print(f"I chose {my_move}.")
if my_move == selection_list:
    print("Tie!")
elif selection_list == 'rock':
    if my_move == 'paper':
        print("Paper wins!")
    elif my_move == 'spock':
        print("Spock wins!")
    else:
        print("Rock wins!")
elif selection_list == 'scissors':
    if my_move == 'spock':
        print("Spock wins!")
    elif my_move == 'rock':
        print("Rock wins!")
    else:
        print("Scissors wins!")
elif selection_list == 'paper':
    if my_move == 'lizard':
        print("Lizard wins!")
    elif my_move == 'scissors':
        print("Scissors wins!")
    else:
        print("Paper wins!")
elif selection_list == 'spock':
    if my_move == 'paper':
        print("Paper wins!")
    elif my_move == 'lizard':
        print("Lizard wins!")
    else:
        print("Spock wins!")
elif selection_list == 'lizard':
    if my_move == 'rock':
        print("Rock wins!")
    elif my_move == 'Scissors':
        print("Scissors wins!")
    else:
        print("Lizard wins!")
