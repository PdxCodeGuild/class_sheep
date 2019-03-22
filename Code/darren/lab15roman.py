#lab15roman.py
'''Number to Phrase (Numeris Romanis)'''

ones = {0: '', 1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX'}
tens = {0: '', 10: 'X', 20: 'XX', 30: 'XXX', 40: 'XL', 50: 'L', 60: 'LX', 70: 'LXX', 80: 'LXXX', 90: 'XC'}
hundreds = {0: '', 100: 'C', 200: 'CC', 300: 'CCC', 400: 'CD', 500: 'D', 600: 'DC', 700: 'DCC', 800: 'DCCC', 900: 'CM'}
while True:
    out_string = ''
    user_num = input("Please enter your number in numeral form, between 0 to 999. Enter 'linquo' to stop. >")
    if user_num == 'linquo':
        break
    else:
        user_num = int(user_num)
        if user_num < 10:
            out_string += ones[user_num]
        if user_num >= 10 and user_num < 100:
            digit1 = user_num % 10
            digit2 = user_num - digit1
            out_string += tens[digit2] + ones[digit1]
        if user_num >= 100:
            digit1 = (user_num % 100) % 10
            digit2 = (user_num % 100) - digit1
            digit3 = (user_num - digit2) - digit1
            out_string += hundreds[digit3]+ tens[digit2]+ ones[digit1]

    print(f"When in Rome, do as Romans do. {user_num} is {out_string}!")
