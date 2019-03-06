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

def player_ticket():
   player_list = []
   length = 0
   # player_list = lottery_list
   while length < 6:
       random_number = random.randint(1,99)
       player_list.append(random_number)
       length += 1
   # print(player_list)
   return(player_list)


#total_winnings will compare the pick6 to player ticket to determine how many matches each ticket has.  matches are inside the while loop, so they will be reset inbetween ticket.  winnings are added outside the loop so a total is accumulated.

def total_winnings(stuff, stuff2):
    play_count = 0
    winnings = 0
    lottery_list = pick6()
    while play_count < user_input:
        player_list = player_ticket()
        play_count += 1
        matches = 0
        for num in [0,1,2,3,4,5]:
            if player_list[num] == lottery_list[num]:
                matches +=1
                if matches == 1:
                    winnings += 1
                elif matches == 2:
                    winnings += 5
                elif matches == 3:
                    winnings += 100
                elif matches == 4:
                    winnings += 50000
                elif matches == 5:
                    winnings += 1000000
                elif matches == 6:
                    winnings +=25000000
    return(winnings, play_count)

def ROI():
    roi= (output[0]-output[0]*2)/output[0]*2
    return(roi)

user_input = int(input("play count \n"))
winnings = 0
play_count = 0
output = total_winnings(winnings, play_count)
balance =output[0] + output[1]*(-2)
roi = ROI()



print(f"you played {output[1]} times, and you won {output[0]}. The problem is that you spent '{output[1] * 2}$ so you're in the hole {balance}.  Your ROI is {roi}")
