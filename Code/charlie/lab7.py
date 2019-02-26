import random

options_list = ['rock','paper','scissors','lizard', 'spock']
print('Welcome to rock, paper, scissors, lizard, spock')
user_input = input('which will you choose? > ')
computer_selection = random.choice(options_list)

if user_input == 'rock':
    if computer_selection == 'rock':
        print('You both picked the same thing! It\'s a tie.')
    elif computer_selection == 'paper':
        print('paper covers rock, computer wins')
    elif computer_selection == 'lizard':
        print('rock crushes lizard, player wins')
    elif computer_selection == 'spock':
        print('spock vaporizes rock, computer wins')

    else:
        print('rock crushes scissors, player wins!')

if user_input == 'scissors':
    if computer_selection == 'scissors':
        print('You both picked the same thing! It\'s a tie.')
    elif computer_selection == 'rock':
        print('rock beats scissors, computer wins')
    elif computer_selection == 'lizard':
        print('scissors decapitates lizard, player wins')
    elif computer_selection == 'spock':
        print('spock smashes scissors, computer wins')
    else:
        print('scissors beats paper, player wins!')

if user_input == 'paper':
    if computer_selection == 'paper':
        print('You both picked the same thing! It\'s a tie.')
    elif computer_selection == 'scissors':
        print('scissors beats paper, computer wins')
    elif computer_selection == 'lizard':
        print('lizard eats paper, computer wins')
    elif computer_selection == 'spock':
        print('paper disproves spock, player wins')
    else:
        print('paper beats rock, player wins!')

if user_input == 'spock':
    if computer_selection == 'spock':
        print('You both picked the same thing! It\'s a tie.')
    elif computer_selection == 'scissors':
        print('spock crushes scissors, player wins')
    elif computer_selection == 'lizard':
        print('lizard poisons spock, computer wins')
    elif computer_selection == 'rock':
        print('spock vaporizes rock, player wins')
    else:
        print('spock vaporizes rock, player wins!')

if user_input == 'lizard':
    if computer_selection == 'lizard':
        print('You both picked the same thing! It\'s a tie.')
    elif computer_selection == 'scissors':
        print('scissors decapitates lizard, computer wins')
    elif computer_selection == 'rock':
        print('rock crushes lizard, computer wins')
    elif computer_selection == 'spock':
        print('lizard poisons spock, player wins')
    else:
        print('lizard eats paper, player wins!')

play_again = input('do you want to play again? Press \'y\' for Yes, or anything else to Exit >')

if play_again == "y":
    user_input = input('which will you choose? > ')
    computer_selection = random.choice(options_list)

    if user_input == 'rock':
        if computer_selection == 'rock':
            print('You both picked the same thing! It\'s a tie.')
        elif computer_selection == 'paper':
            print('paper covers rock, computer wins')
        elif computer_selection == 'lizard':
            print('rock crushes lizard, player wins')
        elif computer_selection == 'spock':
            print('spock vaporizes rock, computer wins')

        else:
            print('rock crushes scissors, player wins!')

    if user_input == 'scissors':
        if computer_selection == 'scissors':
            print('You both picked the same thing! It\'s a tie.')
        elif computer_selection == 'rock':
            print('rock beats scissors, computer wins')
        elif computer_selection == 'lizard':
            print('scissors decapitates lizard, player wins')
        elif computer_selection == 'spock':
            print('spock smashes scissors, computer wins')
        else:
            print('scissors beats paper, player wins!')

    if user_input == 'paper':
        if computer_selection == 'paper':
            print('You both picked the same thing! It\'s a tie.')
        elif computer_selection == 'scissors':
            print('scissors beats paper, computer wins')
        elif computer_selection == 'lizard':
            print('lizard eats paper, computer wins')
        elif computer_selection == 'spock':
            print('paper disproves spock, player wins')
        else:
            print('paper beats rock, player wins!')

    if user_input == 'spock':
        if computer_selection == 'spock':
            print('You both picked the same thing! It\'s a tie.')
        elif computer_selection == 'scissors':
            print('spock crushes scissors, player wins')
        elif computer_selection == 'lizard':
            print('lizard poisons spock, computer wins')
        elif computer_selection == 'rock':
            print('spock vaporizes rock, player wins')
        else:
            print('paper beats rock, player wins!')

    if user_input == 'lizard':
        if computer_selection == 'lizard':
            print('You both picked the same thing! It\'s a tie.')
        elif computer_selection == 'scissors':
            print('scissors decapitates lizard, computer wins')
        elif computer_selection == 'rock':
            print('rock crushes lizard, computer wins')
        elif computer_selection == 'spock':
            print('lizard poisons spock, player wins')
        else:
            print('lizard eats paper, player wins!')
else:
    print('Thanks for playing!')
