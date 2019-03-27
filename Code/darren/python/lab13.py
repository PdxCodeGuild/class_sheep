#lab13.py
'''ROT 13 Cipher'''

import string

result = ''
code_list = string.ascii_lowercase
user_string = input("Enter text to encript: >")
user_string = user_string.lower()
rotation_degree = int(input("Enter encription number: >"))
for letter in user_string:
    if letter == ' ':
        result += letter
    else:
        user_index = code_list.index(letter)
        if user_index < rotation_degree:
            encoded_index = user_index + rotation_degree
        else:
            encoded_index = (user_index + rotation_degree) % rotation_degree
    encoded_letter = code_list[encoded_index]
    result += encoded_letter
print(result)
