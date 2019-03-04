import string
import random

user_string = input("Enter a string:\n")
user_string = user_string.lower()

# ask for rotation integer with validation
while True:
    turns = input("Enter an amount of rotation, or type 'random':\n")
    if turns == 'random':
        turns = random.choice(range(0, 25))
    else:
        try:
            turns = int(turns)
            break
        except:
            print("Not a valid number.")
            continue
turns = turns%26

# encrypt and concatenate to output
output = ''
for i in user_string:
    if i in string.ascii_lowercase:
        output += str(((ord(i)+turns) - 97) % 26) + ' '
    else:
        output += i + ' '

print(output)
