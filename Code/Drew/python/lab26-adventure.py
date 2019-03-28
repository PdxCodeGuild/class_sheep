import random
import time
import blackjack

# Introduction - printed out by letter with time delay
intro = "\nThe year is 2832.\nEarth has been overthrown by an evil race of alien casino employees.\nHumanity is entirely extinct."
intro2 = "\nCats have evolved to disguise themselves as aliens.\nYou are a robot, rescuing kittens from amongst these alien blackjack dealers.\n"
intro3 = "\nTESTINTRO"
#for letter in intro:
#    print(letter, end='', flush=True)
#    time.sleep(.04)
#time.sleep(.8)
#for letter in intro2:
#    print(letter, end='', flush=True)
#    time.sleep(.04)
for letter in intro3:
   print(letter, end='', flush=True)
   time.sleep(.04)

# Set the size of the board
width = 20
height = 20

# Fill board with spaces
board = []
for i in range(height):
    board.append([])
    for j in range(width):
        board[i].append(' ')

# Set starting location for player
player_i = 9
player_j = 9

# Set a number of aliens
alien_num = 8
# Set number of kittens
kitten_num = 3

# Generate that number of aliens
for i in range(alien_num + kitten_num):
    enemy_i = random.randint(0, height - 1)
    enemy_j = random.randint(0, width - 1)
    board[enemy_i][enemy_j] = '👾'

# Each entity will be associated with either 'e' for 'enemy', or 'k' for 'kitten'
kitten_chance = []
for i in range(kitten_num):
    kitten_chance.append('e')
for i in range(alien_num):
    kitten_chance.append('e')
print(kitten_chance)
# This list gives multiple options to be printed if player is defeated
loss_list = ['The alien blackjack dealer eats off your face.','You are smashed into metal dust by the alien.','Your robot body will be used as casino furniture.','You have failed the helpless kittens.','The kittens were wrong to have placed their faith in you.','The alien turns your head into an ashtray.','Your circuits overload with shame.','You are not the hero the kittens deserve.','You have been repurposed into a slot-machine.']

# Set number of kittens found
kittens_found = 0

# Gameplay
while kittens_found < 3:
    # Display number of kittens found so far
    print(kittens_found)
    # User input - move robot or quit
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
    # If robot lands on the same space as an alien
    if board[player_i][player_j] == '👾':
        # Designate that alien to be an enemy or a kitten
        id_index = random.randint(0,len(kitten_chance)-1)
        identifier = kitten_chance[id_index]
        # If alien is an enemy, play blackjack against it
        if identifier == 'e':
            print("It's an alien blackjack dealer!")
            outcome = blackjack.blackjack_game()
            if outcome == 'win':
                print("You are victorious.")
                time.sleep(2)
                board[player_i][player_j] = ' '
                kitten_chance.pop(id_index)
            elif outcome == 'tie':
                print("You have tied.")
                time.sleep(2)
                continue
            else:
                print('\nDefeat.')
                time.sleep(1)
                for letter in random.choice(loss_list):
                    print(letter, end='', flush=True)
                    time.sleep(.05)
                print()
                break
        # If alien is a kitten, game is won
        elif identifier == 'k':
            print("You found the kitten!")
            break
    # Displays robot at player's locaton
    for i in range(height):
        for j in range(width):
            if i == player_i and j == player_j:
                print('🤖', end=' ')
            else:
                print(board[i][j], end=' ')
        print()
