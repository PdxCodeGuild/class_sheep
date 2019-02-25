import random

print('Welcome to the magic eight ball')

user_input = input('what would you like to know? Type done when you want to quit.  ')

eightball_list = ['it is certain', 'it is decidedly so', 'Without a doubt', 'Yes definately', 'As I may see it', 'Don\'t count on it', 'Nope', 'Try again later']

eightball_answer = random.choice(eightball_list)

print(f'{eightball_answer}')

user_input1 = 0
user_input1 = input('Are you done, or would you like to ask another question?')
while True:
   if user_input1 == 'done':
       print("All done")
       break

   elif user_input1 != 'done':
       user_guess = input("Ask again> ")
       eightball_list = ['it is certain', 'it is decidedly so', 'Without a doubt', 'Yes definately', 'As I may see it', 'Don\'t count on it', 'Nope', 'Try again later']
       eightball_answer = random.choice(eightball_list)
       print(f'{eightball_answer}')
