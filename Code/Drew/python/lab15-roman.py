roman = ['IV', 'IX', 'XL', 'XC', 'CD', 'CM', 'I', 'V', 'X', 'L', 'C', 'D', 'M']
roman_dict = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900, 'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

# Create sorted list of tuples form dictionary
roman_list = sorted(roman_dict.items(), key=lambda x: x[1], reverse=True)

# Get input from user
in_num = int(input("Enter a number:\n"))

try:
    out_string = ''
    for x, y in roman_list:
        if in_num // int(y) > 0:
            # Starting with largest values, append roman numeral to out_string for each time it fits into user's number
            out_string += x*(in_num//int(y))
            # Take that value out of user's number, repeat with remainder
            in_num %= int(y)

    print(out_string)

except ValueError:
    print("That's not a number!")
