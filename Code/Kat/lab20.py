#Lab 20: Credit Card Validation

# INSTRUCTIONS:
# Let's write a function which returns whether a string containing a credit card number is valid as a boolean. The steps are as follows:
#
# 1. Convert the input string into a list of ints
# 2. Slice off the last digit. That is the check digit.
# 3. Reverse the digits.
# 4. Double every other element in the reversed list.
# 5. Subtract nine from numbers over nine.
# 6. Sum all values.
# 7. Take the second digit of that sum.
# 8. If that matches the check digit, the whole card number is valid.

#function for validating card number
def valid_card(card_number):
    card_number = list(card_number)
    for i in range(len(card_number)):
        card_number[i] = int(card_number[i])
    last_number = card_number.pop(-1)
    card_number.reverse()
    for j in range(0, len(card_number), 2):
        card_number[j] *= 2
    added_num = 0
    for num in range(len(card_number)):
        if card_number[num] > 9:
            card_number[num] -= 9
        added_num += card_number[num]
    second_digit = added_num % 10
    if second_digit == last_number:
        return 'Valid!'
    else:
        return 'Invalid card. Please try again.'

card_number = input('Please input a credit card number > ')
print(valid_card(card_number))
