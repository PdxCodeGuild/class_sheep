user_grade = input("what grade did you recieve?")
user_grade = int(user_grade)

modulus = user_grade%10
if modulus >=0 and modulus <=3:
    modulus1 = '-'
elif modulus >=4 and modulus <=6:
    modulus1 = ' '
elif modulus >=7 and modulus <=10:
    modulus1 = '+'

if user_grade >=0 and user_grade <= 59:
    print(f"F{modulus1}")
elif user_grade >=60 and user_grade <=69:
    print(f"D{modulus1}")
elif user_grade >=70 and user_grade <=79:
    print(f"C{modulus1}")
elif user_grade >=80 and user_grade <=89:
    print(f"B{modulus1}")
elif user_grade >=90 and user_grade <=100:
    print(f"A{modulus1}")
else:
    print("Not a valid grade, please select a number between 0 and 100")
