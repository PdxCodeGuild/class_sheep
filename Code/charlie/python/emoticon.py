#emoticon.py
import random

eye_list = [':', ';']
nose_list =['-', '>']
mouth_list = [')','}']
number = 22
out_string = ''
for iteration in range(number):
    out_string = ''
    out_string = out_string + random.choice(eye_list) + random.choice(nose_list) + random.choice(mouth_list)
    print(out_string)
    print(len(out_string))
