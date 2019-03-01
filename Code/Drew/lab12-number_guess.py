import random

comp_choice = random.randint(1, 100)
guess = input("Pick a number between 1 and 100:\n")
guess = int(guess)
guess_times = 0
while guess_times < 10:
    if guess_times == 0:
        if guess == comp_choice:
            print(f"I picked {comp_choice}, you guessed right!")
            break
        elif guess > comp_choice:
            guess_times = guess_times + 1
            print(f"Too high. You have {10-guess_times} guesses left.")
            old_guess = guess
            guess = input("Pick another number:\n")
            guess = int(guess)
        elif guess < comp_choice:
            guess_times = guess_times + 1
            print(f"Too low. You have {10-guess_times} guesses left.")
            old_guess = guess
            guess = input("Pick another number:\n")
            guess = int(guess)
    else:
        if guess == comp_choice:
            print(f"I picked {comp_choice}, you guessed right!")
            break
        elif guess > comp_choice:
            guess_times = guess_times + 1
            print(f"Too high. You have {10-guess_times} guesses left.")
            diff = abs(guess - comp_choice)
            old_diff = abs(old_guess - comp_choice)
            if diff > old_diff:
                print("Your last guess was closer")
            else:
                print("That guess was closer than your last.")
            old_guess = guess
            guess = input("Pick another number:\n")
            guess = int(guess)
        elif guess < comp_choice:
            guess_times = guess_times + 1
            print(f"Too low. You have {10-guess_times} guesses left.")
            diff = abs(guess - comp_choice)
            old_diff = abs(old_guess - comp_choice)
            if diff > old_diff:
                print("Your last guess was closer")
            else:
                print("That guess was closer than your last.")
            old_gess = guess
            guess = input("Pick another number:\n")
            guess = int(guess)
if guess_times == 10:
    print(f"Sorry, you're out of guesses. My number was {comp_choice}.")
