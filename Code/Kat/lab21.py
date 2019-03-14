# count_words
import requests
import string
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
# word_dict is a dictionary where the key is the word and the value is the count
# words = list(word_count_dict.items()) # .items() returns a list of tuples
# words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
# for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
#     print(words[i])

#Version 2, counting word pairs
word_pair_dict = {}
for i in range(len(word_list) - 1):
    word_pair = word_list[i] + ' ' + word_list[i + 1]
    if word_pair in word_pair_dict:
        word_pair_dict[word_pair] += 1
    else:
        word_pair_dict[word_pair] = 1

# pairs = list(word_pair_dict.items()) # .items() returns a list of tuples
# pairs.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
# for i in range(min(10, len(pairs))):  # print the top 10 words, or all of them, whichever is smaller
#     print(pairs[i])

user_input = input("What word would you like to check? ")
choice_pair_dict = {}
choice_index_list = []
if user_input in word_list:
    choice_index_list += word_list[user_input]
# for i in range(len(word_list) - 1):
#     if user_input in word_list:
#         choice_index_list.append(user_input[i])
print (choice_index_list)

# for i in word_list:
#     if user_input in word_list:
#         choice_index_list += i
# print(choice_index_list)
# for choice in word_list:
#     choice_pair = word_list[user_input] + ' ' + word_list[user_input + 1]
