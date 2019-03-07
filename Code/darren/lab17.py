#lab17
#palindrome and anagram checker

'''Palindrome'''
# def reverser(inword):
#     outstring = ''
#     for iteration in range(len(inword)):
#         outstring += inword[length - iteration]
#         active_index + 1
#     return outstring
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
def compready(inword):
    inword = inword.lower()
    inword = inword.replace(' ', '')
    inword = list(inword)
    inword.sort()
    return inword

word1 = input("Please enter your word. >")
word2 = input("Please enter a word to compare to it. >")
comp1 = compready(word1)
comp2 = compready(word2)
if comp1 == comp2:
    print(f"{word1} and {word2} are anagrams.")
else:
    print(f"{word1} and {word2} are not anagrams.")
