import random
# Let's play rock-paper-scissors with the computer.

# The computer will ask the user for their choice (rock, paper, scissors)
game_running = True
while game_running:
    choices = ['r', 'p', 's']
    player_choice = ''

    while player_choice not in choices:
        player_choice = input('Choose (R)ock (P)aper or (S)cissors: ').lower()

    # The computer will randomly choose rock, paper or scissors
    computer_choice = random.choice(choices)

    # Determine who won and tell the user
    # Let's list all the cases:

    # rock vs rock (tie)
    print('Player has a {}.'.format(player_choice))
    print('Player has a {}.'.format(computer_choice))

    if player_choice == computer_choice:
        print('It\'s a tie!')
    # rock vs paper
    elif player_choice == 'r' and computer_choice == 'p':
        print('The computer wins.')
    elif player_choice == 'p' and computer_choice == 'r':
        print('The player wins.')
    # rock vs scissors
    elif player_choice == 's' and computer_choice == 'r':
        print('The computer wins.')
    elif player_choice == 'r' and computer_choice == 's':
        print('The player wins.')
    # paper vs scissors
    elif player_choice == 'p' and computer_choice == 's':
        print('The computer wins.')
    elif player_choice == 's' and computer_choice == 'p':
        print('The player wins.')

    again = input('would you like to play again?: ')
    if again in ['n', 'no']:
        break
