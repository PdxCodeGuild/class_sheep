import string
import random

letters = list(string.ascii_letters)
numbers = list(string.digits)
special = list(string.punctuation)
charset = letters + numbers + special
num = int(input('How long should the password be?\n'))
password = ''
for n in range(num):
    password += random.choice(charset)
print(password)
