# Lab 11: Simple Calculator
# Let's write a simple REPL (read evaluate print loop) calculator that can handle addition, subtraction, multiplication, and division. Ask the user for an operator and each operand. Don't forget that input returns a string, which you can convert to a float using float(user_input) where user_input is the string you got from input. Below is some sample input/output.

# Version 2
# Allow the user to keep performing operations until they say 'done'. Use while True and break. Below is some sample input/output.

import string
while True:
    user_input = input("What is the operation you'd like to perform (+, -, *, /)? Type done to exit.>")
    if user_input == 'done':
        print("Goodbye!")
        break
    user_num1 = float(input("What is the first number? >"))
    user_num2 = float(input("What is the second number? >"))
    if user_input == '+':
        print(user_num1+user_num2)
    elif user_input == '-':
        print(user_num1-user_num2)
    elif user_input == '*':
        print(user_num1*user_num2)
    elif user_input == '/':
        print(user_num1/user_num2)
