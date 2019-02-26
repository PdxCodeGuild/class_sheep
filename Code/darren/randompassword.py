#randompassword
import random
import string
out_string = ''
running = True
while running:
    passlength = input("Please set password length. >")
    passlength = int(passlength)
    for num in range(0, passlength):
        out_string = out_string + random.choice(string.ascii_lowercase + string.ascii_uppercase + string.punctuation)
    print(out_string)
    cont = input("Type anything to redo password or type 'done' to confirm. >")
    if cont.lower() == 'done':
        running = False
