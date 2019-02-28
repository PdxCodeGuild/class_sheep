import string
while True:
    user_op = input("What is the operation you'd like to perform (+, -, *, /)? Press done to exit.>")
    if user_op == 'done':
        print("Goodbye!")
        break
    else:
        user_num1 = float(input("What is the first number? >"))
        user_num2 = float(input("What is the second number? >"))
        if user_op == '+':
            print(user_num1+user_num2)
        elif user_op == '-':
            print(user_num1-user_num2)
        elif user_op == '*':
            print(user_num1*user_num2)
        elif user_op == '/':
            print(user_num1/user_num2)
