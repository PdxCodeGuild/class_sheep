#version 1

import string
import random

letters = string.ascii_letters
integer = string.digits
number = 10
out_string = ''

for iteration in range(number):
    out_string = out_string + (random.choice(string.ascii_letters + string.digits))
print(out_string)


#version 2
# import string
# import random
#
# letters = string.ascii_letters
# integer = string.digits
# number = 0
# user_length = ''
# out_string = ''
#
# user_length = int(input("How long do you want the password? "))
#
# for iteration in range(user_length):
#     out_string = out_string + (random.choice(string.ascii_letters + string.digits))
#
# print(out_string)
