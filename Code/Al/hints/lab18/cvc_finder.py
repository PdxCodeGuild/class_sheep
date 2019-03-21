# cvc_finder.py
import string
input_string = 'abcadeemonqrs'
vowel_string = 'aoeuiy'
consonant_string = ''
for letter in string.ascii_lowercase:
    if letter not in vowel_string:
        consonant_string += letter

for index in range(1, len(input_string) - 1):
    if input_string[index] in vowel_string and input_string[index - 1] in consonant_string and input_string[index + 1] in consonant_string:
        print(index, input_string[index-1:index+2])