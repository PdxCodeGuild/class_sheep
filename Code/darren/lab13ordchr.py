#lab13ordchr.py
#ROT Cipher with ord and chr
import string
result = ''
user_string = input("Enter text to encript: >")
user_string = user_string.lower()
rotation_degree = int(input("Enter encription number: >"))
for letter in user_string:
    if letter == ' ':
        result += letter
    else:
        base_dex = ord(letter) - 97
        # if user_dex > 97:
        #     base_dex = user_dex % 97
        # else:
        #     base_dex = abs(user_dex - 97)
        if base_dex < rotation_degree:
            code_dex = base_dex + rotation_degree
        else:
            code_dex = (base_dex + rotation_degree) % rotation_degree
        code_letter = chr(code_dex + 97)
        result += code_letter
print(result)
