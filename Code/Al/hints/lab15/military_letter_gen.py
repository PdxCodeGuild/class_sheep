# military_letter_gen.py
'''
The goal of this program is to take in a word, and output a string of military letters to communicate the word.
'''
letter_dict = {'a': 'alpha', 'b': 'bravo', 'c': 'charlie'}
user_input = input("Give me some letters >")
out_string =''
for letter in user_input:
    out_string = out_string + letter_dict[letter] + ' '
print(out_string)
