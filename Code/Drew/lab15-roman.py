roman = ['IV', 'IX', 'XL', 'XC', 'CD', 'CM', 'I', 'V', 'X', 'L', 'C', 'D', 'M']
roman_dict = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900, 'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
tens_dict = {1 : 'teen', 2 : 'twenty', 3 : 'thirty', 4 : 'forty', 5 : 'fifty', 6 : 'sixty', 7 : 'seventy', 8 : 'eighty', 9 : 'ninety'}
ones_dict = {0 : 'zero', 1 : 'one', 2 : 'two', 3 : 'three', 4 : 'four', 5 : 'five', 6 : 'six', 7 : 'seven', 8 : 'eight', 9 : 'nine'}

try:
    in_num = int(input("Enter a number:\n"))
    if 0 <= in_num <= 99:
        tens_digit = in_num//10
        ones_digit = in_num%10
    elif 100 <= in_num <= 999:
        tens_digit = (in_num%100)//10
        ones_digit = in_num%10
        hundreds = in_num//100
    if in_num >= 0 and in_num <10:
        print(ones_dict[in_num])
    elif in_num == 10:
        print('ten')
    elif in_num == 11:
        print('eleven')
    elif in_num == 12:
        print('twelve')
    elif in_num == 13:
        print('thirteen')
    elif in_num == 15:
        print('fifteen')
    elif 13 < in_num < 20:
        print(ones_dict[ones_digit]+tens_dict[tens_digit])
    elif in_num % 10 == 0:
        print(tens_dict[tens_digit])
    elif 99 < in_num < 1000:
        print(ones_dict[hundreds] +'-hundred and '+ tens_dict[tens_digit] + '-' +  ones_dict[ones_digit])
    elif in_num >= 1000:
        print('Number out of range')
    elif in_num < 0:
        print('Number out of range')
    else:
        print(tens_dict[tens_digit] + '-' +  ones_dict[ones_digit])

    out_string = ''
    roman_list = sorted(roman_dict.items(), key=lambda x: x[1], reverse=True)
    for i, x in roman_list:
        if in_num // int(x) > 0:
            out_string += i*(in_num//int(x))
            in_num %= int(x)

    print(out_string)

except ValueError:
    print("That's not a number!")

