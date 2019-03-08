# #lab17.py
# ''' i want to input a string
# then i want to convert the string into indicies
# then i want to compare the first and last indicies to determine if they are the same
# if they are the same, return true
# else return false
# '''
#
import string
abc_list = list(string.ascii_lowercase) #defines ascii string to abc list variable
#
# def check_palindrome(input_string): #defines the function
#     string_list = [] #empty lisr
#     reverse_list = [] #empty list
#
#     for letter in input_string: #iterates indicies in input string
#         string_list.append(abc_list.index(letter)) #indexes iteration by the abc_list, and then assisgns iterations to string_list
#     for letter in input_string:# iterates indicies in input string
#         reverse_list.append(abc_list.index(letter)) #indexes iterations by the abc_list, and then assings it to the reverse list
#     reverse_list.reverse() #reverses the reverse list
#
#     print(string_list)
#     print(reverse_list)
#
#     if string_list != reverse_list: # with the '==' sign python will compare both lists and return true or false.
#         return False
#     else:
#         return True
#
#
# print(check_palindrome('racecar'))

#Anagram



def check_anagram(first_word, second_word):

    first_word_list = []
    second_word_list = []
    first_word_lower = first_word.lower()
    second_word_lower = second_word.lower()
    first_word_no_space = first_word_lower.replace(' ', '')
    second_word_no_space = second_word_lower.replace(' ','')


    for letter in first_word_no_space:
        first_word_list.append(abc_list.index(letter))
    for letter in second_word_no_space:
        second_word_list.append(abc_list.index(letter))
    first_word_list.sort()
    second_word_list.sort()

    if first_word_list != second_word_list:
        return False
    else:
        return True

first_word = input("enter the first word\n:")
second_word = input("enter the second word\n:")
print(check_anagram( first_word, second_word))
