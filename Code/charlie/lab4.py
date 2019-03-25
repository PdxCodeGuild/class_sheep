import random


print('Welcome to the magic eight ball')

fortunes = [
    'it is certain', 'it is decidedly so',
    'Without a doubt', 'Yes definately',
    'As I may see it', 'Don\'t count on it',
    'Nope', 'Try again later'
    ]
#quit responses gives the user more flexibilty in responding
quit_responses = ['done', 'quit', 'finished', 'esc' ]

#while True lets the user ask as many questions as they want.
while True:
    user_input = input('what would you like to know? Type done when you want to quit.\n:')

    if user_input.lower() in quit_responses:
           print("All done")
           break
    else:
        answer = random.choice(fortunes)
        print(f'{answer}')
