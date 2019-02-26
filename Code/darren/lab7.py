#lab7.py
#RPS Game
import random
rpslist = ['rock','paper','scissors', 'lizard', 'spock']
while True:
    userhand = ''
    compyhand = ''
    userhand = input("I challenge you to Rock, Paper, Scissors... Lizard, Spock! Go! >")
    compyhand = random.choice(rpslist)
    if userhand.lower() != 'rock' and userhand.lower() != 'paper' and userhand.lower() != 'scissors' and userhand.lower() != 'lizard' and userhand.lower() != 'spock':
        print("That's not a real hand! Cheater!")
    if userhand.lower() == 'rock' and compyhand == 'paper':
        print("Paper covers rock.")
        print("I win!")
    if userhand.lower() == 'rock' and compyhand == 'spock':
        print("Spock vaporizes rock.")
        print("I win!")
    if userhand.lower() == 'rock' and compyhand == 'scissors':
        print("Rock crushes scissors.")
        print("You win...")
    if userhand.lower() == 'rock' and compyhand == 'lizard':
        print("Rock smashes lizard")
        print("You win...")
    if userhand.lower() == 'paper' and compyhand == 'scissors':
        print("Scissors cut paper.")
        print("I win!")
    if userhand.lower() == 'paper' and compyhand == 'lizard':
        print("Lizard eats paper.")
        print("I win!")
    if userhand.lower() == 'paper' and compyhand == 'rock':
        print("Paper covers rock.")
        print("You win...")
    if userhand.lower() == 'paper' and compyhand == 'spock':
        print("Paper disproves Spock.")
        print("You win...")
    if userhand.lower() == 'scissors' and compyhand == 'rock':
        print("Rock crushes scissors.")
        print("I win!")
    if userhand.lower() == 'scissors' and compyhand == 'spock':
        print("Spock smashes scissors.")
        print("I win!")
    if userhand.lower() == 'scissors' and compyhand == 'paper':
        print("Scissors cut paper.")
        print("You win...")
    if userhand.lower() == 'scissors' and compyhand == 'lizard':
        print("Scissors decapitate lizard.")
        print("You win...")
    if userhand.lower() == 'lizard' and compyhand == 'rock':
        print("Rock smashes lizard.")
        print("I win!")
    if userhand.lower() == 'lizard' and compyhand == 'scissors':
        print("Scissors decapitate lizard.")
        print("I win!")
    if userhand.lower() == 'lizard' and compyhand == 'paper':
        print("Lizard eats paper.")
        print("You win...")
    if userhand.lower() == 'lizard' and compyhand == 'spock':
        print("Lizard poisons Spock.")
        print("You win...")
    if userhand.lower() == 'spock' and compyhand == 'lizard':
        print("Lizard poisons Spock.")
        print("I win!")
    if userhand.lower() == 'spock' and compyhand == 'paper':
        print("Paper disproves Spock.")
        print("I win!")
    if userhand.lower() == 'spock' and compyhand == 'rock':
        print("Spock vaporizes rock.")
        print("You win...")
    if userhand.lower() == 'spock' and compyhand == 'scissors':
        print("Spock smashes scissors.")
        print("You win...")
    if userhand.lower() == compyhand:
        print(compyhand)
        print("A tie?")
    cont = input("Want to play again? >")
    if cont.lower() != 'yes':
        break
