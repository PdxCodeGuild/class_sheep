#Lab 11: Simple Calculator, version 1

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


#version 2
# calculate_again = True
# while calculate_again: #while calculate again = True
#
#     user_choice = input("What operation do you want to perform? + - * /\n ")
#
#     num1 = int(input("What is the first number? "))
#     num2 = int(input("What is the second number? "))
#
#     if user_choice == '+':
#         print('{} + {} = '.format(num1, num2), (num1 + num2))
#
#     elif user_choice == '-':
#         print('{} - {} = '.format(num1, num2), (num1 - num2))
#
#     elif user_choice == '*':
#         print('{} * {} = '.format(num1, num2), (num1 * num2))
#
#     elif user_choice == '/':
#         print('{} / {} = '.format(num1, num2), (num1 / num2))
#
#
#     again = input("Would you like to make another calculation? yes or done:  ").lower()
#     if again == 'done':
#         play = False
#         print('Goodbye!')
#         break
