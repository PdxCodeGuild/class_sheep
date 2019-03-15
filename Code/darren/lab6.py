#lab6
#randompassword
import random
import string
lower_list = list(string.ascii_lowercase)
upper_list = list(string.ascii_uppercase)
symbol_list = list(string.punctuation)
running = True
while running == True:
    out_string = ''
    password = ''
    pass_chunk1 = ''
    pass_chunk2 = ''
    pass_chunk3 = ''
    lower_no = input("Please set number of lower case letters. >")
    upper_no = input("Please set number of upper case letters. >")
    symbol_no = input("Please set number of symbols. >")
    lower_no = int(lower_no)
    upper_no = int(upper_no)
    symbol_no = int(symbol_no)
    for num in range(0, lower_no):
        pass_chunk1 = pass_chunk1 + random.choice(lower_list)
    for num in range(0, upper_no):
        pass_chunk2 = pass_chunk2 + random.choice(upper_list)
    for num in range(0, symbol_no):
        pass_chunk3 = pass_chunk3 + random.choice(symbol_list)
    out_string = pass_chunk1 + pass_chunk2 + pass_chunk3
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
