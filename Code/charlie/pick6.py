#pick6.py

import random
'''
The lottery picks a lsit of numbers, and then i play the game and generate a list of numbers.  those two lists are compared and then the winnings are determined.  i run the game 100,000 times and sum the total winnings.
'''
def pick6():
    lottery_list = []
    length = 0
    while length < 6:
        random_number = random.randint(1,99)
        lottery_list.append(random_number)
        length += 1
    # print(lottery_list)
    return(lottery_list)

def num_matches():
   player_list = []
   length = 0
   # player_list = lottery_list
   while length < 6:
       random_number = random.randint(1,99)
       player_list.append(random_number)
       length += 1
   # print(player_list)
   return(player_list)
# def winnings():
# #     num_matches()
# #     user_balance = (play_count*-2)+winnings
# #     for index in range(len(user_list)):
# #         if user_list[0] == list[0]:
# #             winnings += 1
# #
# #         if user_list[0] == list[0]:
# #             winnings += 1
# #
# #         if user_list[1] == list[1]:
# #             winnings += 1
# #
# #         if user_list[2] == list[2]:
# #             winnings += 1
# #
# #         if user_list[3] == list[3]:
# #             winnings += 1
# #
# #         if user_list[4] == list[4]:
# #             winnings += 1
# #
# #         if user_list[5] == list[5]:
# #             winnings += 1
# #             if winnings == 1:
# #                 winnings = 2
# #             elif winnings == 2:
# #                 winnings = 7
# #             elif winnings == 3:
# #                 winnings = 100
# #             elif winnings ==4:
# #                 winnings = 50000
# #             elif winnings == 5:
# #                 winnings = 1000000
# #             elif winnings == 6:
# #                 winnings = 25000000
# #     return(user_balance)
# #     print(user_balance)
#
#
# game_range = [1,99]

user_balance = 0
wallet = 0
# pick6()
play_count = 0
# lottery_list = pick6()
winnings = 0
lottery_list = pick6()

while play_count < 100000:
    player_list = num_matches()
    play_count += 1
    for num in [0,1,2,3,4,5]:
        if player_list[num] == lottery_list[num]:
            winnings +=1
            if winnings > 0:
                if winnings == 1:
                    winnings = 2
                elif winnings == 2:
                    winnings = 7
                elif winnings == 3:
                    winnings = 100
                elif winnings ==4:
                    winnings = 50000
                elif winnings == 5:
                    winnings = 1000000
                elif winnings == 6:
                    winnings = 25000000
        wallet += winnings
wallet -= (2*play_count)

print(f"winnings is {wallet}")
# winnings()
