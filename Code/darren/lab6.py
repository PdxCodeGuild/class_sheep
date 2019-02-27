#lab6
#randompassword
import random
import string
lowerlist = list(string.ascii_lowercase)
upperlist = list(string.ascii_uppercase)
symbollist = list(string.punctuation)
running = True
while running == True:
    out_string = ''
    password = ''
    passchunk1 = ''
    passchunk2 = ''
    passchunk3 = ''
    lowerno = input("Please set number of lower case letters. >")
    upperno = input("Please set number of upper case letters. >")
    symbolno = input("Please set number of symbols. >")
    lowerno = int(lowerno)
    upperno = int(upperno)
    symbolno = int(symbolno)
    for num in range(0, lowerno):
        passchunk1 = passchunk1 + random.choice(lowerlist)
    for num in range(0, upperno):
        passchunk2 = passchunk2 + random.choice(upperlist)
    for num in range(0, symbolno):
        passchunk3 = passchunk3 + random.choice(symbollist)
    out_string = passchunk1 + passchunk2 + passchunk3
    password = list(out_string)
    random.shuffle(password)
    password = ''.join(password)
    print(password)
    cont = input("Type anything to redo password or type 'done' to confirm. >")
    if cont.lower() == 'done':
        running = False
#while running == True:
    #passlength = input("Please set password length. >")
    #passlength = int(passlength)
    #for num in range(0, passlength):
        #out_string = out_string + random.choice(string.ascii_lowercase + string.ascii_uppercase + string.punctuation)
    #print(out_string)
    #cont = input("Type anything to redo password or type 'done' to confirm. >")
    #if cont.lower() == 'done':
        #running = False
