#version 2: convert numbers from 0 - 999 to words
ones = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
teens = ['eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
tens = ['NotUsed', 'NotUsed', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
hundreds = ['NotUsed','one-hundred', 'two-hundred', 'three-hundred', 'four-hundred', 'five-hundred', 'six-hundred', 'seven-hundred', 'eight-hundred', 'nine-hundred']


def number_word(number):
    if number >= 100:
        hundreds_digit = number // 100 #divide by 100 to get the hundreds multiple
        hundreds_remainder = number % 100 #then find the remainder of 100 and use that to do the remaining math
        tens_digit = hundreds_remainder // 10 #using the hundreds remainder, find what multiple of 10 it is
        ones_digit = hundreds_remainder % 10 #using the hundreds remainder see how many ones after pulling out the multiples of 10
        if tens_digit == 0 and ones_digit == 0: #ie 200
            return hundreds[hundreds_digit]
        elif tens_digit == 1 and ones_digit > 0: #ie 250
            return hundreds[hundreds_digit] + '-' + teens[ones_digit]
        else: # ie 255
            return hundreds[hundreds_digit] + '-' + tens[tens_digit] + '-' + ones[ones_digit]
    elif number >= 20:
        tens_digit = number // 10 #to find tens digit, find what multiple of 10 it is
        ones_digit = number % 10 #see how many remain after pulling out the multiples of 10
        if ones_digit == 0:
            return tens[tens_digit]
        else:
            return tens[tens_digit] + '-' + ones[ones_digit]
    elif number >= 11:
        return teens[number - 11]
    elif number <= 10:
        return ones[number]


number = int(input('What is the number? '))

print(number_word(number))
