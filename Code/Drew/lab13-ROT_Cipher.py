import string
import random

user_string = input("Enter a string:\n")

# ask for rotation integer with validation
while True:
    turns = input("Enter an amount of rotation (0-25), or type 'random':\n")
    if turns == 'random':
        turns = random.choice(range(0, 25))
    else:
        try:
            turns = int(turns)
        except:
            print("Not a valid number.")
            continue
    if turns > 25:
        print("Not a valid number.")
        continue
    elif turns < 0:
        print("Not a valid number.")
        continue
    elif turns >= 0 and turns <= 25:
        break

# build dicitonary
rot_list = {}
rot_num = 0
letters = string.ascii_lowercase
for x in letters:
    rot_list[x] = rot_num
    rot_num += 1
print(rot_list)

# convert user string to ciphertext
output = ''
for i in user_string:
    if i in letters:
        cipher = rot_list[i] + turns
        if cipher > 25:
            cipher -= 26
            output += str(cipher)
        else:
            output += str(cipher)
    else:
       output += str(i)


print(output)
