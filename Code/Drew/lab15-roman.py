roman = ['IV', 'IX', 'XL', 'XC', 'CD', 'CM', 'I', 'V', 'X', 'L', 'C', 'D', 'M']
roman_dict = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900, 'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
roman_list = sorted(roman_dict.items(), key=lambda x: x[1], reverse=True)

in_num = int(input("Enter a number:\n"))
try:
    out_string = ''
    for i, x in roman_list:
        if in_num // int(x) > 0:
            out_string += i*(in_num//int(x))
            in_num %= int(x)

    print(out_string)

except ValueError:
    print("That's not a number!")

#convert back
