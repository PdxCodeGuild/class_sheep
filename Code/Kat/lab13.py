#ROT 13 version 2
import string
user_letters = list(string.ascii_lowercase)
to_encode = input("Type a word that you would like to encode >")
user_direction = int(input("How far would you like to shift your encoded text? >"))
out_string = ''
for character in to_encode:
    if character in string.ascii_letters:
        out_string += character
    else:
        out_string += ''
for letter in out_string:
    letter = letter.lower()
    direction = user_letters.index(letter)
    direction += user_direction
    print(user_letters[direction % 26], end='')
print()
