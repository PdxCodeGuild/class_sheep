import random
import time

while True:
    try:
        user_wallet = int(input("How much money are you starting with?\n"))
        break
    except ValueError:
        print("Enter a number")
        continue

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
        return user_wallet
    elif matches == 1:
        user_wallet += 4
        print(f"You got {matches} match. You win $4.")
        return user_wallet
    elif matches == 2:
        user_wallet += 7
        print(f"You got {matches} matches. You win $7.")
        return user_wallet
    elif matches == 3:
        user_wallet += 100
        print(f"You got {matches} matches. You win $100.")
        return user_wallet
    elif matches == 4:
        user_wallet += 50000
        print(f"You got {matches} matches. You win $50,000!")
        return user_wallet
    elif matches == 5:
        user_wallet += 1000000
        print(f"You got {matches} matches. You win $1,000,000!")
        return user_wallet
    elif matches == 6:
        user_wallet += 25000000
        print(f"You got {matches} matches. You win $25,000,000!")
        return user_wallet
for game in range(num_games):
    winning_numbers = []
    for i in range(6):
        winning_numbers.append(random.randrange(1, 100))
    winning_numbers = sorted(winning_numbers)
    user_nums = []
    for i in range(6):
        user_nums.append(random.randrange(1, 100))
    user_nums = sorted(user_nums)
    print(winning_numbers)
    time.sleep(.5)
    print(user_nums)
    time.sleep(.5)
    user_wallet = lottery_check(user_nums, user_wallet)
    user_wallet -= 2
    print(f"You have {user_wallet} dollars.")
