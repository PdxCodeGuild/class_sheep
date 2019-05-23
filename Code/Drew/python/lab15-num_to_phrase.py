""" This program takes a number in digits and prints out the corresponding word """
tens_dict = {1: 'ten', 2 : 'twenty', 3 : 'thirty', 4 : 'fourty', 5 : 'fifty', 6 : 'sixty', 7 : 'seventy', 8 : 'eighty', 9 : 'ninety'}
teens_dict = {0: 'ten', 1 : 'eleven', 2 : 'twelve', 3 : 'thirteen', 4 : 'fourteen', 5 : 'fifteen', 6 : 'sixteen', 7 : 'seventeen', 8 : 'eighteen', 9 : 'nineteen'}
ones_dict = {0 : 'zero', 1 : 'one', 2 : 'two', 3 : 'three', 4 : 'four', 5 : 'five', 6 : 'six', 7 : 'seven', 8 : 'eight', 9 : 'nine'}

def num_parse(x):
    """ Parse digits into a list """
    nums_list = []
    while x != 0:
        nums_list.append(x % 10)
        x = x // 10
    return nums_list

try:
    # Get number from user
    in_num = int(input("Enter a number:\n"))
    # Create a list from number
    number_list = num_parse(in_num)
    # Print list according to dictionary
    if len(number_list) == 1:
        print(ones_dict[in_num])
    if len(number_list) == 2:
        if number_list[0] == 0:
            print(f"{ones_dict[number_list[1]]}")
        if number_list[1] > 1:
            print(f"{tens_dict[number_list[1]]}-{ones_dict[number_list[0]]}")
        elif number_list[1] == 1:
            print(f"{teens_dict[number_list[0]]}")
        elif number_list[1] == 0:
            print(f"{teens_dict[number_list[0]]}")
    if len(number_list) == 3:
        if number_list[1] > 1:
            print(f"{ones_dict[number_list[2]]}-hundred and {tens_dict[number_list[1]]}-{ones_dict[number_list[0]]}")
        elif number_list[1] == 1:
            print(f"{ones_dict[number_list[2]]}-hundred and {teens_dict[number_list[0]]}")
        elif number_list[1] < 1:
            print(f"{ones_dict[number_list[2]]}-hundred and {ones_dict[number_list[0]]}")
    if len(number_list) == 4:
        if number_list[1] > 1:
            print(f"{ones_dict[number_list[3]]} thousand {ones_dict[number_list[2]]}-hundred and {tens_dict[number_list[1]]}-{ones_dict[number_list[0]]}")
        elif number_list[1] == 1:
            print(f"{ones_dict[number_list[3]]} thousand {ones_dict[number_list[2]]} hundred and {teens_dict[number_list[0]]}")
        elif number_list[1] < 1:
            print(f"{ones_dict[number_list[3]]} thousand {ones_dict[number_list[2]]}-hundred and {ones_dict[number_list[0]]}")
    print(number_list)
except ValueError:
    print("That's not a number!")
