import random
import string
user_length = input("How many characters do you want your password to be?")
user_length = int(user_length)
out_string = ''
cat = 0
while cat < user_length:
    cat += 1
for answer in range(0, user_length):
    out_string = out_string + random.choice(string.digits + string.ascii_lowercase + string.ascii_uppercase + string.punctuation)
print(out_string)
