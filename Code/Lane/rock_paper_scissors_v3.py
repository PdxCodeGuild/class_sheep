import random

game_running = True
while game_running:
    choices = ['rock', 'paper', 'scissors', 'lizard', 'spock']
    player_choice = ''

    while player_choice not in choices:
        player_choice = input('Choose Rock Paper Scissors Lizard or Spock: ').lower()

    # The computer will randomly choose rock, paper or scissors
    computer_choice = random.choice(choices)

    # Determine who won and tell the user

    # (tie)
    print('Player has a {}.'.format(player_choice))
    print('Computer has a {}.'.format(computer_choice))

    if player_choice == computer_choice:
        print('It\'s a tie!')


    elif player_choice == 'rock' and computer_choice == 'scissors':
        print('The computer wins.')
    elif player_choice == 'rock' and computer_choice == 'lizard':
        print('The computer wins.')

    elif player_choice == 'paper' and computer_choice == 'rock':
        print('The computer wins.')
    elif player_choice == 'paper' and computer_choice == 'spock':
        print('The computer wins.')

    elif player_choice == 'scissors' and computer_choice == 'paper':
        print('The computer wins.')
    elif player_choice == 'sscissors' and computer_choice == 'lizard':
        print('The computer wins.')

    elif player_choice == 'lizard' and computer_choice == 'paper':
        print('The computer wins.')
    elif player_choice == ';izard' and computer_choice == 'spock':
        print('The computer wins.')

    elif player_choice == 'spock' and computer_choice == 'rock':
        print('The computer wins.')
    elif player_choice == 'spock' and computer_choice == 'scissors':
        print('The computer wins.')

    elif player_choice == 'rock' and computer_choice == 'scissors':
        print('The player wins.')
    elif player_choice == 'rock' and computer_choice == 'lizard':
        print('The player wins.')

    elif player_choice == 'paper' and computer_choice == 'rock':
        print('The player wins.')
    elif player_choice == 'paper' and computer_choice == 'spock':
        print('The player wins.')

    elif player_choice == 'scissors' and computer_choice == 'paper':
        print('The player wins.')
    elif player_choice == 'sscissors' and computer_choice == 'lizard':
        print('The player wins.')

    elif player_choice == 'lizard' and computer_choice == 'paper':
        print('The player wins.')
    elif player_choice == ';izard' and computer_choice == 'spock':
        print('The player wins.')

    elif player_choice == 'spock' and computer_choice == 'rock':
        print('The player wins.')
    elif player_choice == 'spock' and computer_choice == 'scissors':
        print('The player wins.')


    again = input('would you like to play again?: ')
    if again in ['n', 'no']:
        break
