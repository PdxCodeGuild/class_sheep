#lab12reverse.py
#Guess The Number Reverse
import random
while True:
    attempt_counter = 0
    attempt_list = []
    input("This time I will try to guess the number you're thinking of. Please select a number between 1 and 10. Enter anything when ready!. >")
    while True:
        compy_guess = random.randint(1,10)
        if compy_guess in attempt_list:
            compy_guess = random.randint(1,10)
        if compy_guess not in attempt_list:
            attempt_counter += 1
            guess = input(f"Is it {compy_guess}? Y/N >")
            if guess.lower() == 'y':
                attempt_list.append(compy_guess)
                print("I win! I'm smarter than a human.")
                break
            if guess.lower() == 'n' and attempt_counter <=9:
                attempt_list.append(compy_guess)
                print("Really? Hmm.")
            if guess.lower() == 'n' and attempt_counter ==9:
                attempt_list.append(compy_guess)
                print("Drat, I was outsmarted by a human!")
                break
    print(f"I guessed {attempt_list}.")
    cont = input("Want to play again? >")
    if cont.lower() != 'yes':
        break
