import random
move_list = ['rock', 'paper', 'scissors', 'lizard', 'spock']
selection_list = input(f"Would you like to play {move_list[0]}, {move_list[1]}, {move_list[2]}, {move_list[3]}, or {move_list[4]} >")
while selection_list not in move_list:
    selection_list = [f"Which would you like, {move_list[0]}, {move_list[1]}, {move_list[2]}, {move_list[3]}, or {move_list[4]}?"]
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
