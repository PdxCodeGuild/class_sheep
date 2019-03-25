# Lab 6: Password Generator
# Let's generate a password of length n using a while loop and random.choice, this will be a string of random characters.
# Hint: random.choice can be used to pick a character out of a string, as well as an element out of a list.
# Version 2
# Allow the user to enter the value of n, remember to convert its type, as input returns a string.

import random
import string
user_length = int(input("How many characters do you want your password to be? > "))
out_string = ''
characters = 0
# add to password until user length is reached
while characters <= user_length:
    characters += 1
# randomize numbers, punctuation, and lower- and uppercase letters at user-specified length
for answer in range(user_length):
    out_string += random.choice(string.digits + string.ascii_lowercase + string.ascii_uppercase + string.punctuation)
print(out_string)

# Version 3 (optional)
# INSTRUCTIONS: Ask the user for how many lowercase letters, uppercase letters, numbers, and special characters they'd like in their password. Generate a password accordingly.
user_uc = int(input("How many uppercase letters do you want in your password? > "))
user_lc = int(input("How many lowercase letters do you want in your password? > "))
user_num = int(input("How many numbers do you want in your password? > "))
user_sc = int(input("How many special characters do you want in your password? > "))
out_string = ''
# create outstring with user-specified number of characters
for answer in range(user_uc):
    out_string += random.choice(string.ascii_uppercase)
for answer in range(user_lc):
    out_string += random.choice(string.ascii_lowercase)
for answer in range(user_sc):
    out_string += random.choice(string.punctuation)
for answer in range(user_num):
    out_string += random.choice(string.digits)
# turn into a list (outstrings are immutable)
password = list(out_string)
# shuffle characters
random.shuffle(password)
# turn back into a string to print
print(''.join(password))
