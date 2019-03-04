import random
plays = ['rock', 'paper', 'scissors']
computer_play = random.choice(plays)
computer_choice = plays.index(computer_play)
user_play = input("Would you like to play rock, paper, or scissors? >")
play_num = ['rock', 'paper', 'scissors'].index(user_play)
play_num = int(play_num)
print(f"The computer played {computer_play}.")
computer_choice += play_num
computer_choice = plays[computer_choice % 3]
print(computer_choice)
if computer_choice == play_num:
    print("Tie!")
elif computer_choice > play_num:
    print("You lose!")
elif computer_choice < play_num:
    print("You win!")

# computer_play += play_num
# print(computer_play)
