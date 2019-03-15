#lab17
#palindrome and anagram checker

'''Palindrome'''
# def reverser(in_word):
#     out_string = ''
#     for iteration in range(len(in_word)):
#         out_string += in_word[length - iteration]
#         active_index + 1
#     return out_string
#
# def comparer(in1, in2):
#     if in1 == in2:
#         return True
#     else:
#         return False
#
# word1 = input("Please enter your word. >")
# length = len(word1) - 1
# active_index = 0
# word2 = reverser(word1)
# result = comparer(word1, word2)
# if result == True:
#     print(f"{word1} is a palindrome.")
# else:
#     print(f"{word1} is not a palindrome.")

'''Anagram'''
def comp_ready(in_word):
    in_word = in_word.lower()
    in_word = in_word.replace(' ', '')
    in_word = list(in_word)
    in_word.sort()
    return in_word

word1 = input("Please enter your word. >")
word2 = input("Please enter a word to compare to it. >")
comp1 = comp_ready(word1)
comp2 = comp_ready(word2)
if comp1 == comp2:
    print(f"{word1} and {word2} are anagrams.")
else:
    print(f"{word1} and {word2} are not anagrams.")
