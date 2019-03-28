import random
while True:
    try:
        user_wallet = int(input("How much money are you starting with?\n"))
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
while True:
    print(f"You have {user_wallet} dollars.")
    play = input("Would you like to buy a ticket? (y/n):\n")
    if play in ['y', 'yes']:
        try:
            winning_numbers = []
            for i in range(6):
                winning_numbers.append(random.randrange(1, 100))
            winning_numbers = sorted(winning_numbers)
            print(winning_numbers)
            user_nums = input("Enter six numbers (comma-separated):\n")
            user_nums = user_nums.split(',')
            user_nums = [int(i) for i in user_nums]
            user_nums = sorted(user_nums)
            print(user_nums)
            user_wallet = lottery_check(user_nums, user_wallet)
        except:
            print("Try again.")
    elif play in ['n', 'no']:
        break
    else:
        print("Invalid response.")
        continue
