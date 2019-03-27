import random

width = 10  # the width of the board
height = 10  # the height of the board

# create a board with the given width and height
# we'll use a list of list to represent the board
board = []  # start with an empty list
for i in range(height):  # loop over the rows
    board.append([])  # append an empty row
    for j in range(width):  # loop over the columns
        board[i].append(' ')  # append an empty space to the board

# define the player position
player_i = 4
player_j = 4

# add 5 enemies in random locations
for i in range(5):
    enemy_i = random.randint(0, height - 2)
    enemy_j = random.randint(0, width - 2)
    board[enemy_i][enemy_j] = 'X'

# add "treasure" aka pizza to collect
for i in range(10):
    heart_i = random.randint(0, height - 2)
    heart_j = random.randint(0, width - 2)
    board[heart_i][heart_j] = '♥'

# loop until the user says 'done' or dies

life_counter = 10 # set number of lives
enemy_counter = 5 # set number of enemies
heart_counter = 0
print(f'You have {life_counter} lives.')
while True:

    command = input('Where to? ')  # get the command from the user
    print(heart_counter)
    print(enemy_counter)
    if command == 'done':
        break  # exit the game
    elif command in ['left', 'l', 'west', 'w']:
        if player_j < 1: #alert player to edges
            print('Your earth isn\'t flat, but this one is. Please turn around!')
        else:
            player_j -= 1  # move left
    elif command in ['right', 'r', 'east', 'e']:
        if player_j > width - 2:
            print('Your earth isn\'t flat, but this one is. Please turn around!')
        else:
            player_j += 1  # move right
    elif command in ['up', 'u', 'north', 'n']:
        if player_i < 1:
            print('Your earth isn\'t flat, but this one is. Please turn around!')
        else:
            player_i -= 1  # move up
    elif command in ['down', 'd', 'south', 's']:
        if player_i > height - 2:
            print('Your earth isn\'t flat, but this one is. Please turn around!')
        else:
            player_i += 1  # move down


    # check if the player is on the same space as an enemy

    if board[player_i][player_j] == 'X':
        print('Yikes! An X! Press "a" to attack.')
        action = input('what will you do? ')
        if action == 'a':
            print('You fought the good fight and won. Good work!')
            board[player_i][player_j] = ' '  # remove the snow from the board
            enemy_counter -= 1
        else:
            life_counter -= 1 # reduce life counter by one
            print(f'Death prevailed. Lives remaining: {life_counter}')
            if life_counter == 0:
                print('This is the end, my friend! Goodbye.') # exit the loop when lives are gone
                break


    if board[player_i][player_j] == '♥':
        print('Love? Press "y" to collect.')
        action = input('what will you do? ')
        if action == 'y':
            print('You\'re special. Good work!')
            board[player_i][player_j] = ' '  # remove the enemy from the board
            heart_counter += 1
            if enemy_counter == 0 and heart_counter == 10:
                print('Victory is sweet! Congratulations.')
                break
    # print out the board
    for i in range(height):
        for j in range(width):
            # if we're at the player location, print the player icon
            if i == player_i and j == player_j:
                print('☺', end=' ')
            else:
                print(board[i][j], end=' ')  # otherwise print the board square
        print()
