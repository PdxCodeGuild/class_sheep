#written_addition.py
'''
The purpose of this program: to allow the users to type it written words, and then tell them what the written words add up to.
'''
word_to_number = {'one': 1, 'two': 2, 'three': 3, 'four': 4}
num1 = input("Write the first number >")
while num1 not in word_to_number.keys():
    num1 = input("Write the first number >")
num2 = input("Write the second number >")
out_num = word_to_number[num1] + word_to_number[num2]
print(f"{num1} + {num2} = {out_num}")
