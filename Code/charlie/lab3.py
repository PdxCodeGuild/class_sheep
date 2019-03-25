#I replaced the if/elif with a for loop using a tuple list.

user_grade = int(input("what grade did you recieve?"))

modulus = user_grade % 10
if modulus >= 0 and modulus <= 3:
    operator = '-'
elif modulus >= 4 and modulus <= 6:
    operator = ' '
elif modulus >= 7 and modulus <= 10:
    operator = '+'

grades = [(59, 'F'), (69, 'D'), (79, 'C'), (89, 'B'), (100, 'A')]

for i in range(len(grades)):
    if grades[i][0] >= user_grade:
        print(f"Your letter grade is {grades[i][1]}{operator}")
        break
