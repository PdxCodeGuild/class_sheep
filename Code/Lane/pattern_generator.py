import random
pattern list = ['##', '\\', '//', '~~', '**']
length = 10
out_string = ''
for iteration in range(length):
    # out_string += random.choice(pattern_list) * 5 multiplying the string of two characters by 5 to get a result of 10 of that symbol
    out_string += '\n'
print(out_string)

# notice how the \ has  less lines, that is becasue it has a special function to it and tell the computer to skip the next character, in effect removing one \ from the list
#
# try this version:

import random
pattern list = ['##', '\\\\', '//', '~~', '**']
length = 10
out_string = ''
for iteration in range(length):
    out_string += random.choice(pattern_list) * 5
    out_string += '\n'
print(out_string)
