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

# function to return list of words
def word_list(a):
    words = []
    for line in a:
        words += line.split()
    return words

# run function on book
words = word_list(new_alice)

print(new_alice)
#words.sort(key=lambda tup: tup[1], reverse=True)
#for i in range(min(10, len(words))):
    #print(words[i])
