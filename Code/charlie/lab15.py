#number_to_phrase

# what problem does your application solve?
# what is the core function it performs?

# how did you go about planning?

# what major issues did you encounter during the course of development?
# how did you go about overcoming them?

# how did your vision for the project change over time?

# what part did you like the most? least?

# what is the future of the project?
 # what features (if any) will you work on next?

#improve readability
#create a class for all these funcitons
import string
#V1-3
def teen(in_num):
    out_string = ''
    out_string += teen_dict[in_num]
    return(out_string)

def singles(in_num):
    single_digit = in_num % 10
    out_string = ''
    out_string += singles_dict[single_digit]
    return(out_string)

def tens(in_num):
    ten_digit = (in_num // 10)*10
    single_digit = in_num % 10
    out_string = ''
    out_string += tens_dict[ten_digit] + singles_dict[single_digit]
    return(out_string)

def hundreds(in_num):
    hundred_digit =  (in_num //100)*100
    ten_digit = (in_num - hundred_digit) // 10 * 10
    teen_digit = in_num - hundred_digit
    single_digit = in_num % 10
    out_string = ''
    if single_digit == 0 and ten_digit == 0:
        out_string = hundreds_dict[hundred_digit]

    elif single_digit == 0:
        out_string += hundreds_dict[hundred_digit] +' and '+ tens_dict[ten_digit]
    elif ten_digit == 0:
        out_string += hundreds_dict[hundred_digit] + ' and ' + singles_dict[single_digit]
    elif teen_digit in teen_dict:
        out_string += hundreds_dict[hundred_digit] + ' and ' + tens_dict[teen_digit]
    else:
        out_string += hundreds_dict[hundred_digit] + ' and ' + tens_dict[ten_digit] + '-' + singles_dict[single_digit]
    return(out_string)

#V3
def tens_Roman(in_num):
    ten_digit = (in_num // 10)*10
    single_digit = in_num % 10
    out_string = ''
    out_string += tens_dict[ten_digit] + singles_dict[single_digit]
    return(out_string)


def hundreds_Roman(in_num):
    hundred_digit =  (in_num //100)*100
    ten_digit = ((in_num // 10)*10) - hundred_digit
    single_digit = in_num % 10
    out_string = ''
    out_string += hundreds_dict[hundred_digit] + tens_dict[ten_digit] + singles_dict[single_digit]
    return(out_string)

#V4
def time(in_num):
    in_num_hours =  user_nums[0]
    in_num_minute = user_nums[1]
    out_string = ''

    if in_num_minute < 20 and in_num_minute > 10:
        in_num_teen = ((user_nums[1] % 20))
        out_string += (hour_dict[in_num_hours] +' ' + minute_teen_dict[in_num_teen])

    elif in_num_minute >= 10:
        ten_digit = user_nums[1]//10*10
        single_digit = user_nums[1] % 10
        out_string += hour_dict[in_num_hours] +' ' +minute_tens_dict[ten_digit] + minute_singles_dict[single_digit]
    elif in_num_minute < 10:
        in_num_O = user_nums[1]
        out_string += hour_dict[in_num_hours] + hour_O_minute_dict[in_num_O]

    return(out_string)

#==============================NUMBERS=======================================

user_choice = input("do you want numbers or Roman numerals or a time > ")
if user_choice == 'numbers':
    user_num = int(input("enter digit "))

    hundreds_dict = {
        100: 'One Hundred',200: 'Two Hundred',300: 'Three Hundred',
        400: 'Four Hundred',500: 'Five Hundred',600: 'Six Hundred',
        700: 'One Hundred',800: 'Eight Hundred',900: 'Nine Hundred'
        }
    tens_dict = {
        0: '', 10: 'Ten', 20: 'Twenty', 30:'Thirty', 40:'Forty', 50:'Fifty',
        60: 'Sixty', 70:'Seventy', 80: 'Eighty', 90: 'Ninety'
        }
    singles_dict = {
        0:'', 1: 'one', 2: 'two', 3:'three', 4:'four', 5:'five',
        6:'six', 7:'seven', 8:'eight', 9:'nine'
        }
    teen_dict = {
        11: 'eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen',
        16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen'
        }

    if user_num >=11 and user_num <=19:
        print(teen(user_num))

    if user_num >= 20 or user_num <= 10:
        if user_num < 10:
            print(singles(user_num))


        elif user_num >= 10 and user_num <= 99:
            print(tens(user_num))


        elif user_num >= 100:
            print(hundreds(user_num))



#==============================ROMAN NUMERALS===================================
elif user_choice == 'Roman numerals':
    user_num = int(input("enter digit "))

    hundreds_dict = {
        100: 'C',200: 'CC',300: 'CCC',400: 'CD',500:'D',
        600: 'DC',700: 'DCC',800: 'DCCC',900: 'CM'
        }
    tens_dict = {
        10: 'X', 20: 'XX', 30:'XXX', 40:'XL', 50:'L',
        60: 'LX', 70:'LXX', 80: 'LXXX', 90: 'XC'
        }
    singles_dict = {
        1: 'I', 2: 'II', 3:'III', 4:'IV', 5:'V',
        6:'VI', 7:'VII', 8:'VIII', 9:'IX'
        }
    teen_dict = {
        11: 'XI', 12: 'XII', 13: 'XIII', 14: 'XIV', 15: 'XV',
        16: 'XVI', 17: 'XVII', 18: 'XVIII', 19: 'XIX'
        }


    if user_num <= 10:
        print(singles(user_num))

    elif user_num >=11 and user_num <=19:
        print(teen(user_num))

    elif user_num >= 20 and user_num <= 99:
        print(tens_Roman(user_num))

    elif user_num >= 100:
        print(hundreds_Roman(user_num))

#==============================TIME=======================================
elif user_choice == 'time':
    user_num = input("enter time ")
    user_nums = user_num.split(':')
    user_nums = list(map(int, user_nums))

    hour_dict = {
        1: 'One', 2: 'Two', 3:'Three', 4:'Four', 5:'Five', 6:'Six',
        7:'Seven', 8:'Eight', 9:'Nine', 10: 'Ten', 11: 'Eleven', 12:'Twelve'
        }

    minute_tens_dict = {
        10: 'ten', 20: 'twenty', 30:'thirty', 40:'forty', 50:'fifty'
        }

    minute_singles_dict = {
        0:'', 1: '-one', 2: '-two', 3:'-three', 4:'-four',
        5:'-five', 6:'-six', 7:'-seven', 8:'-eight', 9:'-nine'
        }

    hour_O_minute_dict = {
        0: ' O-clock', 1: ' O-one', 2: ' O-two', 3: ' O-three', 4: ' O-four',
        5: ' O-five', 6: ' O-six', 7: ' O-seven', 8: ' O-eight', 9: ' O-nine'
        }
    minute_teen_dict = {
        11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
        15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen',
        19: 'nineteen'
        }

    print(time(user_num))
    # print(user_nums)
