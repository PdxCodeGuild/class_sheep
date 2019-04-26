in_string = ''
while True:
  user_input = input("add to the string or the type (done) >")
  if user_input == 'done':
    break
  in_string += user_input
print(in_string)
vowel_counter = 0
for letter in in_string:
  # for vowel in 'aoeui':
  #   if letter == vowel:
  #     vowel_counter += 1
  if letter == 'a':
      vowel_counter += 1
print(f"You entered {len(in_string)} characters with {vowel_counter} vowels.")
