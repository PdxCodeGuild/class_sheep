# Lab 12: Guess the Number
# Let's play 'Guess the Number'. The computer will guess a random int between 1 and 10. The user will then try to guess the number, and the program will tell them whether they're right or wrong.

import random
import string

# Version 1
# Using a while loop, allow the user to guess 10 times. If they fail to guess the number after 10 tries, the user is told they've lost. If the user guesses the number, the user is told they've won and the game exits.
# Version 2
# Allow the user to make an unlimited number of guesses using a while True and break. Keep track of how many guesses the user has made, and tell them at the end.
# Version 3
# Tell the user whether their guess is above ('too high!') or below ('too low!') the target value.

num1 = random.randint(1, 10)
print("Pick a number between 1 and 10.")
counter = 0
while True:
    user_input = int(input("answer >"))
    counter += 1
    if user_input == num1:
        print("You got it!")
        break

    if user_input > num1:
        print("Too high!")
    elif user_input < num1:
        print("Too low!")
print (f"You guessed correctly in {counter} tries.")

# Version 4 (optional)
# Tell the user whether their current guess is closer than their last. This can be done by maintaining a variable containing the last guess outside the loop, then comparing the last guess to the current guess, and check if it's closer. Hint: you're interested in comparing the two absolute differences: abs(current_guess-target) and abs(last_guess-target).

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
