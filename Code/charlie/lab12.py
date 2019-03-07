# lab12
# import random
# random_number = random.randint(1,10)
#
# user_guess_count = 0
# user_guess = int(input("Guess the number> "))
# user_guess_count += 1
# while user_guess != random_number:
#     # print("Try again")
#     # if user_guess_count > 10:
#     #     print("you've used all your guesses> ")
#     #     break
#     # elif user_guess_count <= 10:
#         user_guess = int(input("Guess the number> "))
#         user_guess_count += 1
#         while user_guess == random_number:
#            print(f"Correct! you guessed {user_guess_count} times")
#            break
#
# print(f"This is the random number, {random_number}")
# print(f"{random_number} this is the random number")
#
#V2-3

# import random
# random_number = random.randint(1,10)
# print(random_number)
#
# user_guess_count = 0
# user_guess = int(input("Guess the number> "))
# user_guess_count += 1
# while user_guess != random_number:
#     if user_guess > random_number:
#         user_guess = int(input("Your too High! Guess again or type 'done' if you're ready to give up.> "))
#         user_guess_count += 1
#         while user_guess == random_number:
#             print(f"Correct! you guessed {user_guess_count} times")
#             break
#     elif user_guess < random_number:
#         user_guess = int(input("Your too low! Guess again or type 'done' if you're ready to give up.> "))
#         user_guess_count += 1
#         while user_guess == random_number:
#             print(f"Correct! you guessed {user_guess_count} times")
#             break
#
#
#     elif user_guess == 'done':
#         break

#V4

import random
# random_number = random.randint(1,10)#ive selected a number between 1 and 10
# print(random_number)
#
# user_guess1 = int(input("Guess the number or type 'done' if you're ready to give up.> ")) #this is the first guess.
# first_guess_target = user_guess1 #this guess an integer that will become  first_guess_target
# absolute_last = abs(first_guess_target - random_number) #here we determine the absolute value of the first guess by comparing it to the random int.
# print(f"<<< {absolute_last} >>> This is how close the first guess was to the random integer.")
#
# while user_guess1 != random_number: #if the first guess is wrong, this is True, and will run.
#     user_guess2 = int(input("Guess again or type 'done' if you're ready to give up.> ")) #line 61 asks the question, what is your second guess.
#     if user_guess2 == 'done': #if the user selects done, the program exits
#         print("thanks")
#         break
#     if user_guess2 != random_number: # we will run the following loop, if the second guess does not equal the random integer.
#         absolute_current = abs(user_guess2 - random_number) #this is determining how close the second guess was to the integer.
#         print(f"<<< {absolute_current} >>> this is how close the second guess is to the random integer.")
#
#         if absolute_current > absolute_last:
#             print("Your getting further away")
#             user_guess1 = user_guess2
#
#         elif absolute_current < absolute_last:
#             print("Your getting closer")
#             user_guess1 = user_guess2
#
#
#     elif user_guess2 == random_number:
#         print('nice guess, You got it!')
#         break
#
#
#
# print("you got it")

#V5
user_selection = int(input("pick a number between 1 and 10000\n:"))

computer_selection = random.randint(0, 10000)
computer_count = 0
while computer_selection != user_selection:
    computer_selection = random.randint(0,10000)
    computer_count += 1
    if computer_selection == user_selection:
        print(f"Computer guess {computer_selection} and it matches user's pick {user_selection}")
        break
print(f"Computer tried {computer_count} times")
