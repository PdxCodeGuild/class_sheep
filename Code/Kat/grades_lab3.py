grade = input('What grade did you get between 0 and 100?>')
grade = int(grade)
if 100 >= grade >= 90:
    print('A')
elif 89 >= grade >= 80:
    print('B')
elif 79 >= grade >= 70:
    print('C')
elif 69 >= grade >= 60:
    print('D')
elif 59 >= grade >= 0:
    print('F')
else:
    print('Please enter a number between 0 and 100.')
