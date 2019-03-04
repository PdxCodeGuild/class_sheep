#lab15
#NumberToPhrase
ones = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
teens = {10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}
tens = {20: 'twenty', 30: 'thirty', 40: 'fourty', 50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety'}
hundreds = {100: 'one hundred', 200: 'two hundred', 300: 'three hundred', 400: 'four hundred', 500: 'five hundred', 600: 'six hundred', 700: 'seven hundred', 800: 'eight hundred', 900: 'nine hundred'}
while True:
    outstring = ''
    usernum = int(input("Please enter your number in numeral form, between 0 to 99. >"))
    if usernum < 10:
        outstring += ones[usernum]
    if usernum >= 10 and usernum < 20:
        outstring += teens[usernum]
    if usernum >= 20 and usernum < 100:
        digit2 = usernum % 10
        digit1 = usernum - digit2
        outstring += tens[digit1] + ' ' + ones[digit2]
    if usernum >= 100:
        digit3 = usernum % 10
        digit2 = (usernum % 100) - digit3
        digit1 = (usernum - digit2) - digit3
        if digit2 == 0 and digit3 == 0:
            outstring += hundreds[digit1]
        if digit2 == 0 and digit3 != 0:
            outstring += hundreds[digit1]+ ' and ' + ones[digit3]
        if digit2 != 0 and digit3 == 0:
            outstring += hundreds[digit1]+ ' and ' + tens[digit2]
        if digit2 != 0 and digit3 != 0:
            outstring += hundreds[digit1]+ ' and ' + tens[digit2] + ' ' + ones[digit3]
    print(f'Your number is {outstring}.')
    cont = input("Type anything to convert again or 'done' to quit. >")
    if cont.lower() == 'done':
        break
