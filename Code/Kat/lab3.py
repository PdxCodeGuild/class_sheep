grade = int(input('What grade did you get between 0 and 100?>'))
if 100 >= grade >= 90:
    # print('A')
    grade_letter = 'A'
elif 89 >= grade >= 80:
    # print('B')
    grade_letter = 'B'
elif 79 >= grade >= 70:
    # print('C')
    grade_letter = 'C'
elif 69 >= grade >= 60:
    # print('D')
    grade_letter = 'D'
elif 59 >= grade >= 0:
    # print('F')
    grade_letter = 'F'
else:
    print('Please enter a number between 0 and 100.')
if grade % 10 >= 7:
	grade_letter = grade_letter + '+'
if grade % 10 <= 3:
    grade_letter = grade_letter + '-'
print(grade_letter)
