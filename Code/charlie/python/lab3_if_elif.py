user_grade = int(input("what grade did you recieve?"))

modulus = user_grade % 10
if modulus >= 0 and modulus <= 3:
    operator = '-'
elif modulus >= 4 and modulus <= 6:
    operator = ' '
elif modulus >= 7 and modulus <= 10:
    operator = '+'

if user_grade >= 0 and user_grade <= 59:
    print(f"F{operator}")
elif user_grade >= 60 and user_grade <= 69:
    print(f"D{operator}")
elif user_grade >= 70 and user_grade <= 79:
    print(f"C{operator}")
elif user_grade >= 80 and user_grade <= 89:
    print(f"B{operator}")
elif user_grade >= 90 and user_grade <= 100:
    print(f"A{operator}")
else:
    print("Not a valid grade, please select a number between 0 and 100")
