# turn_left_or_right.py
'''
The purpose of this program is to tell the user what direction they're facing, let them choose how many times they want to turn right, and then tell them their direction after turning.
'''
import random
directions = ["North", "East", "South", "West"]
user_direction = random.randint(0, 3)
print(f"You are facing {directions[user_direction]}") # You are facing North, or East, or South, or West
turn_num = int(input("How many times would you like to turn 90 degrees right? >"))
user_direction += turn_num # user_direction = user_direction + turn_num
print(f"You are facing {directions[user_direction % 4]}") # You are facing North, or East, or South, or West
