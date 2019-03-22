# Lab 15: Number to Phrase
# Convert a given number into its english representation. For example: 67 becomes 'sixty-seven'. Handle numbers from 0-99.

user_input = int(input("Enter a number between 0 and 99 >"))
ones_dictionary = {0: '', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
teens_dictionary = {10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}
tens_dictionary = {2: 'twenty ', 3: 'thirty ', 4: 'forty ', 5: 'fifty ', 6: 'sixty ', 7: 'seventy ', 8: 'eighty ', 9: 'ninty '}

if user_input == 0:
    print("zero")
tens_digit = user_input // 10
ones_digit = user_input % 10
if tens_digit == 0:
    out_number = ones_dictionary[user_input]
    print(out_number)
if tens_digit == 1:
    out_number = teens_dictionary[user_input]
    print(out_number)
if tens_digit >= 2:
    out_number = tens_dictionary[tens_digit] + ones_dictionary[ones_digit]
    print(out_number)




# Alternate version 2 using functions and taking in numbers 1-999.
def hundreds(in_num):
    if user_input > 100:
        return f"{ones_dictionary[in_num]} hundred "

def tens(in_num):
    if in_num == 0:
        return 'one hundred'
    elif in_num < 10:
        return f"{ones_dictionary[in_num]}"
    elif in_num < 20:
        return f"{teens_dictionary[in_num]}"
    elif in_num >= 20:
        return f"{tens_dictionary[in_num // 10]}{ones_dictionary[in_num % 10]}"

def ones(in_num):
    return f"{ones_dictionary_functions[in_num]}"

def number(full_num):
    if user_input > 100:
        return hundreds(full_num // 100) + tens(full_num % 100)
    elif user_input >= 10:
        return tens(full_num % 100)
    elif user_input >= 0:
        return ones(full_num)

user_input = int(input("Enter a number between 0 and 999 >"))

if user_input == 0:
    print("zero")
else:
    print(number(user_input))
