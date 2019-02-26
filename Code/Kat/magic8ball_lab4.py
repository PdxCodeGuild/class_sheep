import random
print("Welcome to the Magic 8 Ball.")
answer_list = ["absolutely", "not clear", "no way!", "your future has already been determined", "don't give up"]
while True:
    user_question = input("Please ask the magic eight ball your question. Type done to exit. >")
    if user_question == 'done':
        break
    else:
        print(f"The answer to your question is {random.choice(answer_list)}.")
