import random
import time
import blackjack

#intro = "\nThe year is 2832.\nEarth has been overthrown by an evil race of alien casino employees.\nHumanity is entirely extinct.\nCats have evolved to disguise themselves as aliens.\nYou are a robot, rescuing kittens from among these alien blackjack dealers.\n"
intro = "test"
for letter in intro:
    print(letter, end='', flush=True)
    time.sleep(.05)

width = 20
height = 20

board = []
for i in range(height):
    board.append([])
    for j in range(width):
        board[i].append(' ')

player_i = 9
player_j = 9

for i in range(9):
    enemy_i = random.randint(0, height - 1)
    enemy_j = random.randint(0, width - 1)
    board[enemy_i][enemy_j] = '👾'

kitten_chance = ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'k']

while True:
    command = input('WASD to move, q to quit: ')
    if command == 'q':
        break
    elif command == 'a':
        player_j -= 1
    elif command == 'd':
        player_j += 1
    elif command == 'w':
        player_i -= 1
    elif command == 's':
        player_i += 1

    if board[player_i][player_j] == '👾':
        id_index = random.randint(0,len(kitten_chance)-1)
        identifier = kitten_chance[id_index]
        if identifier == 'e':
            print("It's an alien blackjack dealer!")
            outcome = blackjack.blackjack_game()
            if outcome == 'win':
                print("You are victorious.")
                board[player_i][player_j] = ' '
                kitten_chance.pop(id_index)
            else:
                print('You have been defeated')
                break
        elif identifier == 'k':
            print("You found the kitten!")
            break
    for i in range(height):
        for j in range(width):
            if i == player_i and j == player_j:
                print('🤖', end=' ')
            else:
                print(board[i][j], end=' ')
        print()
