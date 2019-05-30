#grading.py

# Input user's grade
user_grade = input('Enter your grade (0-100):\n')
grade = int(user_grade)
if grade >= 90 and grade <=100:
    letter_grade = 'A'
elif grade >= 80 and grade <= 89:
    letter_grade ='B'
elif grade >= 70 and grade <=79:
    letter_grade ='C'
elif grade >= 60 and grade <=69:
    letter_grade ='D'
elif grade >= 0 and grade <=59:
    letter_grade ='F'

# Set + or - if grade is not F
grade2 = grade%10
if letter_grade != 'F':
    if grade2 >= 7 and grade2 <= 10:
        qualifier = '+'
    elif grade2 >= 4 and grade2 <= 6:
        qualifier = ''
    elif grade2 >= 0 and grade2 <= 3:
        qualifier = '-'
    print(letter_grade + qualifier)
else:
    print(letter_grade)

