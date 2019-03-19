# Lab 5: Random Emoticon Generator
# INSTRUCTIONS
# Let's generate emoticons by assembling a randomly choosing a set of eyes, a nose, and a mouth. Examples of emoticons are :-D =^P and :\
# 1. Define a list of eyes
# 2. Define a list of noses
# 3. Define a list of mouths
# 4. Randomly pick a set of eyes
# 5. Randomly pick a nose
# 6. Randomly pick a mouth
# 7. Assemble and display the emoticon

# Version 2
# Use a while loop to generate 5 emoticons.

import random
eyes_list = [':', ';', '8']
nose_list = ['3', '-', '>']
mouth_list = [')', '(', '|']
for num in range(5):
    out_string = ''
    out_string = out_string + random.choice(eyes_list) + random.choice(nose_list) + random.choice(mouth_list)
    out_string = out_string + '\n'
    print(out_string)
