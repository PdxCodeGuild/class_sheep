#lab3
#grading.py
number_grade = input("Please enter your total score. >")
number_grade = int(number_grade)
out_string = ''
if number_grade > 90:
    out_string = 'A'
elif number_grade <= 89 and number_grade >= 80:
    out_string = 'B'
elif number_grade <= 79 and number_grade >= 70:
    out_string = 'C'
elif number_grade <= 69 and number_grade >= 60:
    out_string = 'D'
elif number_grade < 59:
    out_string = 'F'
if number_grade % 10 > 7:
    out_string = out_string + '+'
if number_grade % 10 < 4:
    out_string = out_string + '-'
print(out_string)
