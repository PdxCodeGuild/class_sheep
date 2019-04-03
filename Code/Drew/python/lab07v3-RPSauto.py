import random
import string
import time

options = ['Rock', 'Paper', 'Scissors']
player1 = input("Enter a name for Player 1:\n")
player2 = input("Enter a name for Player 2:\n")
game_number = int(input("Best of how many games?\n"))

i = 0
tie_count = 0
points1 = 0
points2 = 0
while i < game_number:
    choice1 = random.choice(options)
    choice2 = random.choice(options)
    #print(f"{choice1} vs {choice2}")
    choice1 = options.index(choice1)
    choice2 = options.index(choice2)
    i += 1
    if choice1 == choice2:
        tie_count += 1
        #print("Tie.")
        continue
    elif choice1 == ((choice2+1) % 3):
        points1 += 1
        #print(f"{player1} wins.")
    elif choice2 == ((choice1+1) % 3):
        points2 += 1
        #print(f"{player2} wins.")
    #time.sleep(.2)
print()
print(f"Ties: {tie_count}")
print(f"{player1}: {points1}")
print(f"{player2}: {points2}")
