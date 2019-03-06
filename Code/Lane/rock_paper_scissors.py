import random
choice = ['rock', 'paper', 'scissors']
computer_choice = random.choice(choice)
user_choice = input("Rock, paper or scissors?").lower()

if user_choice == computer_choice:
    print("Tie!")

elif computer_choice == 'rock':
    if user_choice == 'scissors':
        print('Computer wins!')
    else:
        print("You win!")

elif computer_choice =='paper':
    if user_choice == 'rock':
        print("Computer wins!")
    else:
        print("You win!")

elif computer_choice == 'scissors':
    if user_choice == 'paper':
        print("Computer wins!")
    else:
        print("You win!")
