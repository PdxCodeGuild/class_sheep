# count_words
import requests
import string
#function to replace lambda in provided sort code
def return_index_one(in_tuple):
    return in_tuple[1]
# # acquiring text using requests
response = requests.get('http://www.gutenberg.org/files/84/84-0.txt')
text = response.text
# # lowercase all letters
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
# #remove punctuation
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
words = list(word_count_dict.items()) # .items() returns a list of tuples
words.sort(key=return_index_one, reverse=True)  # sort largest to smallest, based on count
for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
    print(words[i])



#Version 2, counting word pairs
word_pair_dict = {}
for i in range(len(word_list) - 1):
    word_pair = (word_list[i], word_list[i + 1])
    if word_pair in word_pair_dict:
        word_pair_dict[word_pair] += 1
    else:
        word_pair_dict[word_pair] = 1
#sort pairs and print 10 most common pairs
pairs = list(word_pair_dict.items()) # .items() returns a list of tuples
pairs.sort(key=return_index_one, reverse=True)  # sort largest to smallest, based on count
for i in range(min(10, len(pairs))):  # print the top 10 words, or all of them, whichever is smaller
    print(pairs[i])


#Version 3
user_pair_dict = {}
user_input = input("What word would you like to check? ")
#Check if user word is in word_pair_dict
for item in word_pair_dict.keys():
    if user_input == item[0]:
        user_pair_dict[item] = word_pair_dict[item]
#Count the number of occurrences and print top 10 or most common
user_pairs = list(user_pair_dict.items()) # .items() returns a list of tuples
user_pairs.sort(key=return_index_one, reverse=True)  # sort largest to smallest, based on count
for i in range(min(10, len(user_pairs))):  # print the top 10 words, or all of them, whichever is smaller
    print(user_pairs[i])
