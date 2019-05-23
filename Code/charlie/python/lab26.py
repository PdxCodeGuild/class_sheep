import random

width = 100  # the width of the board
height = 100  # the height of the board

# create a board with the given width and height
# we'll use a list of list to represent the board
board = []  # start with an empty list
for i in range(height):  # loop over the rows
    board.append([])  # append an empty row
    for j in range(width):  # loop over the columns
        board[i].append(' ')  # append an empty space to the board

# define the player position
player_i = height // 2
player_j = width // 2

#define player health
health = 5

# add 4 enemies in random locationsz
for i in range(200):
    enemy_i = random.randint(0, height - 1)
    enemy_j = random.randint(0, width - 1)
    board[enemy_i][enemy_j] = '§'

for k in range(100):
    treasure_l = random.randint(0, height -1)
    treasure_k = random.randint(0, width - 1)
    board[treasure_l][treasure_k] = '💩'


# loop until the user says 'done' or dies
while True:

    command = input('Use (awds) to move. To exit, type "done". What is your command? ')  # get the command from the user

    if command == 'done':
        break  # exit the game

    elif command in ['left', 'a']:
        player_j -= 1  # move left
        if player_j == 0:
            player_j = width - 1
    elif command in ['right', 'd']:
        player_j += 1  # move right
        if player_j == width:
            player_j %= width
    elif command in ['up', 'w']:
        player_i -= 1  # move up
        if player_i == 0:
            player_i = height - 1
    elif command in ['down', 's']:
        player_i += 1  # move down
        if player_i == height:
            player_i %= height

        # check if the player is on the same space as an enemy
    if board[player_i][player_j] == '§':
        print('you\'ve encountered an enemy! type "attack" to attack this monster')
        action = input('what will you do? ')
        if action == 'attack':
            print('you\'ve slain the enemy')
            board[player_i][player_j] = ' '  # remove the enemy from the board
        else:
            print('you hestitated and were injured')
            health -= 1
            print(health)
            if health == 0:
                print('You loose')
                break

        #
    if board[player_i][player_j] == '💩':
        print('Yuck!, what will you do? will you (a)"wipe your shoe", or (b)"take it like a man"?')
        action = input('what will you do? ')
        if action == 'a':
            print('cleanliness: +2 points')
        elif action == 'b':
            print('dude...')
            health -= 1
            print(health)
            if health == 0:
                print('You loose')
                break

    # player viewport
    for i in range(player_i - 10, player_i +10):
        for j in range(player_j - 10, player_j + 10):
            if i == player_i and j == player_j:
                print('☺', end=' ')
            else:
                print(board[i][j], end = '')
        print()
