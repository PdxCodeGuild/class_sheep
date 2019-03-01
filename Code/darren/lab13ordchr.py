#lab13ordchr.py
#ROT Cipher with ord and chr
import string
result = ''
userstring = input("Enter text to encript: >")
userstring = userstring.lower()
rotationdegree = int(input("Enter encription number: >"))
for letter in userstring:
    if letter == ' ':
        result += letter
    else:
        userdex = ord(letter)
        if userdex > 97:
            basedex = userdex % 97
        else:
            basedex = abs(userdex - 97)
        if basedex < rotationdegree:
            codedex = basedex + rotationdegree
        else:
            codedex = (basedex + rotationdegree) % rotationdegree
        codeletter = chr(codedex + 97)
        result += codeletter
print(result)
