#patterngen.py

import random
pattern_list = ['##', '\\', '//', '~~', '**']
length = 10
out_string = ''
for iteration in range(length):
    out_string += random.choice(pattern_list) * 5
    out_string += '\n'
print(out_string)
