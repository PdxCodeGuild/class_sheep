#lab15time.py
#NumberToPhrase
ones = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
teens = {10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}
tens = {20: 'twenty', 30: 'thirty', 40: 'fourty', 50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety'}
while True:
    min_string = ''
    hour_string = ''
    hour_plus = 0
    user_hour = int(input("Please enter the number of hours. >"))
    user_min = int(input("please enter the number of minutes. >"))
    hour_plus = user_min // 60
    user_min = user_min % 60
    if user_min < 10:
        min_string += ones[user_min]
    if user_min >= 10 and user_min < 20:
        min_string += teens[user_min]
    if user_min >= 20:
        min1 = user_min % 10
        min2 = user_min - min1
        min_string += tens[min2]+ ' '+ ones[min1]
    user_hour += hour_plus
    if user_hour < 10:
        hour_string += ones[user_hour]
    if user_hour >= 10 and user_hour < 20:
        hour_string += teens[user_hour]
    if user_hour >= 20:
        hou1 = user_hour % 10
        hou2 = user_hour - hou1
        hour_string += tens[hou2]+ ' '+ ones[hou1]
    print(f"Your total is {hour_string} hours and {min_string} minutes.")
    cont = input("Type anything to convert again or 'done' to quit. >")
    if cont.lower() == 'done':
        break
