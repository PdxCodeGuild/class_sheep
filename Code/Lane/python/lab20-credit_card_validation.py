# Lab 20, credit card validation

# user_input = input('Enter your credit card number with a space between each number: ')

user_input = '4 5 5 6 7 3 7 5 8 6 8 9 9 8 5 5'

#convert input string to list of integers
cc = user_input.split(' ')
for i in range(len(cc)):
    cc[i] = int(cc[i])
# cc = [int(i) for i in user_input.split(' ')]

# Slice off the last digit. That is the check digit.
check_digit = cc.pop(-1)
print(check_digit)

#Reverse the digits
cc = cc[::-1]
print(cc)

total = 0
for i in range(len(cc)):
    if i % 2 == 0: # Double every other element in the reversed list
        cc_doubled = cc[i]*2
        print(cc_doubled)
        if cc_doubled >= 9:
            cc_doubled -= 9 # Subtract nine from numbers over nine
        total += cc_doubled # Sum all even values
    else:
        total += cc[i] # Sum all odd values
print(f'Total = {total}')


# Take the second digit of the total
def second_digit(num):
    if num < 10:
        return None
    return num%10

# If the second_digit matches the check digit, the whole card number is valid
if second_digit(total) == check_digit:
    print('Valid')
else:
    print('Invalid')
