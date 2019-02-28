import random
eyes_list = [':', ';', '8']
nose_list = ['3', '-', '>']
mouth_list = [')', '(', '|']
for num in range(5):
    out_string = ''
    out_string = out_string + random.choice(eyes_list) + random.choice(nose_list) + random.choice(mouth_list)
    out_string = out_string + '\n'
    print(out_string)
