import random

responses = ("It is certain", "It is decidedly so", "Without a doubt", "Yes, definitely", "You may rely on it", "As I see it, yes", "Most likely", "Outlook good", "Yes", "signs point to yes", "Reply hazy try again", "Ask again later", "Better not tell you now", "Cannot predict now", "Concentrate and ask again", "Don't count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very doubtful")

continue_choice = 'yes'

while continue_choice == 'yes':
    player_choice = input('Type your yes/no style question: ')
    print(random.choice(responses))
    continue_choice = input('Do you want to ask another question? yes or no: ').lower()



# step=int(input('enter skip factor: '))
# num = int(input('Enter a number: '))
#
# while True:
#   for i in range(0,num,step):
#
#     if (i % 2) == 0:
#        print( i, ' is Even')
#     else:
#        print(i, ' is Odd')
# again = str(input('do you want to use another number? type yes or no')
#         if again = 'no' :
#             break
