#number_to_phrase
import string
hundreds_dict = {100: 'One Hundred',200: 'Two Hundred',300: 'Three Hundred',400: 'Four Hundred',500: 'Five Hundred',600: 'Six Hundred',700: 'One Hundred',800: 'Eight Hundred',900: 'Nine Hundred'}
tens_dict = {10: 'Ten', 20: 'Twenty', 30:'Thirty', 40:'Forty', 50:'Fifty', 60: 'Sixty', 70:'Seventy', 80: 'Eighty', 90: 'Ninety'}
singles_dict = {1: 'one', 2: 'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine'}
user_digit = int(input("enter digit "))

if user_digit == 11:
    print('Eleven')
elif user_digit == 12:
    print('Twelve')
elif user_digit == 13:
    print('Thirteen')
elif user_digit == 14:
    print('Fourteen')
elif user_digit == 15:
    print('Fifteen')
elif user_digit == 16:
    print('Sixteen')
elif user_digit == 17:
    print('Seventeen')
elif user_digit == 18:
    print('Eighteen')
elif user_digit == 19:
    print('Nineteen')

# while user_digit >= 20 or user_digit <= 10:
while user_digit >= 20 or user_digit <= 10:
    if user_digit <= 10:

        user_digit_singles = user_digit % 10
        print(user_digit_singles)
        out_string = ''
        out_string += singles_dict[user_digit_singles]
        print(out_string)
        break


    if user_digit >= 20 and user_digit <= 99:
        user_digit_tens = (user_digit // 10)*10
        print(user_digit_tens)
        user_digit_singles = user_digit % 10
        print(user_digit_singles)
        out_string = ''
        out_string += tens_dict[user_digit_tens] + '-' + singles_dict[user_digit_singles]
        print(out_string)
        break

    if user_digit >= 100:
        user_digit_hundreds =  (user_digit //100)*100
        print(user_digit_hundreds)
        user_digit_tens = ((user_digit // 10)*10) - user_digit_hundreds
        print(user_digit_tens)
        user_digit_singles = user_digit % 10
        print(user_digit_singles)

        out_string = ''
        out_string += hundreds_dict[user_digit_hundreds] +' and '+ tens_dict[user_digit_tens] + '-' + singles_dict[user_digit_singles]
        print(out_string)
        break
