#lab20.py
#Credit Card Validation

#mynum.copy()
#mynum.index()

#tool to split strings into lists
def list_converter(in_string):
    out_list = []
    for piece in in_string:
        out_list.append(int(piece))
    return out_list

#tool to double every other index
def index_doubler(in_list):
    for index in range(len(in_list)):
        if index % 2 == 0:
            in_list[index] = in_list[index]*2

#tool to subtract 9 from all indices with value > 9
def index_subtractor(in_list):
    for index in range(len(in_list)):
        if in_list[index] > 9:
            in_list[index] = in_list[index] - 9

#tool to add all values of indices in a list together
def listadder(in_list):
    out_num = 0
    for index in range(len(in_list)):
        out_num += in_list[index]
    return out_num

#enter card number
card_string = input("Please enter a card number. >")
# print(card_string)
#turn card_string into a list
card_list = list_converter(card_string)
# print(card_list)
#split final check number from list and save in its own variable
check_num = card_list.pop(len(card_list)-1)
# print(check_num)
#reverse list
card_list.reverse()
# print(card_list)
#multiply every other index by 2
index_doubler(card_list)
# print(card_list)
#subtract 9 from every index over 9
index_subtractor(card_list)
# print(card_list)
#sum values in the list
card_sum = listadder(card_list)
# print(card_sum)
#split out last digit of sum
sum_list = list(str(card_sum))
# print(sum_list)
comp_num = sum_list[len(sum_list)-1]
comp_num = int(comp_num)
# print(comp_num)
#check second digit against check number
if comp_num == check_num:
    print(f"The card number {card_string} is valid.")
else:
    print(f"The card number {card_string} is not valid.")
