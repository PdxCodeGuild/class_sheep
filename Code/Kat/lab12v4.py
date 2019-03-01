import random
import string
num1 = random.randint(1, 10)
print("Pick a number between 1 and 10.")
counter = 0
first_guess = True
while True:
    user_input = int(input("answer >"))
    counter = counter + 1
    if user_input == num1:
        print("You got it!")
        break
    if first_guess == True:
        user_guess = abs(user_input-num1)
        print(f"You are {user_guess} away from the right answer.")
        old_guess = user_guess
        first_guess = False
    else:
        user_guess2 = abs(user_input-num1)
        if user_guess2 > user_guess:
            print("Getting colder.")
        if user_guess2 < user_guess:
            print("Getting warmer.")
        user_guess2 = user_guess
    # user_input = int(input("answer >"))
    # if user_input == num1:
    #     print("You got it!")
    #     break
    # if user_guess != num1:
