#lab15roman.py
#NumberToPhrase
ones = {0: '', 1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX'}
tens = {0: '', 10: 'X', 20: 'XX', 30: 'XXX', 40: 'XL', 50: 'L', 60: 'LX', 70: 'LXX', 80: 'LXXX', 90: 'XC'}
hundreds = {0: '', 100: 'C', 200: 'CC', 300: 'CCC', 400: 'CD', 500: 'D', 600: 'DC', 700: 'DCC', 800: 'DCCC', 900: 'CM'}
while True:
    outstring = ''
    usernum = int(input("Please enter your number in numeral form, between 0 to 999. >"))
    if usernum < 10:
        outstring += ones[usernum]
    if usernum >= 10 and usernum < 100:
        digit1 = usernum % 10
        digit2 = usernum - digit1
        outstring += tens[digit2]+ ones[digit1]
    if usernum >= 100:
        digit1 = (usernum % 100) % 10
        digit2 = (usernum % 100) - digit1
        digit3 = (usernum - digit2) - digit1
        outstring += hundreds[digit3]+ tens[digit2]+ ones[digit1]
    print(f"{usernum} is {outstring} in Rome!")
