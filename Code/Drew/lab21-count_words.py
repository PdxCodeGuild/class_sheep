import string

# open txt file
book = open('alicio_en_mirlando.txt', 'r')
alice = book.read()
print("La Aventuroj de Alicio en Mirlando by Lewis Carroll")

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

#print
print("\nMost frequent words:")
for i in range(min(10, len(words))):
    print(f"{i+1}: {words[i][0]} - {words[i][1]}")

# next, word pairs:
def word_pairs(text):
    pair_dict = []
    for i in range(len(text)-1):
        pair_dict.append((text[i], text[i+1]))
    return pair_dict

words2 = new_alice.split()
words2 = word_pairs(words2)

# same as before, sort word dictionary by value
# create word dictionary
word_dict = {}
for i in words2:
    if i in word_dict:
        word_dict[i] += 1
    else:
        word_dict[i] = 1
# sort
words2 = list(word_dict.items())
words2.sort(key=lambda tup: tup[1], reverse=True)

# print - this seems like a sloppy shortcut (instead of joining tuples)
print("\nMost frequent word pairs:")
for i in range(min(10, len(words2))):
    print(f"{i+1}: {words2[i][0][0]} {words2[i][0][1]} - {words2[i][1]}")
