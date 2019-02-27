#lab4
#eightball
import random
while True:
    question = input("Ask me any question. >")
    answer_list = ['For certain', 'Doubtful', 'Ask again later', 'Unlikely', 'Probably yes']
    print(f"{random.choice(answer_list)}")
    cont = input("Type 'done' if you are finished. >")
    if cont.lower() == 'done':
        break
