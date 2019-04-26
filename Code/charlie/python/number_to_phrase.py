#number_to_phrase
import string
tens_dict = {10: 'Ten', 20: 'Twenty;', 30:'Thirty', 40:'Forty', 50:'Fifty', 60: 'Sixty', 70:'Seventy', 80: 'Eighty', 90: 'Ninety'}
singles_dict = {1: 'one', 2: 'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine'}
user_digit = int(input("enter digit"))
user_digit_tens = (user_digit // 10)*10
print(user_digit_tens)
user_digit_singles = user_digit % 10
print(user_digit_singles)

out_string = ''
# for tens in tens_dict.keys():
out_string += tens_dict[user_digit_tens]+ '-' + singles_dict[user_digit_singles]
print(out_string)
