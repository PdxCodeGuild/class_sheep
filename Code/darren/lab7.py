#lab7.py
#RPS Game
import random
rpslist = ['rock','paper','scissors', 'lizard', 'spock']
while True:
    userhand = ''
    compyhand = ''
    userhand = input("I challenge you to Rock, Paper, Scissors... Lizard, Spock! Go! >")
    compyhand = random.choice(rpslist)
    if userhand.lower() not in rpslist:
        print("That's not a real hand! Cheater!")
    if userhand.lower() == 'rock':
        if compyhand == 'paper':
            print("Paper covers rock.")
            print("I win!")
        if compyhand == 'spock':
            print("Spock vaporizes rock.")
            print("I win!")
        if compyhand == 'scissors':
            print("Rock crushes scissors.")
            print("You win...")
        if compyhand == 'lizard':
            print("Rock smashes lizard")
            print("You win...")
    if userhand.lower() == 'paper':
        if compyhand == 'scissors':
            print("Scissors cut paper.")
            print("I win!")
        if compyhand == 'lizard':
            print("Lizard eats paper.")
            print("I win!")
        if compyhand == 'rock':
            print("Paper covers rock.")
            print("You win...")
        if compyhand == 'spock':
            print("Paper disproves Spock.")
            print("You win...")
    if userhand.lower() == 'scissors':
        if compyhand == 'rock':
            print("Rock crushes scissors.")
            print("I win!")
        if compyhand == 'spock':
            print("Spock smashes scissors.")
            print("I win!")
        if compyhand == 'paper':
            print("Scissors cut paper.")
            print("You win...")
        if compyhand == 'lizard':
            print("Scissors decapitate lizard.")
            print("You win...")
    if userhand.lower() == 'lizard':
        if compyhand == 'rock':
            print("Rock smashes lizard.")
            print("I win!")
        if compyhand == 'scissors':
            print("Scissors decapitate lizard.")
            print("I win!")
        if compyhand == 'paper':
            print("Lizard eats paper.")
            print("You win...")
        if compyhand == 'spock':
            print("Lizard poisons Spock.")
            print("You win...")
    if userhand.lower() == 'spock':
        if compyhand == 'lizard':
            print("Lizard poisons Spock.")
            print("I win!")
        if compyhand == 'paper':
            print("Paper disproves Spock.")
            print("I win!")
        if compyhand == 'rock':
            print("Spock vaporizes rock.")
            print("You win...")
        if compyhand == 'scissors':
            print("Spock smashes scissors.")
            print("You win...")
    if userhand.lower() == compyhand:
        print(compyhand)
        print("A tie?")
    cont = input("Want to play again? >")
    if cont.lower() != 'yes':
        break
