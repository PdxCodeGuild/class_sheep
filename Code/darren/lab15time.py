#lab15time.py
#NumberToPhrase
ones = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
teens = {10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}
tens = {20: 'twenty', 30: 'thirty', 40: 'fourty', 50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety'}
while True:
    minstring = ''
    minoverflow = ''
    hourstring = ''
    hourplus = 0
    userhour = int(input("Please enter the number of hours. >"))
    usermin = int(input("please enter the number of minutes. >"))
    hourplus = usermin // 60
    usermin = usermin % 60
    if usermin < 10:
        minstring += ones[usermin]
    if usermin >= 10 and usermin < 20:
        minstring += teens[usermin]
    if usermin >= 20:
        min1 = usermin % 10
        min2 = usermin - min1
        minstring += tens[min2]+ ' '+ ones[min1]
    userhour += hourplus
    if userhour < 10:
        hourstring += ones[userhour]
    if userhour >= 10 and userhour < 20:
        hourstring += teens[userhour]
    if userhour >= 20:
        hou1 = userhour % 10
        hou2 = userhour - hou1
        hourstring += tens[hou2]+ ' '+ ones[hou1]
    print(f"Your total is {hourstring} hours and {minstring} minutes.")
    cont = input("Type anything to convert again or 'done' to quit. >")
    if cont.lower() == 'done':
        break
