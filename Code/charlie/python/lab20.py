


def credit_number_check(user_input):

    #this while statement allows the user to input a list of numbers until they are input 'done'
    while True:
        credit_number = input("enter your credit card number\n:")
        if credit_number == 'done':
            break
        credit_number = int(credit_number)
        credit_number_list.append(credit_number)
    # print(f"credit number is {credit_number_list}")

    # i pop the last integer and set that value to the check_digit variable.  I print the check digit and the list without the check digit.
    check_digit = credit_number_list.pop((len(credit_number_list)-1))
    # print(f"credit number list without the check number is {credit_number_list}")
    # print(f"check digit is {check_digit}")

    #str.reverse will reverse the credit number
    credit_number_list.reverse()
    # print(f" credit number reveresed is {credit_number_list}")

    #the for loop will insert an if statement for every indicie between 0 and the length of the list.  if the if statement is true, the value and the index will be multiplied by 2.
    for index in range(len(credit_number_list)):
        if index % 2 == 0:
            credit_number_list[index] *= 2
    print(credit_number_list)


    #this for loop will check each indice whether the value is above 9.  if it is, 9 will be removed from the value.
    for index in range(len(credit_number_list)):
        if credit_number_list[index] > 9:
            credit_number_list[index] -= 9
    # print(f"this is the list after 9 was removed from values above 9, {credit_number_list}")


    #this for loop will take each value in the list and then set it to a new variable, sum_credit_num, and continue to add to itself.
    sum_credit_num = 0
    for value in credit_number_list:
        sum_credit_num += value
    print(sum_credit_num)

    #i find the last number in the sum of the credit by determining the length of the string, and subtracting 1 to find the index.
    sum_credit_num = str(sum_credit_num)
    last_number = sum_credit_num[len(sum_credit_num)-1]
    last_number = int(last_number)

    if last_number == check_digit:
        print('Valid!')
        return True
    else:
        print("Invalid!")
        return False

credit_number_list = []
credit_number = ' '
credit_number_check(credit_number_list)
