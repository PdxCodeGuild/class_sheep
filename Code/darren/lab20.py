#lab20.py
'''Credit Card Validation'''

#mynum.copy()
#mynum.index()

'''Splits strings into lists'''
def list_converter(in_string):
    out_list = []
    for piece in in_string:
        out_list.append(int(piece))
    return out_list

'''Doubles every other index'''
def index_doubler(in_list):
    for index in range(len(in_list)):
        if index % 2 == 0:
            in_list[index] = in_list[index]*2

'''Subtracts 9 from every index greater than 9'''
def index_subtractor(in_list):
    for index in range(len(in_list)):
        if in_list[index] > 9:
            in_list[index] = in_list[index] - 9

'''Adds all indices together'''
def listadder(in_list):
    out_num = 0
    for index in range(len(in_list)):
        out_num += in_list[index]
    return out_num

#enter card number
card_string = input("Please enter a card number. >")
#turn card_string into a list
card_list = list_converter(card_string)
#split final check number from list and save in its own variable
check_num = card_list.pop(len(card_list)-1)
#reverse list
card_list.reverse()
#multiply every other index by 2
index_doubler(card_list)
#subtract 9 from every index over 9
index_subtractor(card_list)
#sum values in the list
card_sum = listadder(card_list)
#split out last digit of sum
sum_list = list(str(card_sum))
comp_num = sum_list[len(sum_list)-1]
comp_num = int(comp_num)
#check second digit against check number
if comp_num == check_num:
    print(f"The card number {card_string} is valid.")
else:
    print(f"The card number {card_string} is not valid.")
