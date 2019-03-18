# #anamgram Lab 17
# # 1.Convert each word to lower case (lower)
# # 2.Remove all the spaces from each word (replace)
# # 3.Sort the letters of each word (sorted)
# # 4.Check if the words are equal

user_input1 = []
user_input2 = []
#converting user inputs to lowercase strings
user_input1 = input("Enter the first word: ").lower()
user_input2 = input("Enter the second word: ").lower()

#replacing spaces " " with no space ""
user_input1 = user_input1.replace(" ", "")
user_input2 = user_input2.replace(" ", "")

#sorts the letters to be alphabetical
user_input1 = sorted(user_input1)
user_input2 = sorted(user_input2)

#check if the two are equal
if ((user_input1) == (user_input2)):
    print('It\'s an anagram!')
else:
    print('Not an anagram.')


#
# #palindrome Lab 17
user_input = []

#converting user inputs to lowercase strings
user_input = input("Enter the word: ").lower()

#replacing spaces " " with no space ""
user_input = user_input.replace(" ", "")

# reversing sequence of user_input
def reverse_string(s):
    return "".join(reversed(s))

#assigning new variable to the reversed user_input
word_check = reverse_string(user_input)

# checking to see if the user_input is the same as the reversed word
if user_input == word_check :
    print('It\'s a palindrome!')
else:
    print('Not a palindrome.')
