import random
eyes_list = [':', ';', '8']
nose_list = ['~', '-', '>']
mouth_list = [')', '(', '|']
out_string = ''
out_string = out_string + random.choice(eyes_list) + random.choice(nose_list) + random.choice(mouth_list)
print(out_string)
