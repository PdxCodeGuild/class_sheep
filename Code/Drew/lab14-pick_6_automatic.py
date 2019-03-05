import random
import time

while True:
    try:
        user_wallet = int(input("How much money are you starting with?\n"))
        break
    except ValueError:
        print("Enter a number")
        continue

starting_wallet = user_wallet

while True:
    try:
        num_games = int(input("How many games do you want to play?\n"))
        break
    except ValueError:
        print("Enter a number")
        continue

def lottery_check(l, user_wallet):
    matches = 0
    for i in range(len(l)):
        if l[i] == winning_numbers[i]:
            matches += 1
            continue
    if matches == 0:
        print(f"You got {matches} matches.")
        return user_wallet, matches
    elif matches == 1:
        user_wallet += 4
        print(f"You got {matches} match. You win $4.")
        return user_wallet, matches
    elif matches == 2:
        user_wallet += 7
        print(f"You got {matches} matches. You win $7.")
        return user_wallet, matches
    elif matches == 3:
        user_wallet += 100
        print(f"You got {matches} matches. You win $100.")
        return user_wallet, matches
    elif matches == 4:
        user_wallet += 50000
        print(f"You got {matches} matches. You win $50,000!")
        return user_wallet, matches
    elif matches == 5:
        user_wallet += 1000000
        print(f"You got {matches} matches. You win $1,000,000!")
        return user_wallet, matches
    elif matches == 6:
        user_wallet += 25000000
        print(f"You got {matches} matches. You win $25,000,000!")
        return user_wallet, matches
highest = 0
for game in range(num_games):
    winning_numbers = random.sample(range(1, 100), 6)
    winning_numbers = sorted(winning_numbers)
    user_nums = random.sample(range(1, 100), 6)
    user_nums = sorted(user_nums)
    print(winning_numbers)
    print(user_nums)
    temp_var = lottery_check(user_nums, user_wallet)
    user_wallet = temp_var[0]
    user_wallet -= 2
    if temp_var[1] > highest:
        highest = temp_var[1]
    print(f"                                     You have {user_wallet} dollars.")
    time.sleep(.1)

print(f"Your best game was {highest} matches.")
print(f"Overall ROI was {(((user_wallet - starting_wallet)-(num_games*2))/(num_games*2))}.")
