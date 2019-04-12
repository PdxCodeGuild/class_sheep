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
eyes_list = [':', ';', '8', '=']
nose_list = ['—', '-', '>', '~']
mouth_list = [')', '(', '|', '3', 'P', '/',]
user_input = int(input("How many emojis do you want to make? > "))
# print number of emojis based on user input
for num in range(user_input):
    out_string = ''
    # randomly select from available eyes, noses, and mouths
    out_string = out_string + random.choice(eyes_list) + random.choice(nose_list) + random.choice(mouth_list)
    # add space between each emoji printed
    out_string = out_string + '\n'
    print(out_string)
