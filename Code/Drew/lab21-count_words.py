import string

# open txt file
book = open('alicio_en_mirlando.txt', 'r')
alice = book.read()

# remove punctuation and numbers
new_alice = ''
for i in list(alice):
    if i not in string.punctuation and i not in string.digits:
        new_alice += ''.join(i)

# change to lower case
new_alice = new_alice.lower()

# split into list of words
words = new_alice.split()

# create word dictionary
word_dict = {}
for i in words:
    if i in word_dict:
        word_dict[i] += 1
    else:
        word_dict[i] = 1

# sort word dictionary by value
words = list(word_dict.items())
words.sort(key=lambda tup: tup[1], reverse=True)

for i in range(min(15, len(words))):
    print(words[i])
