ones_dictionary = {0: '', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
teens_dictionary = {10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}
tens_dictionary = {2: 'twenty ', 3: 'thirty ', 4: 'forty ', 5: 'fifty ', 6: 'sixty ', 7: 'seventy ', 8: 'eighty ', 9: 'ninty '}

def hundreds(in_num):
    if user_input > 100:
        return f"{ones_dictionary[in_num]} hundred"

def tens(in_num):
    # if in_num == 1:
    #     return f"{teens_dictionary[in_num]}"
    # if in_num >= 2:
    #     return f"{tens_dictionary[in_num]}"
    if in_num == 0:
        return ''

def ones(in_num):
    return f"{ones_dictionary[in_num]}"

def number(full_num):
    return hundreds(full_num // 100) + tens((full_num % 100) // 10) + ones(full_num % 10)

user_input = int(input("Enter a number between 0 and 999 >"))

print(number(user_input))
