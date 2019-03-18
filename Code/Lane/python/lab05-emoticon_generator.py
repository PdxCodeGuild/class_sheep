import random

eyes = [':', ';']
nose = ['^', '-']
mouth = ['(', ')', 'D']
number = 5
out_string = ''
for iteration in range(number):
    out_string += random.choice(eyes)
    out_string += random.choice(nose)
    out_string += random.choice(mouth)
print(out_string)


# another way to write this:
#     print(random.choice(eyes) + random.choice(nose) + random.choice(mouth))
# Or put this line above into a for loop to get five emoticons
