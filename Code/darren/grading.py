#grading.py
numbergrade = input("Please enter your total score. >")
numbergrade = int(numbergrade)
outstring = ''
if numbergrade > 90:
    outstring = 'A'
elif numbergrade <= 89 and numbergrade >= 80:
    outstring = 'B'
elif numbergrade <= 79 and numbergrade >= 70:
    outstring = 'C'
elif numbergrade <= 69 and numbergrade >= 60:
    outstring = 'D'
elif numbergrade < 59:
    outstring = 'F'
if numbergrade % 10 > 7:
    outstring = outstring + '+'
if numbergrade % 10 < 4:
    outstring = outstring + '-'
print(outstring)
