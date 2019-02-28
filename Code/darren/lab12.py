#lab12
#Guess the Number
import random
while True:
    trycounter = 0
    firstdiff = 0
    currentdiff = 0
    lastdiff = 0
    trydiff = 0
    # trycountdown = 10
    compynum = random.randint(1,10)
    print("I'm thinking of a number between 1 and 10. Try to guess the number within ten tries!")
    while True:
        usernum = input("Guess! >")
        usernum = int(usernum)
        if usernum == compynum:
            # trycountdown -= 1
            trycounter += 1
            print(compynum)
            print(f"You win! You guessed {trycounter} times.")
            break
        if usernum != compynum:
            trycounter += 1
            # trycountdown -= 1
            # if trycounter < 0:
            #     print(f"Sorry, the number was {compynum}. Better luck next time!")
            #     break
            # else:
                # print(f"Guess again! You have {trycountdown} tries left.")
            if trycounter is 1:
                previousguess = usernum
                firstdiff = abs(usernum - compynum)
                print(f"Guess again! You have guessed {trycounter} times.")
            if trycounter is 2:
                lastdiff = firstdiff
                currentdiff = abs(usernum - compynum)
                print(f"Guess again! You have guessed {trycounter} times. Previously, you guessed {previousguess}.")
                if currentdiff > firstdiff:
                    print(f"You are {abs(currentdiff-lastdiff)} further away than before.")
                if currentdiff < firstdiff:
                    print(f"You are {abs(currentdiff-lastdiff)} closer than before.")
                previousguess = usernum
                lastdiff = currentdiff
            if trycounter > 2:
                currentdiff = abs(usernum - compynum)
                print(f"Guess again! You have guessed {trycounter} times. Previously, you guessed {previousguess}.")
                if currentdiff > firstdiff:
                    print(f"You are {abs(currentdiff-lastdiff)} further away than before.")
                if currentdiff < firstdiff:
                    print(f"You are {abs(currentdiff-lastdiff)} closer than before.")
                previousguess = usernum
                lastdiff = currentdiff
            if usernum < compynum:
                print("You're too low.")
            if usernum > compynum:
                print("You're too high.")
    cont = input("Want to play again? >")
    if cont.lower() != 'yes':
        break
