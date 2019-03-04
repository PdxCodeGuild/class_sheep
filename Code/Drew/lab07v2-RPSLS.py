import random
import string

options = ['Rock', 'Paper', 'Scissors']
while True:
    user_choice = string.capwords(input('Rock, Paper, or Scissors?\n'))
    if user_choice not in options:
        print("Try again.")
        continue
    else:
        break
comp_choice = random.choice(options)
print(f"I chose {comp_choice}")

user_choice = options.index(user_choice)
comp_choice = options.index(comp_choice)

print(f"user choice is {user_choice}")
print(f"comp choice is {comp_choice}")
print(f"comp%3 = {comp_choice%3}")
print(f"user%3 = {user_choice%3}")
if user_choice == comp_choice:
    print("Tie.")
elif user_choice == ((comp_choice+1) % 3):
    print("You win.")
elif comp_choice == ((user_choice+1) % 3):
    print("You lose.")
