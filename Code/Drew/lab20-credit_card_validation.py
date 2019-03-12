# ask user for number

cc_input = input("Please enter your credit card number:\n")

# convert user number to list of strings
cc_number = []
for num in cc_input:
    try:
        cc_number.append(int(num))
    except ValueError:
        continue
# pop and assign last number in list
check_digit = cc_number.pop(-1)

# reverse list
cc_number.reverse()

# define function to double every other number
def doubled(l):
    d_list = []
    for x in range(len(l)):
        if x%2 == 0:
            d_list.append(l[x]*2)
        else:
            d_list.append(l[x])
    return d_list

# define function to subtract 9 from all numbers greater than 9
def sub_nine(l):
    s_list = []
    for x in l:
        if x > 9:
            s_list.append(x-9)
        else:
            s_list.append(x)
    return s_list

# apply previous two functions
cc_number = sub_nine(doubled(cc_number))

# sum all numbers in the list
total = sum(cc_number)

# check second digit against the original check digit
if check_digit == total%10:
    print("Valid number.")
else:
    print("Invalid number.")
