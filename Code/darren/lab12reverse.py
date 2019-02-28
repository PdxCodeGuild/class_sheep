#lab12reverse.py
#Guess The Number Reverse
import random
while True:
    trycounter = 0
    attemptlist = []
    input("This time I will try to guess the number you're thinking of. Please select a number between 1 and 10. Enter anything when ready!. >")
    while True:
        compyguess = random.randint(1,10)
        if compyguess in attemptlist:
            compyguess = random.randint(1,10)
        if compyguess not in attemptlist:
            trycounter += 1
            guess = input(f"Is it {compyguess}? Y/N >")
            if guess.lower() == 'y':
                attemptlist.append(compyguess)
                print("I win! I'm smarter than a human.")
                break
            if guess.lower() == 'n' and trycounter <=9:
                attemptlist.append(compyguess)
                print("Really? Hmm.")
            if guess.lower() == 'n' and trycounter ==9:
                attemptlist.append(compyguess)
                print("Drat, I was outsmarted by a human!")
                break
    print(f"I guessed {attemptlist}.")
    cont = input("Want to play again? >")
    if cont.lower() != 'yes':
        break
