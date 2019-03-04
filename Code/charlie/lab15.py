#number_to_phrase




import string

def teen(in_num):
    out_string = ''
    out_string += teen_dict[user_digit]
    print(out_string)
    return(out_string)

def singles(in_num):
    user_digit_singles = user_digit % 10
    out_string = ''
    out_string += singles_dict[user_digit_singles]
    print(out_string)
    return(out_string)

def tens(in_num):
    user_digit_tens = (user_digit // 10)*10
    user_digit_singles = user_digit % 10
    out_string = ''
    out_string += tens_dict[user_digit_tens] + singles_dict[user_digit_singles]
    print(out_string)
    return(out_string)

def hundreds(in_num):
    user_digit_hundreds =  (user_digit //100)*100
    user_digit_tens = ((user_digit // 10)*10) - user_digit_hundreds
    user_digit_singles = user_digit % 10
    out_string = ''
    out_string += hundreds_dict[user_digit_hundreds] +' and '+ tens_dict[user_digit_tens] + '-' + singles_dict[user_digit_singles]
    print(out_string)
    return(out_string)

def tens_Roman(in_num):
    user_digit_tens = (user_digit // 10)*10
    user_digit_singles = user_digit % 10
    out_string = ''
    out_string += tens_dict[user_digit_tens] + singles_dict[user_digit_singles]
    print(out_string)
    return(out_string)


def hundreds_Roman(in_num):
    user_digit_hundreds =  (user_digit //100)*100
    user_digit_tens = ((user_digit // 10)*10) - user_digit_hundreds
    user_digit_singles = user_digit % 10
    out_string = ''
    out_string += hundreds_dict[user_digit_hundreds] + tens_dict[user_digit_tens] + singles_dict[user_digit_singles]
    print(out_string)
    return(out_string)

user_choice = input("do you want numbers or Roman numerals > ")
if user_choice == 'numbers':
    user_digit = int(input("enter digit "))

    hundreds_dict = {100: 'One Hundred',200: 'Two Hundred',300: 'Three Hundred',400: 'Four Hundred',500: 'Five Hundred',600: 'Six Hundred',700: 'One Hundred',800: 'Eight Hundred',900: 'Nine Hundred'}
    tens_dict = {10: 'Ten', 20: 'Twenty', 30:'Thirty', 40:'Forty', 50:'Fifty', 60: 'Sixty', 70:'Seventy', 80: 'Eighty', 90: 'Ninety'}
    singles_dict = {0:'', 1: '-one', 2: '-two', 3:'-three', 4:'-four', 5:'-five', 6:'-six', 7:'-seven', 8:'-eight', 9:'-nine'}
    teen_dict = {11: 'eleven', 12: 'Twelve', 13: 'Thirtenn', 14: 'Fourteen', 15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen'}

    if user_digit >=11 and user_digit <=19:
        teen(user_digit)

    while user_digit >= 20 or user_digit <= 10:
        if user_digit < 10:
            singles(user_digit)
            break
        if user_digit >= 10 and user_digit <= 99:
            tens(user_digit)
            break
        if user_digit >= 100:
            hundreds(user_digit)
            break

#V 3 dict
elif user_choice == 'Roman numerals':
    user_digit = int(input("enter digit "))

    hundreds_dict = {100: 'C',200: 'CC',300: 'CCC',400: 'CD',500: 'D',600: 'DC',700: 'DCC',800: 'DCCC',900: 'CM'}
    tens_dict = {10: 'X', 20: 'XX', 30:'XXX', 40:'XL', 50:'L', 60: 'LX', 70:'LXX', 80: 'LXXX', 90: 'XC'}
    singles_dict = {1: 'I', 2: 'II', 3:'III', 4:'IV', 5:'V', 6:'VI', 7:'VII', 8:'VIII', 9:'IX'}
    teen_dict = {11: 'XI', 12: 'XII', 13: 'XIII', 14: 'XIV', 15: 'XV', 16: 'XVI', 17: 'XVII', 18: 'XVIII', 19: 'XIX'}


    if user_digit <= 10:
        singles(user_digit)


    elif user_digit >=11 and user_digit <=19:
        teen(user_digit)


    elif user_digit >= 20 and user_digit <= 99:
        tens_Roman(user_digit)

    elif user_digit >= 100:
        hundreds_Roman(user_digit)
