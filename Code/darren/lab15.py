#lab15
#NumberToPhrase
ones = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
teens = {10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}
tens = {20: 'twenty', 30: 'thirty', 40: 'fourty', 50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety'}
hundreds = {100: 'one hundred', 200: 'two hundred', 300: 'three hundred', 400: 'four hundred', 500: 'five hundred', 600: 'six hundred', 700: 'seven hundred', 800: 'eight hundred', 900: 'nine hundred'}
while True:
    out_string = ''
    user_num = int(input("Please enter your number in numeral form, between 0 to 999. >"))
    if user_num < 10:
        out_string += ones[user_num]
    if user_num >= 10 and user_num < 20:
        out_string += teens[user_num]
    if user_num >= 20 and user_num < 100:
        digit2 = user_num % 10
        digit1 = user_num - digit2
        out_string += tens[digit1] + ' ' + ones[digit2]
    if user_num >= 100:
        digit3 = user_num % 10
        digit2 = (user_num % 100) - digit3
        digit1 = (user_num - digit2) - digit3
        if digit2 == 0 and digit3 == 0:
            out_string += hundreds[digit1]
        if digit2 == 0 and digit3 != 0:
            out_string += hundreds[digit1]+ ' and ' + ones[digit3]
        if digit2 != 0 and digit3 == 0:
            out_string += hundreds[digit1]+ ' and ' + tens[digit2]
        if digit2 != 0 and digit3 != 0:
            out_string += hundreds[digit1]+ ' and ' + tens[digit2] + ' ' + ones[digit3]
    print(f'Your number is {out_string}.')
    cont = input("Type anything to convert again or 'done' to quit. >")
    if cont.lower() == 'done':
        break
