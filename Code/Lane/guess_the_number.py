import random
guessesTaken = 0

print("Guess a number between 1 and 20: ")
player_guess = input()

number = random.randint(1, 10)
while guessesTaken < 9:
    guess = input()
    guess = int(guess)

    guessesTaken = guessesTaken + 1

    if guess < number:
        print('Too low. Pick a bigger number. ')
    if guess > number:
        print("Too high. Pick a smaller number. ")
    if guess == number:
        print ("Correct!")
        break
        print("Guess again: ")
