#get a word as a string

#convert word to numbers (look at your number loop,
# before the loop make an empty list, append in the loop)

#shift numbers by 13 (look at turn_right.py)

#convert numbers into letters >>> string.ascii_lowercase[2]
#

# alphabet = dict(string.ascii_lowercase)

def cipher(input):

    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    rotated = 'nopqrstuvwxyzabcdefghijklm'
    output = '' #open string waiting for output, empty string is the pan waiting for the cake batter to go in it
    for letter in input:
        index = alphabet.find(letter)
        output += rotated[index]

    print(output)

user_input = (input("What do you want to encrypt?: "))

cipher(user_input)



#version 2
# def cipher(input, shifted_number):
#
#
#     alphabet = 'abcdefghijklmnopqrstuvwxyz'
#
#     output = '' #open string waiting for output, empty string is the pan waiting for the cake batter to go in it
#     for letter in input:
#         index = alphabet.find(letter)
#         index += shifted_number
#
#         if index >= len(alphabet):
#             index -= len(alphabet)
#         output += alphabet[index]
#
#     return output
#
# user_input = (input("What do you want to encrypt?: "))
# user_input2 = int(input("How many digits do you want to shift the alphabet by?: "))
#
# string = cipher(user_input, user_input2)
#
# print(string)
