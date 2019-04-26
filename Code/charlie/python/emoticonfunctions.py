#emoticonfunctions.py
import random

eyes = ":;"
noses = ">-"
mouths = ")]"

def gen_faces(in_number):
    out_string = ''
    for iteration in range(in_number):
        out_string = out_string + random.choice(eyes) + random.choice(noses)+random.choice(mouths) + '\n'
    return out_string


user_num = int(input("how many faces?"))

# for iteration in range(user_num):
#     print(random.choice(eyes) + random.choice(noses)+random.choice(mouths) + '\n')
print(gen_faces(user_num), end='')
