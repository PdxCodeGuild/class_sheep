# Lab 4: Magic 8-Ball
# Let's write a program to simulate the classic "Magic Eight Ball"
# Instructions
# 1. Print a welcome screen to the user.
# 2. Use the random module's random.choice() to choose a prediction.
# 3. Prompt the user to ask the 8-ball a question "will I win the lottery tomorrow?"
# 4. Display the result of the 8-ball.

# Version 2
# Using a while loop, keep asking the user for a question, if they enter 'done', exit

import random
print("Welcome to the Magic 8 Ball.")
answer_list = ["absolutely!", "not clear. Please ask again later.", "no way!", "that your future has already been determined.", "never give up!"]
# allow player to continue playing
while True:
    user_answer = input("Please ask the magic eight ball your question. Type done to exit. >")
    # option to leave the program
    if user_answer == 'done':
        print("Thank you for playing. Goodbye!")
        break
    print(f"The answer to your question is {random.choice(answer_list)}")
