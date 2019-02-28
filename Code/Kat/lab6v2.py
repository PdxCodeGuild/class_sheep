# ', and also '.join(['red', 'blue', 'green'])
# ''.join(['red', 'blue', 'green'])

import random
import string
user_uc = int(input("How many uppercase letters do you want in your password?"))
user_lc = int(input("How many lowercase letters do you want in your password?"))
user_sc = int(input("How many special characters do you want in your password?"))
cat = 0
while cat < user_uc:
    cat += 1
while cat < user_lc:
    cat += 1
while cat < user_sc:
    cat += 1
