import string
def string_has_a_digit(input_string):
    true_false_flag = False
    for letter in input_string:
        if letter in string.digits:
            true_false_flag = True
			break
    return true_false_flag

print(string_has_a_digit('abcdefghi'))
print(string_has_a_digit('abcde2fghi'))