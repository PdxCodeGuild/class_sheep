# rate_of_vowel.py
in_string = ''
while True: # REPL until the user types 'done'
    user_input = input("Add to the string or type (done) >")
    if user_input == 'done':
        break
    in_string += user_input # add what the user wrote to the string
	print(f"The current string is {in_string}")
vowel_counter = 0
for letter in in_string: # iterate over all letters
    for vowel in 'aoeuiy': # iterate over all vowels
        if letter == vowel: # if the letter is a vowel
            vowel_counter += 1 # increment the vowel counter
            break # break out of the inner loop, but not the outer loop
print(f"You entered {len(in_string)} characters with {vowel_counter} vowels.")
