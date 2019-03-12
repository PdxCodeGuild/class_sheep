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
        return "Valid!"
    else:
        return "Invalid card. Please try again."

card_number = input("Please input a credit card number > ")
print(valid_card(card_number))
