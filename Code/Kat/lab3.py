# Lab 3: Grading
# Let's convert a number grade to a letter grade, using if and elif statements and comparisons.
# INSTRUCTIONS
# 1. Have the user enter a number representing the grade (0-100)
# 2. Convert the number grade to a letter grade

grade = int(input('What grade did you get between 0 and 100?>'))
if 100 >= grade >= 90:
    # print('A')
    grade_letter = 'A'
elif grade >= 80:
    # print('B')
    grade_letter = 'B'
elif grade >= 70:
    # print('C')
    grade_letter = 'C'
elif grade >= 60:
    # print('D')
    grade_letter = 'D'
elif grade >= 0:
    # print('F')
    grade_letter = 'F'
# catahall for invalid entries
else:
    print('Please enter a number between 0 and 100.')

# Version 2
# INSTRUCTIONS: Find the specific letter grade (A+, B-, etc). You can check for more specific ranges using if statements, or use modulus % to get the ones-digit to set another string to '+', '-', or ' '. Then you can concatenate that string with your grade string.

def plus_or_minus(grade_letter):
    # assign + or - to all grades except F's
    if grade >=60:
        if grade % 10 >= 7:
    	       grade_letter = grade_letter + '+'
        if grade % 10 <= 3:
            grade_letter = grade_letter + '-'
    return grade_letter

print(plus_or_minus(grade_letter))
