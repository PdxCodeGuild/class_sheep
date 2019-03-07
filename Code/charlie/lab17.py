#lab17.py
''' i want to input a string
then i want to convert the string into indicies
then i want to compare the first and last indicies to determine if they are the same
if they are the same, return true
else return false
'''

import string
def check_palindrome(input_string):
    abc_list = list(string.ascii_lowercase)
    list2 = []
    string_list = []
    reverse_list = []
    for letter in input_string:
        string_list.append(abc_list.index(letter))
    for letter in input_string:
        reverse_list.append(abc_list.index(letter))

    reverse_list.reverse()

    print(string_list)
    print(reverse_list)
    # index = 0
    length = len(string_list)
    for index in range(len(string_list)):
        if string_list != reverse_list:
            # index +=1
            # if index == length:
            return False
        else:
            return True
    #     for letter2 in range(len(reverse_list)):
    #         if current_index == letter2[index]:
    #
    #         return False

        # reverse_list=reverse_list.index(letters)
        # print(f"index:{letter}")
        # print(f"letter:{letter}")

print(check_palindrome('racecar'))
