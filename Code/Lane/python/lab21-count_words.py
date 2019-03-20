#Lab 21 - Count Words
#Version 1

import string
word_dict = {} # word_dict is a dictionary where the key is the word and the value is the count
word_pairs = {}

#open the book file
f = open("the_adventures_of_reddy_fox.txt", encoding="utf-8")

# Make everything lowercase, strip punctuation, split into a list of words.
book = f.read().lower()

for punctuation in string.punctuation: # remove punctuation
    book = book.replace(punctuation, '')

book_list = book.split() # split the string of words into a list of words where each word is a list item

for word in book_list:
    if word in word_dict.keys(): # builds list of keys in dictionary
        word_dict[word] += 1 # adds an incidence to a word that already exists in the dictionary
    else:
        word_dict[word] =1 # if the word is not yet in the dictionary, this adds it

print('The ten most used words are:')
words = list(word_dict.items()) # .items() returns a list of tuples
words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
    print(words[i])


#version 2

for i in range(len(book_list)-1):
    bigram = (book_list[i] + ' ' + book_list[i+1]) # combines a word with the next one to the right with a space in between
    if bigram in word_pairs:
        word_pairs[bigram] += 1 # if the pair of words is not yet in the dictionary, add them
    else:
        word_pairs[bigram] = 1 # if the pair of words is in the dictioary, add one to its count

print() # to have a line between v1 and v2 printouts

print('The ten most used pairs of words are:')
words = list(word_pairs.items()) # .items() returns a list of tuples
words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
for i in range(min(10, len(words))):  # print the top 10 word pairs, or all of them, whichever is smaller
    print(words[i])
