#Lab 12: Guess the Number
# version 1 & 3 ===============================================================

import random
number_of_guesses = 0

print("Guess a number between 1 and 20:")

number = random.randint(1, 20) #picks random number between 1 and 20
while number_of_guesses < 10:
    guess = input() #collect user input for each guess
    guess = int(guess) #convert user guess to integer

    number_of_guesses += 1 #adds one for each guess taken until it reaches 10 or the correct number is guessed

    if guess < number:
        print("Too low. Pick a bigger number.")
    if guess > number:
        print("Too high. Pick a smaller number.")
    if guess == number:
        print ("Correct, you won!")
        break
        print("Guess again: ")
else:
    print("You lost, goodbye!")


# version 2 ===================================================================

import random

number = random.randint(1, 20) #picks random number between 1 and 20
number_of_guesses = 0
print("Guess a number between 1 and 20:")

while True:
    guess = input() # collect user input for each guess
    guess = int(guess) # convert user guess to integer
    number_of_guesses = number_of_guesses + 1 #adds one for each guess taken until the correct number is guessed

    if guess < number:
        print('Too low! Pick a bigger number.')
    if guess > number:
        print("Too high! Pick a smaller number.")
    if guess == number:
        print(f"The correct number was {number}. You got the number in {number_of_guesses} guesses!")
        break
