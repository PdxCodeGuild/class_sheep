import random
import string

letters = string.ascii_letters
integer = string.digits
number = 3
out_string = ''
for iteration in range(number):
    out_string = out_string + random.choice(string.ascii_letters)
    out_string = out_string + random.choice(string.digits)
print(out_string)
