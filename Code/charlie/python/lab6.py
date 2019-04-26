import random

import string

abc_list = list(string.ascii_lowercase)
ABC_list = list(string.ascii_uppercase)
special_list = list(string.punctuation)
number_list = list(string.digits)
# length = len(abc_list)
length_of_abc = int(input('Select how many lowercase letter you\'d like > '))

length_of_ABC = int(input('Select how many uppercase letters you\'d like> '))

length_of_special = int(input('Select how many special characters you\'d like> '))

length_of_number = int(input('Select how many numbers you\'d like> '))


# length_of_password = random.randint(5,length)
#length_of_password = 10
# print(length_of_password)
abc = ''
while len(abc) < length_of_abc:
    abc += random.choice(abc_list)

ABC = ''
while len(ABC) < length_of_ABC:
    ABC += random.choice(ABC_list)

special = ''
while len(special) < length_of_special:
    special += random.choice(special_list)

number = ''
while len(number) < length_of_number:
    number += random.choice(number_list)

password_characters = abc+ABC+special+number

print(password_characters)
