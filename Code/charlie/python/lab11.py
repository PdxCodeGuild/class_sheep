#lab11.py
import math
import string
import operator


operators_list = ['+', '-', '*','/','//','%','**']
ops = { "+": operator.add, "-": operator.sub, "*": operator.mul,  "/": operator.truediv}


while True:
    operator = input("What is the first operation you'd like to perform? ")
    if operator == 'done':
        break
    if operator in (operators_list):
        # print(operators_list)
        first_num = float(input("What is the first number?" ))
        second_num = float(input("what is the second number?" ))
        output = (ops[operator](first_num,second_num))
        print(f"{first_num} {(operator)} {second_num} = {output}")
    else:
        output = input("must choose from this list: '+','-','*','/'")
        first_num = float(input("What is the first number?" ))
        second_num = float(input("what is the second number?" ))
        output = (ops[operator](first_num,second_num))
        print(f"{first_num} {(operator)} {second_num} = {output}")
