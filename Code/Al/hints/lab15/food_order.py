# food_order.py
'''
The goal of this program is to let the user enter a three-digit number, and parse a lunch order
'''
food_list = ['sandwiches', 'rolls', 'cups of soup'] # these are the foods to order

def sandwich_order(in_num):
    return f"You want {in_num} {food_list[0]}, "

def roll_order(in_num):
    return f"{in_num} {food_list[1]}, "

def soup_order(in_num):
    return f"{in_num} {food_list[2]}."

def full_order(full_num):
    return sandwich_order( full_num // 100 ) + roll_order((full_num % 100) // 10) + soup_order(full_num % 10) # using // and % to get the correct digits

print("You can order 0-9 sandwiches, 0-9 rolls, 0-9 cups of soup")
user_input = int(input("Please give me all three numbers together >"))
print(full_order(user_input))
