import random
import string

#===========================================================================
# user input
user_string = input("Your string, please\n")
user_rotation = int(input("how many times do you want to encrpyt your information.  Must be an integer  "))

#===========================================================================

# input translation
user_list = list(user_string)
abc_list = list(string.ascii_lowercase)
ROT13_num_list = []
ROT13_letter_list = []

ROT13_outstring = ''

length = len(user_list)
for letters in range(length):
    random_letter = random.choice(user_list)#randomly selects a letter from the string list
    ROT13_num_list.append((abc_list.index(random_letter)+13)*(user_rotation))
    user_list.remove(random_letter)
    # print(user_list)
    print(ROT13_num_list)

length2 = len(ROT13_num_list)
for indicies in range(length2):
    random_number2 = random.choice(ROT13_num_list)
    ROT13_num_list.remove(random_number2)
    if random_number2 >= 26:
        random_number2 %= 13
        random_letter = abc_list[random_number2]
        ROT13_letter_list.append(random_letter)
        # ROT13_num_list.remove(random_number2)


    else:
        print(random_number2)
        ROT13_letter_list.append(abc_list[random_number2])
        # ROT13_num_list.remove(random_number2)
print(ROT13_letter_list)

length3 = len(ROT13_letter_list)
# print(length3)
for letters in range(length3):
    choice = random.choice(ROT13_letter_list)
    # print(choice)
    ROT13_outstring += choice
    ROT13_letter_list.remove(choice)
print(ROT13_letter_list)
print(ROT13_outstring)
