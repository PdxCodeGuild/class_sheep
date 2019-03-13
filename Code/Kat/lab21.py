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
text = text.replace('   ', ' ')
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
    if word in word_count_dict.keys():
        word_count_dict[word] += 1
    else:
        word_count_dict[word] = 1
# word_dict is a dictionary where the key is the word and the value is the count
words = list(word_count_dict.items()) # .items() returns a list of tuples
words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
    print(words[i])
