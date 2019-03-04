user_input = int(input("Enter a number between 0 and 99 >"))
ones_dictionary = {0: '', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
if user_input == 0:
    print("zero)")
tens_digit = user_input//10
ones_digit = user_input%10
if tens_digit == 0:
    out_number = ones_dictionary[user_input]
    print(out_number)
if tens_digit == 1:
    teen_dictionary = {10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}
    out_number = teen_dictionary[user_input]
    print(out_number)
if tens_digit >= 2:
    tens_dictionary = {2: 'twenty ', 3: 'thirty ', 4: 'forty ', 5: 'fifty ', 6: 'sixty ', 7: 'seventy ', 8: 'eighty ', 9: 'ninty '}
    out_number = tens_dictionary[tens_digit] + ones_dictionary[ones_digit]
    print(out_number)
