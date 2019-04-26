import string
import random

# #
# # def latest_alpha(input_letter):
# #     return(string.ascii_lowercase.index(input_letter))
# #
# # print(latest_alpha('y'))
#
#
# def latest_word(input_word):
#     alpha_num = 0
#     for letter in input_word:
#         # print(letter)
#         if string.ascii_lowercase.index(letter) > alpha_num:
#             alpha_num = string.ascii_lowercase.index(letter)
#     return string.ascii_lowercase[alpha_num]
#
#
#     # return(string.ascii_lowercase.index(input_letter))
#
# print(latest_word('asdfuilaergiusfdaiulfdiuhruiwplploijkmngv'))

number_list = []
def even_numbers(input_num_list):
    length2 = len(input_num_list)
    for nums in range(length2):
        number1 = random.choice(input_num_list)
        if number1 % 2 == 0:
            number = number1
            number = 1
            number_list.append(number)
            input_num_list.remove(number1)

        else:
            input_num_list.remove(number1)
    length = len(number_list)
    if length % 2 == 0:
        # print(True)
        return(True)
    else:
        # print(False)
        return(False)

# even_numbers([6, 4, 3, 0, 20, 4, 10, 33, 3, 1])
#
# even_numbers([5, 5, 2])
#
# even_numbers([2, 2, 3, 4, 5, 6, 2, 3, 2, 2])

input_num_list = even_numbers([3, 5, 3, 2, 3, 2, 2])
print(number_list)
print(input_num_list)
