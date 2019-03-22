#lab21.py
'''Count Words in M.R. James "Oh, Whistle, and I'll Come to You, My Lad."'''

import string

'''Returns the second index in a tuple'''
def use_count(in_tuple):
    return in_tuple[1]

'''Removes punctuation and line changes, generates a list'''
def clean_text(in_string):
    in_string = in_string.lower()
    punct = string.punctuation
    for symbol in punct:
        in_string = in_string.replace(symbol, '')
    in_string = in_string.replace('\n', ' ')
    in_string = in_string.replace('  ', ' ')
    out = list(in_string.split(' '))
    return out

'''Generates a dictionary with count of occurances in list'''
def dict_generator(in_list):
    out = {}
    for word in in_list:
        if word in out.keys():
            out[word] += 1
        else:
            out[word] = 1
    return out

'''Sorts list according to second index using use_count function'''
def list_sorter(in_dict):
    out = []
    for key in in_dict:
        out.append((key, in_dict[key]))
    out= sorted(out, key=use_count, reverse=True)
    return out

'''Generate word list'''
print("Searching M.R. James \"Oh, Whistle, and I'll Come to You, My Lad\".")
file = open(r'/Users/pdxguest/Desktop/class_sheep/code/darren/whistle.txt')
text_orig = file.read()
text_orig = clean_text(text_orig)

'''Find most frequent words and most frequent pairs'''
text_dict = dict_generator(text_orig)
text_sort = list_sorter(text_dict)
print(f"These are the most common ten words: {text_sort[0:10]}")

pair_list = []
for item in text_sort[0:10]:
    check_words = item[0]
    for index in range(len(text_orig)-1):
        if text_orig[index] == check_words:
            append_string = text_orig[index] + ' ' + text_orig[index+1]
            pair_list.append(append_string)
pair_dict = dict_generator(pair_list)
text_pairs = list_sorter(pair_dict)
print(f"These are the most common ten pairs of words: {text_pairs[0:10]}")

'''Find most frequent following word'''
while True:
    key_word = input("Please enter the word you wish to search for, or type 'ghost' to exit: ")
    key_word = key_word.lower()
    if key_word == 'ghost':
        break
    key_list = []
    word_count = 0
    for index in range(len(text_orig)-1):
        if text_orig[index] == key_word:
            word_count += 1
            append_string = text_orig[index] + ' ' + text_orig[index+1]
            key_list.append(append_string)
    key_pair_dict = dict_generator(key_list)
    text_keys = list_sorter(key_pair_dict)
    if text_keys == []:
        print(f"There are no occurances of {key_word} in the text.")
    else:
        print(f"For your word, '{key_word}', which occurs {word_count} times, these are the most common ten pairs of following words: {text_keys[0:10]}.")

# {Notes}
