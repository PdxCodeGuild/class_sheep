
import string
import math
#pair each word in the list with the following word.
def pair_word(word):

    return(list)

#make a dictionary with keys and value counts.  for each word, the key counter goes up one.
def word_counter(text):
    for word in text:
        if word in word_dict.keys():
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    return(word_dict)

def double_counter(tuple_list):
    for tuple in tuple_list:
        if tuple in word_dict_pair.keys():
            word_dict_pair[tuple] += 1
        else:
            word_dict_pair[tuple] = 1
    return(word_dict_pair)

def word_follow_list(tuple_list, input):

    for (x, y) in tuple_list:
        if input == x:
            y_list.append(y)
    return(y_list)

def word_follow_counter(list):
    for word in list:
        if word in word_follow_dict.keys():
            word_follow_dict[word] += 1
        else:
            word_follow_dict[word] = 1
    return(word_follow_dict)

#=============================================================================

with open('little_folks.txt', 'r') as f:
    text = f.read()

#make everything lowercase
text_lower = text.lower()

#strip punctuation
text_punc = text_lower.strip()

#split list into words
text_list = text_punc.split()

#i want to put each pair of words into a tuple
text_tuple_list = []
for i in range(0,len(text_list)-1,2):
    text_tuple_list.append(tuple((text_list[i],text_list[i+1])))
for tuple in text_tuple_list:
    (first_word, second_word) = tuple


word_dict = {}
word_counter(text_list)

word_dict_pair = {}
double_counter(text_tuple_list)
# print(pair_word(text_list))


# user input a word
user_word = input("Choose a word. \n:")
y_list = []

# user input to find all tuples with that word in text_tuple_list
word_follow_list(text_tuple_list, user_word)
word_follow_dict = {}
word_follow_counter(y_list)



# #word_dict is a dictionary where the key is the word and the value is the count
# words = list(word_dict.items()) # .items() returns a list of tuples
# words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
# for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
#     print(words[i])
#
# print()
#
# #word_dict_pair is a dictionary where the key is the tuple and the value is the count
# tuple = list(word_dict_pair.items()) # .items() returns a list of tuples
# tuple.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
# for i in range(min(10, len(tuple))):  # print the top 10 words, or all of them, whichever is smaller
#     print(tuple[i])

#word_dict_pair is a dictionary where the key is the tuple and the value is the count
words = list(word_follow_dict.items()) # .items() returns a list of tuples
words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
    print(words[i])
