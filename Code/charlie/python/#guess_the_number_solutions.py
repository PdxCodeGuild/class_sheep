#guess_the_number_solutions.py
import random

random_number = int(input('Choose a number between 1 and 10\n '))

print(user_number)

computer_number = random.randint(1,10)
print(computer_number)

guess_count = 0
while guess_count <=10:
    quit_option = input('type quit ')
    if quit_option == 'quit':
        break
    if random_number == computer_number:
        print('nice')
    elif random_number != computer_number:
        print('not nice, guess again')
        random_number = int(input('Guess again\n '))

    guess_count +=1
