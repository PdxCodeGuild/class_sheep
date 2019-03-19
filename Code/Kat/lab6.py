# Lab 6: Password Generator
# Let's generate a password of length n using a while loop and random.choice, this will be a string of random characters.
# Hint: random.choice can be used to pick a character out of a string, as well as an element out of a list.
# Version 2
# Allow the user to enter the value of n, remember to convert its type, as input returns a string.

import random
import string
user_length = input("How many characters do you want your password to be?")
user_length = int(user_length)
out_string = ''
cat = 0
while cat < user_length:
    cat += 1
for answer in range(user_length):
    out_string = out_string + random.choice(string.digits + string.ascii_lowercase + string.ascii_uppercase + string.punctuation)
print(out_string)

# Version 3 (optional)
# INSTRUCTIONS: Ask the user for how many lowercase letters, uppercase letters, numbers, and special characters they'd like in their password. Generate a password accordingly.
user_uc = int(input("How many uppercase letters do you want in your password?"))
user_lc = int(input("How many lowercase letters do you want in your password?"))
user_sc = int(input("How many special characters do you want in your password?"))
cat = 0
while cat < user_uc:
    cat += 1
while cat < user_lc:
    cat += 1
while cat < user_sc:
    cat += 1
