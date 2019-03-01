user_choice = input("What operation do you want to perform? + - * / ")
num1 = int(input("What is the first number? "))
num2 = int(input("What is the second number? "))

if user_choice == '+':
    print('{} + {} = '.format(num1, num2), (num1 + num2))

elif user_choice == '-':
    print('{} - {} = '.format(num1, num2), (num1 - num2))

elif user_choice == '*':
    print('{} * {} = '.format(num1, num2), (num1 * num2))

elif user_choice == '/':
    print('{} / {} = '.format(num1, num2), (num1 / num2))

else:
    print("Input not valid, please try again.")
