import random
import string

options = ['Rock', 'Paper', 'Scissors']
player1 = input("Enter a name for Player 1")
player2 = input("Enter a name for Player 2")
game_number = int(input("Best of how many games?"))

i = 0
while i < game_number:
    points1 = 0
    points2 = 0
    choice1 = random.choice(options)
    choice2 = random.choice(options)
    if choice1 == choice2:
        continue
    elif choice1 == ((choice2+1) % 3):
        points1 += 1
    elif choice2 == ((choice1+1) % 3):
        points2 += 1

print(f"{player1}: {points1}")
print(f"{player2}: {points2}")
