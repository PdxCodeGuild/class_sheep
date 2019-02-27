word_to_number = {'one' : 1, 'two': 2, 'three': 3, 'four': 4}
num1 = input("Write the first number >")
num2 = input("Write the second number >")
out_num = word_to_number[num1] + word_to_number[num2]
print(f"{num1} + {num2} = {out_num}")
