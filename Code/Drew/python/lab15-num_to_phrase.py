
tens_dict = {1: 'ten', 2 : 'twenty', 3 : 'thirty', 4 : 'fourty', 5 : 'fifty', 6 : 'sixty', 7 : 'seventy', 8 : 'eighty', 9 : 'ninety'}
teens_dict = {0: 'ten', 1 : 'eleven', 2 : 'twelve', 3 : 'thirteen', 4 : 'fourteen', 5 : 'fifteen', 6 : 'sixteen', 7 : 'seventeen', 8 : 'eighteen', 9 : 'nineteen'}
ones_dict = {0 : 'zero', 1 : 'one', 2 : 'two', 3 : 'three', 4 : 'four', 5 : 'five', 6 : 'six', 7 : 'seven', 8 : 'eight', 9 : 'nine'}

def num_parse(x):
    nums_list = []
    while x != 0:
        nums_list.append(x % 10)
        x = x // 10
    return nums_list

# Method 2:
try:
    # Get number from user
    in_num = int(input("Enter a number:\n"))
    # Create a list from number
    number_list = num_parse(in_num)
    if len(number_list) == 1:
        print(ones_dict[in_num])
    if len(number_list) == 2:
        if number_list[0] == 0:
            #############pausing here
        if number_list[1] > 1:
            print(f"{tens_dict[number_list[1]]}-{ones_dict[number_list[0]]}")
        elif number_list[1] == 1:
            print(f"{teens_dict[number_list[0]]}")
        elif number_list[1]  1:
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
#try:
#    in_num = int(input("Enter a number:\n"))
#    if 0 <= in_num <= 99:
#        tens_digit = in_num//10
#        ones_digit = in_num%10
#    elif 100 <= in_num <= 999:
#        tens_digit = (in_num%100)//10
#        ones_digit = in_num%10
#        hundreds = in_num//100
#    if in_num >= 0 and in_num <10:
#        print(ones_dict[in_num])
#    elif in_num == 10:
#        print('ten')
#    elif in_num == 11:
#        print('eleven')
#    elif in_num == 12:
#        print('twelve')
#    elif in_num == 13:
#        print('thirteen')
#    elif in_num == 15:
#        print('fifteen')
#    elif 13 < in_num < 20:
#        print(ones_dict[ones_digit]+tens_dict[tens_digit])
#    elif in_num % 10 == 0:
#        print(tens_dict[tens_digit])
#    elif 99 < in_num < 1000:
#        print(ones_dict[hundreds] +'-hundred and '+ tens_dict[tens_digit] + '-' +  ones_dict[ones_digit])
#    elif in_num >= 1000:
#        print('Number out of range')
#    elif in_num < 0:
#        print('Number out of range')
#    else:
#        print(tens_dict[tens_digit] + '-' +  ones_dict[ones_digit])
#except ValueError:
#    print("That's not a number!")
