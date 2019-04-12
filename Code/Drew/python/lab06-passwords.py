import string
import random

letters = list(string.ascii_letters)
numbers = list(string.digits)
special = list(string.punctuation)
charset = letters + numbers
num = int(input('How long should the password be?\n'))
specvar = int(input('How many special characters?\n'))
password = ''
for n in range(num-specvar):
    password += random.choice(charset)
for s in range(specvar):
    password += random.choice(special)
passlist = list(password)
random.shuffle(passlist)
password = ''.join(passlist)
print(password)
