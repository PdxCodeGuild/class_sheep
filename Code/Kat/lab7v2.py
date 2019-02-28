import random
rps_dict = {'rock': ['paper', 'scissors'], 'paper': ['scissors', 'rock'], 'scissors': ['rock', 'paper']}
user_choice = input
if comp_choice == rps_dict[user_choice][0]:
    print('you lose')
if comp_choice == rps_dict[user_choice][1]:
    print('you win')
