#Lab 17: Palindrome and Anagram
# Let's write a palindrome and anagram checker.

# Palindrome
# INSTRUCTIONS: A palindrome is a word that's the same forwards or backwards, e.g. racecar. Another way to think of it is as a word that's equal to its own reverse.
# Write a function check_palindrome which takes a string, and returns True if the string's a palindrome, or False if it's not.

def palindrome_checker(user_input):
    half_length = len(user_input) // 2
    for index in range(half_length):
        if user_input[index] != user_input[len(user_input) - index - 1]:
            return False
    return True

user_input = input("Enter a word to check if it's a palindrome >")
if palindrome_checker(user_input):
    print("Palindrome!")
else:
    print("Not a palindrome.")

#Anagram
# INSTRUCTIONS: Two words are anagrams of eachother if the letters of one can be rearranged to fit the other. e.g. anagram and nag a ram.
# Write another function check_anagram that takes two strings as parameters and returns True if they're anagrams of eachother, False if they're not. The procedure for comparing the two strings is as follow:
# 1. Convert each word to lower case (lower)
# 2. Remove all the spaces from each word (replace)
# 3. Sort the letters of each word (sorted)
# 4. Check if the two are equal

def anagram_checker(user_input1, user_input2):
    user_input1 = user_input1.lower()
    user_input2 = user_input2.lower()
    user_input1 = user_input1.replace(' ', '')
    user_input2 = user_input2.replace(' ', '')
    word1_list = list(user_input1)
    word2_list = list(user_input2)
    word1_list.sort()
    word2_list.sort()
    if word1_list == word2_list:
        return "Anagram!"
    else:
        return "Not an anagram!"

user_input1 = input("Welcome to the anagram checker. Type a word >")
user_input2 = input("Type another word >")

print(anagram_checker(user_input1, user_input2))
