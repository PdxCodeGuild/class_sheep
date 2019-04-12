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
print('Pick a number between 1 and 10.')
counter = 0 #count number of guesses
while True:
    user_input = int(input('answer >'))
    counter += 1
    if user_input == num1:
        print('You got it!')
        break
    elif user_input > num1:
        print('Too high!')
    elif user_input < num1:
        print('Too low!')
print (f'You guessed correctly in {counter} tries.')

# Version 4 (optional)
# Tell the user whether their current guess is closer than their last. This can be done by maintaining a variable containing the last guess outside the loop, then comparing the last guess to the current guess, and check if it's closer. Hint: you're interested in comparing the two absolute differences: abs(current_guess-target) and abs(last_guess-target).

num1 = random.randint(1, 10)
print('Pick a number between 1 and 10.')
counter = 0
first_guess = True # flag to break loop when user guesses correctly
while True:
    user_input = int(input('answer >'))
    counter += 1
    if user_input == num1:
        print('You got it!')
        break
    # first guess loop
    if first_guess == True:
        user_guess = abs(user_input-num1) # find distance between user guess and computer number
        print(f'You are {user_guess} away from the right answer.')
        old_guess = user_guess  # record the difference between the guess and the correct number to compare to next guess
        first_guess = False
    # loop after first guess is made
    else:
        user_guess = abs(user_input-num1)  # get next guess
        # if next guess is same distance as previous guess
        if user_guess == old_guess:
            print('Room temp.')
        # if next guess is less close than previous guess
        if user_guess > old_guess:
            print('Getting colder.')
        # if next guess is closer than previous guess
        if user_guess < old_guess:
            print('Getting warmer.')
        # record the difference between the guess and the correct number to compare to next guess
        old_guess = user_guess
