#turn_left_or_right.py
#hint for lab 13
directions = ["North", "East", "South", "West"]
user_direction = 0
print(f"You are facing {directions[user_direction]}")
turn_num = int(input("How many times would you like to turn right?"))
user_direction += turn_num
print(f"you are facing {directions[user_direction % 4]}")
