# turn_left_or_right.py
import random
hands = ["r", "p", "s"]
user_hand = input("Give me your hand (rps)>")
user_hand_num = int(hands.index(user_hand))# user_hand = user_hand + turn_num
compy_hand_num = random.randint(0,2)
compy_hand = hands[compy_hand_num]
print(compy_hand)
if (compy_hand_num + 1) % 3 == user_hand_num:
    print('you win')
if (compy_hand_num + 1) % 3 == (user_hand_num - 1) % 3:
    print('i win')
if (compy_hand_num + 1) % 3 == (user_hand_num + 1) % 3:
    print('tie')


#
# import random
# rpslist = ["r", "p", "s"]
# user_hand = input("enter hand no. >")
# user_hand = int(user_hand)
# compy_hand = random.randint(0,2)
# print(user_hand)
# print(compy_hand)
# print(diff)
# print(conclusion)
