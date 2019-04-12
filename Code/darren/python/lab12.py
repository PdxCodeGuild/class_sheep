#lab12.py
'''Guess the Number'''

import random

while True:
    attempt_counter = 0
    first_diff = 0
    current_diff = 0
    last_diff = 0
    # attempt_countdown = 10
    compy_num = random.randint(1,10)
    print("I'm thinking of a number between 1 and 10. Try to guess the number within ten tries!")
    while True:
        user_num = input("Guess! >")
        user_num = int(user_num)
        if user_num == compy_num:
            # attempt_countdown -= 1
            attempt_counter += 1
            print(compy_num)
            print(f"You win! You guessed {attempt_counter} times.")
            break
        if user_num != compy_num:
            attempt_counter += 1
            # attempt_countdown -= 1
            # if attempt_counter < 0:
            #     print(f"Sorry, the number was {compy_num}. Better luck next time!")
            #     break
            # else:
                # print(f"Guess again! You have {attempt_countdown} tries left.")
            if attempt_counter == 1:
                prev_guess = user_num
                first_diff = abs(user_num - compy_num)
                print(f"Guess again! You have guessed {attempt_counter} times.")
            if attempt_counter == 2:
                last_diff = first_diff
                current_diff = abs(user_num - compy_num)
                print(f"Guess again! You have guessed {attempt_counter} times. Previously, you guessed {prev_guess}.")
                if current_diff > first_diff:
                    print(f"You are {abs(current_diff-last_diff)} further away than before.")
                if current_diff < first_diff:
                    print(f"You are {abs(current_diff-last_diff)} closer than before.")
                prev_guess = user_num
                last_diff = current_diff
            if attempt_counter > 2:
                current_diff = abs(user_num - compy_num)
                print(f"Guess again! You have guessed {attempt_counter} times. Previously, you guessed {prev_guess}.")
                if current_diff > first_diff:
                    print(f"You are {abs(current_diff-last_diff)} further away than before.")
                if current_diff < first_diff:
                    print(f"You are {abs(current_diff-last_diff)} closer than before.")
                prev_guess = user_num
                last_diff = current_diff
            if user_num < compy_num:
                print("You're too low.")
            if user_num > compy_num:
                print("You're too high.")
    cont = input("Want to play again? >")
    if cont.lower() != 'yes':
        break
