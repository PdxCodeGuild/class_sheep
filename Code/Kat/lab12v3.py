import random
import string
num1 = random.randint(1, 10)
print("Pick a number between 1 and 10.")
counter = 0
while True:
    user_input = input("answer >")
    user_input = int(user_input)
    counter = counter + 1
    if user_input == num1:
        print("You got it!")
        break
    elif user_input > num1:
        print("Too high!")
    elif user_input < num1:
        print("Too low!")
print (f"You guessed correctly in {counter} tries.")
