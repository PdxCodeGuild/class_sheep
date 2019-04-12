# Lab 13: ROT Cipher
# Write a program that prompts the user for a string, and encodes it with ROT13. For each character, find the corresponding character, add it to an output string. Notice that there are 26 letters in the English language, so encryption is the same as decryption.

# Version 2 (optional)
# Allow the user to input the amount of rotation used in the encryption / decryption.

import string
user_letters = list(string.ascii_lowercase)
to_encode = input('Type a word that you would like to encode > ')
user_direction = int(input('How far would you like to shift your encoded text? > '))
out_string = ''
for character in to_encode:
    #eliminate non-alphabet charaters
    if character in string.ascii_letters:
        out_string += character
for letter in out_string:
    letter = letter.lower() #lowercase all letters
    direction = user_letters.index(letter)
    direction += user_direction
    print(user_letters[direction % 26], end='') #modulus allows letters to loop around to the beginning of the alphabet
print()
