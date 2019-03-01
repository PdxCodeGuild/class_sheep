# turn_left_or_right.py
import random
hands = ["r", "p", "s"]
userhand = input("Give me your hand (rps)>")
userhandnum = int(hands.index(userhand))# userhand = userhand + turn_num
compyhandnum = random.randint(0,2)
compyhand = hands[compyhandnum]
print(compyhand)
if (compyhandnum + 1) % 3 == userhandnum:
    print('you win')
if (compyhandnum + 1) % 3 == (userhandnum - 1) % 3:
    print('i win')
if (compyhandnum + 1) % 3 == (userhandnum + 1) % 3:
    print('tie')


#
# import random
# rpslist = ["r", "p", "s"]
# userhand = input("enter hand no. >")
# userhand = int(userhand)
# compyhand = random.randint(0,2)
# print(userhand)
# print(compyhand)
# print(diff)
# print(conclusion)
