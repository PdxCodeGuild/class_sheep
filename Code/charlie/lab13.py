import string
import random

user_string = input("Your string, please\n")
# print(user_string)


user_list = list(user_string)
# print(user_list)

abc_list = list(string.ascii_lowercase)
ROT13_num_list = []
ROT13_letter_list = []
ROT13_outstring = ''
# list = user_list.split('')
# print(list)
length = len(user_list)
for letters in range(length):
    random_letter = random.choice(user_list)#randomly selects a letter from the string list
    ROT13_num_list.append(abc_list.index(random_letter)+13)
    user_list.remove(random_letter)
    # print(user_list)
    # print(ROT13_num_list)

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

 #    ROT13_list.append(abc_list.index(random_letter)+13)
 #    random_letter1 = random.choice(user_list)
 #    if random_letter == random_letter1:#if the two randomly selected letters are the same
 #         #return to the top of the for loop and repeat
 #         continue
 #    elif random_letter != random_letter1:
 #
 #        abc_list.index(random_letter1)
 #        ROT13_list.append(abc_list.index(random_letter1)+13)  #index the randomly selected letter
 #        #adds the indexed number to the empty ROT13 list and adds 13 to it
 #
 #     #defines the next choice
 #
 # #if the two selected letters are different, add the index to the list and add 13





# length = len(user_list)
# for letters in range(length):
#     random_letter = random.choice(user_list) #randomly selects a letter from the string list
#     print(random_letter) #prints the selected letter
#     abc_list.index(random_letter) #index the randomly selected letter
#     print(abc_list.index(random_letter))
#     ROT13_list.append(abc_list.index(random_letter)+13) #adds the indexed number to the empty ROT13 list and adds 13 to it
#
#     random_letter1 = random.choice(user_list) #defines the next choice
#
#     if random_letter == random_letter1:#if the two randomly selected letters are the same
#
# # remove the selected letter
#         continue #return to the top of the for loop and repeat
#     elif random_letter != random_letter1: #if the two selected letters are different, add the index to the list and add 13
#         abc_list.index(random_letter1)
#         ROT13_list.append(abc_list.index(random_letter1)+13)
# print(user_list)
# print(ROT13_list)
