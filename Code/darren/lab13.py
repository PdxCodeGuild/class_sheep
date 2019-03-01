# turn_left_or_right.py
import string
result = ''
codelist = string.ascii_lowercase
userletter = input("Enter text to encript: >")
rotationdegree = int(input("Enter encription number: >"))
for letter in userletter:
    userindex = codelist.index(letter)
    if userindex < rotationdegree:
        encodedindex = userindex + rotationdegree
    else:
        encodedindex = (userindex + rotationdegree) % rotationdegree
    encodedletter = codelist[encodedindex]
    result += encodedletter
print(result)
