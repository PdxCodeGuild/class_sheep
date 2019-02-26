import random
import string

while True:
    user_choice = string.capwords(input('Rock, Paper, Scissors, Lizard, or Spock?\n'))
    comp_choice = random.choice(['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock'])
    if user_choice == comp_choice:
        print(f"{comp_choice} - Tie")
    elif user_choice.lower() == 'rock':
        if comp_choice.lower() == 'paper':
            print('Paper covers rock. I win.')
        elif comp_choice.lower() == 'scissors':
            print('Rock crushes scissors. You win.')
        elif comp_choice.lower() == 'lizard':
            print('Rock crushes lizard. You win.')
        elif comp_choice.lower() == 'spock':
            print('Spock vaporizes rock. I win.')
    elif user_choice.lower() == 'paper':
        if comp_choice.lower() == 'rock':
            print('Paper covers rock. You win.')
        elif comp_choice.lower() == 'scissors':
            print('Scissors cut paper. I win.')
        elif comp_choice.lower() == 'lizard':
            print('Lizard eats paper. I win.')
        elif comp_choice.lower() == 'spock':
            print('Paper disproves Spock. You win.')
    elif user_choice.lower() == 'scissors':
        if comp_choice.lower() == 'paper':
            print('Scissors cut paper. You win.')
        elif comp_choice.lower() == 'rock':
            print('Rock crushes scissors. I win.')
        elif comp_choice.lower() == 'lizard':
            print('Scissors decapitate lizard. You win.')
        elif comp_choice.lower() == 'spock':
            print('Spock smashes scissors. I win.')
    elif user_choice.lower() == 'lizard':
        if comp_choice.lower() == 'paper':
            print('Lizard eats paper. You win.')
        elif comp_choice.lower() == 'scissors':
            print('Scissors decapitate lizard. I win.')
        elif comp_choice.lower() == 'rock':
            print('Rock crushes lizard. I win.')
        elif comp_choice.lower() == 'spock':
            print('Lizard poisons Spock. You win.')
    elif user_choice.lower() == 'spock':
        if comp_choice.lower() == 'paper':
            print('Paper disproves Spock. I win.')
        elif comp_choice.lower() == 'scissors':
            print('Spock smashes scissors. You win.')
        elif comp_choice.lower() == 'lizard':
            print('Lizard poisons Spock. I win.')
        elif comp_choice.lower() == 'rock':
            print('Spock vaporizes rock. You win.')
    again = input('Would you like to play again?\n')
    if again.lower() in ['y', 'yes', 'ok', 'sure', 'whatever']:
        continue
    else:
        break

