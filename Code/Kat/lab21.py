# Lab 21: Count Words
# Let's write a python module to analyze a given text file containing a book for its vocabulary frequency and display the most frequent words to the user in the terminal. Remember there isn't any "perfect" way to identify a word in english (acronymns, mr/ms, contractions, etc), try to find rules that work best.

# Find a book on Project Gutenberg. Download it as a UTF-8 text file.
# 1. Open the file.
# 2. Make everything lowercase, strip punctuation, split into a list of words.
# 3. Your dictionary will have words as keys and counts as values. If a word isn't in your dictionary yet, add it with a count of 1. If it is, increment its count.
# 4. Print the most frequent top 10 out with their counts. You can do that with the code below.

# word_dict is a dictionary where the key is the word and the value is the count
# words = list(word_dict.items()) # .items() returns a list of tuples
# words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
# for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
#     print(words[i])

# =========================================================================
# import modules
import requests
import string

#function to replace lambda in provided sort code
def return_index_one(in_tuple):
    return in_tuple[1]


# # acquiring text using requests
response = requests.get('http://www.gutenberg.org/files/84/84-0.txt')
text = response.text


# lowercase all letters
text = text.lower()
text = text.replace('“', '"')
text = text.replace('”', '"')
text = text.replace('—', '-')
text = text.replace('  ', ' ')
#removing top 10 most common words
# text = text.replace(' i ', ' ')
# text = text.replace(' the ', ' ')
# text = text.replace(' of ', ' ')
# text = text.replace(' and ', ' ')
# text = text.replace(' to ', ' ')
# text = text.replace(' my ', ' ')
# text = text.replace(' a ', ' ')
# text = text.replace(' in ', ' ')
# text = text.replace(' that ', ' ')
# text = text.replace(' was ', ' ')


# remove punctuation
def remove_punctuation(text):
    result = ""
    for character in text:
        if character not in string.punctuation:
            result += character
    return result
text = remove_punctuation(text)

#turn string into list of words
word_list = text.split()

#make dictionary of words and their number of uses
word_count_dict = {}
for word in word_list:
    if word in word_count_dict:
        word_count_dict[word] += 1
    else:
        word_count_dict[word] = 1


# sort words and and print10  most common words
words = list(word_count_dict.items())
words.sort(key=return_index_one, reverse=True)
for i in range(min(10, len(words))):
    print(words[i])



#Version 2, counting word pairs
# INSTRUCTIONS: Count how often each unique pair of words is used, then print the top 10 most common pairs with their counts.

word_pair_dict = {}
for i in range(len(word_list) - 1):
    word_pair = (word_list[i], word_list[i + 1])
    if word_pair in word_pair_dict:
        word_pair_dict[word_pair] += 1
    else:
        word_pair_dict[word_pair] = 1

#sort pairs and print 10 most common pairs
pairs = list(word_pair_dict.items())
pairs.sort(key=return_index_one, reverse=True)
for i in range(min(10, len(pairs))):
    print(pairs[i])


#Version 3
# INSTRUCTIONS: Let the user enter a word, then show the words which most frequently follow it.
user_pair_dict = {}
user_input = input("What word would you like to check? ")

#Check if user word is in word_pair_dict
for item in word_pair_dict.keys():
    if user_input == item[0]:
        user_pair_dict[item] = word_pair_dict[item]

#Count the number of occurrences and print top 10 or most common
user_pairs = list(user_pair_dict.items())
user_pairs.sort(key=return_index_one, reverse=True)
for i in range(min(10, len(user_pairs))):
    print(user_pairs[i])
