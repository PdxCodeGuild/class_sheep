#lab13.py
#ROT Cypher
import string
result = ''
codelist = string.ascii_lowercase
userstring = input("Enter text to encript: >")
userstring = userstring.lower()
rotationdegree = int(input("Enter encription number: >"))
for letter in userstring:
    if letter == ' ':
        result += letter
    else:
        userindex = codelist.index(letter)
        if userindex < rotationdegree:
            encodedindex = userindex + rotationdegree
        else:
            encodedindex = (userindex + rotationdegree) % rotationdegree
    encodedletter = codelist[encodedindex]
    result += encodedletter
print(result)
