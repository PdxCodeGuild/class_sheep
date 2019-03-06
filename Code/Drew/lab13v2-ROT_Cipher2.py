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

# convert back to letters
# first, get rid of this double spacing
out2 = output.split(' ')
space_index = []
iteration = 0
for num in out2:
    if num == '':
        space_index.append(iteration)
        iteration += 1
    else:
        iteration += 1
        continue

# get every other space, delete from list
def alternates(a):
    return a[::2]
space_index = alternates(space_index)
for x in sorted(space_index, reverse=True):
    del out2[x]
    x -= 1

# convert to letters and add to new list
numoutlist = []
for x in out2:
    if x == '':
        numoutlist.append(' ')
    else:
        try:
            numoutlist.append(chr(((int(x)-turns)%26)+97))
        except:
            numoutlist.append(x)

# print final output
decr = ''.join(numoutlist)
print(decr)